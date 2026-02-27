#!/usr/bin/env python3
from pathlib import Path
import json

import numpy as np
import pandas as pd
from scipy import stats

SEED = 20260220
N_PERM = 1000
INP = Path('reports/elements_pcs_atomicprops_merged.csv')
OUT_JSON = Path('reports/pc_physics_tests/pc1_shell_vs_Z.json')
OUT_CSV = Path('reports/pc_physics_tests/pc1_shell_vs_Z.csv')


def safe_corr(x, y, method='pearson'):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    n = len(d)
    if n < 3:
        return {'n': int(n), 'stat': np.nan, 'p': np.nan}
    xv = d['x'].to_numpy(float)
    yv = d['y'].to_numpy(float)
    if np.allclose(xv, xv[0]) or np.allclose(yv, yv[0]):
        return {'n': int(n), 'stat': np.nan, 'p': np.nan}
    if method == 'pearson':
        r, p = stats.pearsonr(xv, yv)
    elif method == 'spearman':
        r, p = stats.spearmanr(xv, yv)
    else:
        raise ValueError(method)
    return {'n': int(n), 'stat': float(r), 'p': float(p)}


def perm_p(x, y, method='pearson', n_perm=1000, seed=0):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    if len(d) < 3:
        return np.nan
    xv = d['x'].to_numpy(float)
    yv = d['y'].to_numpy(float)
    if np.allclose(xv, xv[0]) or np.allclose(yv, yv[0]):
        return np.nan
    if method == 'pearson':
        obs = stats.pearsonr(xv, yv)[0]
    else:
        obs = stats.spearmanr(xv, yv)[0]
    rng = np.random.default_rng(seed)
    null = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        xp = rng.permutation(xv)
        if method == 'pearson':
            null[i] = stats.pearsonr(xp, yv)[0]
        else:
            null[i] = stats.spearmanr(xp, yv)[0]
    return float((1 + np.sum(np.abs(null) >= abs(obs))) / (n_perm + 1))


def residualize(y, z):
    d = pd.DataFrame({'y': y, 'z': z}).dropna()
    yv = d['y'].to_numpy(float)
    zv = d['z'].to_numpy(float)
    X = np.column_stack([np.ones(len(d)), zv])
    beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
    d['resid'] = yv - X @ beta
    return d


def partial_corr(x, y, control, method='pearson', seed=0):
    d = pd.DataFrame({'x': x, 'y': y, 'c': control}).dropna()
    if len(d) < 5:
        return {'n': int(len(d)), 'stat': np.nan, 'p': np.nan, 'perm_p': np.nan}
    rx = residualize(d['x'], d['c'])
    ry = residualize(d['y'], d['c'])
    m = rx[['resid']].join(ry[['resid']], lsuffix='_x', rsuffix='_y').dropna()
    xv = m['resid_x'].to_numpy(float)
    yv = m['resid_y'].to_numpy(float)

    cor = safe_corr(xv, yv, method=method)
    pperm = perm_p(xv, yv, method=method, n_perm=N_PERM, seed=seed)
    return {'n': cor['n'], 'stat': cor['stat'], 'p': cor['p'], 'perm_p': pperm}


def main():
    if not INP.exists():
        raise FileNotFoundError(INP)
    df = pd.read_csv(INP)

    for c in ['atomic_number', 'period', 'group', 'pc1', 'pc2', 'pc3', 'ionization_energy_1', 'electronegativity_pauling', 'atomic_radius']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    transforms = {
        'period': df['period'],
        'atomic_number': df['atomic_number'],
        'sqrt_period': np.sqrt(df['period']),
        'log_period': np.log(df['period']),
        'inv_period': 1.0 / df['period'],
    }

    rows = []
    corr_results = {}
    seed_i = 0
    for name, vec in transforms.items():
        corr_results[name] = {}
        for method in ['pearson', 'spearman']:
            c = safe_corr(df['pc1'], vec, method=method)
            pp = perm_p(df['pc1'], vec, method=method, n_perm=N_PERM, seed=SEED + seed_i)
            seed_i += 1
            corr_results[name][method] = {
                'n': c['n'],
                'stat': c['stat'],
                'p': c['p'],
                'perm_p': pp,
            }
            rows.append({
                'test': f'corr(pc1,{name})',
                'method': method,
                'n': c['n'],
                'stat': c['stat'],
                'p': c['p'],
                'perm_p': pp,
            })

    partial_defs = {
        'corr(pc1,period|atomic_number)': ('pc1', 'period', 'atomic_number'),
        'corr(pc1,atomic_number|period)': ('pc1', 'atomic_number', 'period'),
    }
    partial_results = {}
    for test_name, (x, y, c) in partial_defs.items():
        partial_results[test_name] = {}
        for method in ['pearson', 'spearman']:
            r = partial_corr(df[x], df[y], df[c], method=method, seed=SEED + seed_i)
            seed_i += 1
            partial_results[test_name][method] = r
            rows.append({
                'test': test_name,
                'method': method,
                'n': r['n'],
                'stat': r['stat'],
                'p': r['p'],
                'perm_p': r['perm_p'],
            })

    payload = {
        'input': str(INP),
        'seed': SEED,
        'n_perm': N_PERM,
        'correlations': corr_results,
        'partial_correlations_residualized': partial_results,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    pd.DataFrame(rows).to_csv(OUT_CSV, index=False)

    print(f'Wrote: {OUT_JSON}')
    print(f'Wrote: {OUT_CSV}')


if __name__ == '__main__':
    main()
