#!/usr/bin/env python3
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy import stats

INP = Path('reports/elements_pcs_atomicprops_merged.csv')
CORR_JSON = Path('reports/pc_atomicprops_correlations.json')
PARTIAL_JSON = Path('reports/pc_atomicprops_partial_correlations.json')
PERM_JSON = Path('reports/pc_atomicprops_permutation_pvalues.json')
NULL_CSV = Path('reports/pc_atomicprops_permutation_null_samples.csv')


def corr_pair(df, x, y, method='pearson'):
    d = df[[x, y]].dropna()
    if len(d) < 3:
        return {'n': int(len(d)), 'r': None}
    return {'n': int(len(d)), 'r': float(d[x].corr(d[y], method=method))}


def partial_corr(df, x, y, z):
    d = df[[x, y, z]].dropna()
    n = len(d)
    if n < 5:
        return {'n': int(n), 'r': None, 'p': None}
    X = d[x].to_numpy(float)
    Y = d[y].to_numpy(float)
    Z = d[z].to_numpy(float)
    M = np.column_stack([np.ones(n), Z])
    bx = np.linalg.lstsq(M, X, rcond=None)[0]
    by = np.linalg.lstsq(M, Y, rcond=None)[0]
    rx = X - M @ bx
    ry = Y - M @ by
    r = float(np.corrcoef(rx, ry)[0, 1])
    dof = n - 3
    if dof <= 0 or abs(r) >= 1:
        p = None
    else:
        t = r * np.sqrt(dof / (1 - r * r))
        p = float(2 * stats.t.sf(abs(t), dof))
    return {'n': int(n), 'r': r, 'p': p}


def perm_test(df, x, y, M=1000, seed=42):
    d = df[[x, y]].dropna().copy()
    n = len(d)
    if n < 3:
        return {'n': int(n), 'r_obs': None, 'p_emp_two_sided': None, 'null': []}
    xvals = d[x].to_numpy(float)
    yvals = d[y].to_numpy(float)
    r_obs = float(np.corrcoef(xvals, yvals)[0, 1])
    rng = np.random.default_rng(seed)
    null = np.empty(M, dtype=float)
    for i in range(M):
        yp = rng.permutation(yvals)
        null[i] = np.corrcoef(xvals, yp)[0, 1]
    p_emp = float((1 + np.sum(np.abs(null) >= abs(r_obs))) / (M + 1))
    return {'n': int(n), 'r_obs': r_obs, 'p_emp_two_sided': p_emp, 'null': null.tolist()}


def main():
    df = pd.read_csv(INP)

    targets = ['electronegativity_pauling', 'ionization_energy_1', 'atomic_radius', 'period', 'group', 'atomic_number']
    pcs = ['pc1', 'pc2', 'pc3']

    corr_out = {'pearson': {}, 'spearman': {}}
    for pc in pcs:
        corr_out['pearson'][pc] = {}
        corr_out['spearman'][pc] = {}
        for t in targets:
            if pc in df.columns and t in df.columns:
                corr_out['pearson'][pc][t] = corr_pair(df, pc, t, method='pearson')
                corr_out['spearman'][pc][t] = corr_pair(df, pc, t, method='spearman')

    partial_out = {
        'pc1_period_given_atomic_number': partial_corr(df, 'pc1', 'period', 'atomic_number'),
        'pc1_ionization_energy_1_given_atomic_number': partial_corr(df, 'pc1', 'ionization_energy_1', 'atomic_number'),
        'pc1_electronegativity_pauling_given_atomic_number': partial_corr(df, 'pc1', 'electronegativity_pauling', 'atomic_number'),
        'pc1_atomic_radius_given_atomic_number': partial_corr(df, 'pc1', 'atomic_radius', 'atomic_number'),
    }

    perm_specs = [
        ('pc1', 'period', 'pc1_period'),
        ('pc1', 'ionization_energy_1', 'pc1_ionization_energy_1'),
        ('pc1', 'electronegativity_pauling', 'pc1_electronegativity_pauling'),
        ('pc1', 'atomic_radius', 'pc1_atomic_radius'),
    ]
    perm_out = {}
    null_rows = []
    for x, y, name in perm_specs:
        res = perm_test(df, x, y, M=1000, seed=42)
        perm_out[name] = {k: v for k, v in res.items() if k != 'null'}
        for i, v in enumerate(res['null'], 1):
            null_rows.append({'test': name, 'shuffle_id': i, 'r_null': v})

    CORR_JSON.write_text(json.dumps(corr_out, indent=2), encoding='utf-8')
    PARTIAL_JSON.write_text(json.dumps(partial_out, indent=2), encoding='utf-8')
    PERM_JSON.write_text(json.dumps(perm_out, indent=2), encoding='utf-8')
    pd.DataFrame(null_rows).to_csv(NULL_CSV, index=False)

    print(f'Wrote: {CORR_JSON}')
    print(f'Wrote: {PARTIAL_JSON}')
    print(f'Wrote: {PERM_JSON}')
    print(f'Wrote: {NULL_CSV}')


if __name__ == '__main__':
    main()
