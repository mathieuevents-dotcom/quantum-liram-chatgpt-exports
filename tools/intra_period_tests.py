#!/usr/bin/env python3
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr, t as student_t

SEED = 20260220
RNG = np.random.default_rng(SEED)
N_PERM_PERIOD = 2000
N_PERM_GLOBAL = 5000

INPUT_CSV = Path('reports/elements_pcs_atomicprops_merged.csv')
OUT_CSV = Path('reports/intra_period_group_stats.csv')
OUT_JSON = Path('reports/partial_pc1_period_group.json')
OUT_MD = Path('reports/intra_period_summary.md')


def safe_corr(func, x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) < 3:
        return np.nan, np.nan
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return np.nan, np.nan
    return func(x, y)


def ols_single_predictor(y, x):
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    n = len(y)
    if n < 3 or np.allclose(x, x[0]):
        return {
            'n': int(n),
            'intercept': np.nan,
            'slope': np.nan,
            'r2': np.nan,
            'p_value_slope': np.nan,
        }

    X = np.column_stack([np.ones(n), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    resid = y - yhat

    ss_res = float(np.sum(resid**2))
    ss_tot = float(np.sum((y - np.mean(y))**2))
    r2 = np.nan if ss_tot == 0 else 1.0 - ss_res / ss_tot

    dof = n - X.shape[1]
    if dof <= 0:
        p_val = np.nan
    else:
        sigma2 = ss_res / dof
        xtx_inv = np.linalg.inv(X.T @ X)
        se_slope = float(np.sqrt(sigma2 * xtx_inv[1, 1])) if xtx_inv[1, 1] > 0 else np.nan
        if not np.isfinite(se_slope) or se_slope == 0:
            p_val = np.nan
        else:
            t_stat = float(beta[1] / se_slope)
            p_val = float(2 * student_t.sf(abs(t_stat), dof))

    return {
        'n': int(n),
        'intercept': float(beta[0]),
        'slope': float(beta[1]),
        'r2': float(r2) if np.isfinite(r2) else np.nan,
        'p_value_slope': float(p_val) if np.isfinite(p_val) else np.nan,
    }


def empirical_p_two_sided(obs, null):
    null = np.asarray(null, dtype=float)
    null = null[np.isfinite(null)]
    if len(null) == 0 or not np.isfinite(obs):
        return np.nan
    return float((1 + np.sum(np.abs(null) >= abs(obs))) / (len(null) + 1))


def main():
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f'Missing input: {INPUT_CSV}')

    df = pd.read_csv(INPUT_CSV)
    df_work = df.dropna(subset=['pc1', 'period', 'group']).copy()
    df_work['period'] = pd.to_numeric(df_work['period'], errors='coerce')
    df_work['group'] = pd.to_numeric(df_work['group'], errors='coerce')
    df_work['pc1'] = pd.to_numeric(df_work['pc1'], errors='coerce')
    df_work = df_work.dropna(subset=['pc1', 'period', 'group']).copy()

    rows = []

    print('=== Intra-Period Group Tests (pc1 vs group) ===')
    print(f'Input: {INPUT_CSV}')
    print(f'N after dropna(pc1, period, group): {len(df_work)}')

    for p in range(1, 8):
        sub = df_work[df_work['period'] == p].copy()
        n = len(sub)
        x = sub['group'].to_numpy(dtype=float)
        y = sub['pc1'].to_numpy(dtype=float)

        pear_r, pear_p = safe_corr(pearsonr, y, x)
        spear_r, spear_p = safe_corr(spearmanr, y, x)
        ols = ols_single_predictor(y, x)

        null_corr = np.full(N_PERM_PERIOD, np.nan, dtype=float)
        if n >= 3 and np.unique(x).size > 1 and np.unique(y).size > 1:
            for i in range(N_PERM_PERIOD):
                y_perm = RNG.permutation(y)
                r_perm, _ = safe_corr(pearsonr, y_perm, x)
                null_corr[i] = r_perm
        perm_p = empirical_p_two_sided(pear_r, null_corr)

        row = {
            'period': p,
            'n': n,
            'pearson_r_pc1_group': pear_r,
            'pearson_p_pc1_group': pear_p,
            'spearman_rho_pc1_group': spear_r,
            'spearman_p_pc1_group': spear_p,
            'ols_intercept': ols['intercept'],
            'ols_slope_group': ols['slope'],
            'ols_r2': ols['r2'],
            'ols_p_slope': ols['p_value_slope'],
            'perm_p_two_sided_pearson': perm_p,
            'n_perm': N_PERM_PERIOD,
        }
        rows.append(row)

        print(
            f"Period {p}: n={n:2d} | "
            f"Pearson r={pear_r:.4f}, p={pear_p:.4g} | "
            f"Spearman rho={spear_r:.4f}, p={spear_p:.4g} | "
            f"OLS R2={ols['r2']:.4f}, p_slope={ols['p_value_slope']:.4g} | "
            f"perm p={perm_p:.4g}"
        )

    out_df = pd.DataFrame(rows)
    out_df.to_csv(OUT_CSV, index=False)

    # Global residualized test: pc1_resid from pc1 ~ period
    y = df_work['pc1'].to_numpy(dtype=float)
    period = df_work['period'].to_numpy(dtype=float)
    group = df_work['group'].to_numpy(dtype=float)

    Xp = np.column_stack([np.ones(len(y)), period])
    beta_p, *_ = np.linalg.lstsq(Xp, y, rcond=None)
    yhat_p = Xp @ beta_p
    pc1_resid = y - yhat_p

    pear_r_g, pear_p_g = safe_corr(pearsonr, pc1_resid, group)
    spear_r_g, spear_p_g = safe_corr(spearmanr, pc1_resid, group)
    ols_g = ols_single_predictor(pc1_resid, group)

    null_global = np.full(N_PERM_GLOBAL, np.nan, dtype=float)
    if len(pc1_resid) >= 3 and np.unique(group).size > 1 and np.unique(pc1_resid).size > 1:
        for i in range(N_PERM_GLOBAL):
            y_perm = RNG.permutation(pc1_resid)
            r_perm, _ = safe_corr(pearsonr, y_perm, group)
            null_global[i] = r_perm
    perm_p_global = empirical_p_two_sided(pear_r_g, null_global)

    partial_payload = {
        'seed': SEED,
        'model_residualization': 'pc1 ~ period',
        'n': int(len(df_work)),
        'residualization_coefficients': {
            'intercept': float(beta_p[0]),
            'period_slope': float(beta_p[1]),
        },
        'pc1_resid_vs_group': {
            'pearson_r': float(pear_r_g) if np.isfinite(pear_r_g) else np.nan,
            'pearson_p': float(pear_p_g) if np.isfinite(pear_p_g) else np.nan,
            'spearman_rho': float(spear_r_g) if np.isfinite(spear_r_g) else np.nan,
            'spearman_p': float(spear_p_g) if np.isfinite(spear_p_g) else np.nan,
            'ols_intercept': float(ols_g['intercept']) if np.isfinite(ols_g['intercept']) else np.nan,
            'ols_slope_group': float(ols_g['slope']) if np.isfinite(ols_g['slope']) else np.nan,
            'ols_r2': float(ols_g['r2']) if np.isfinite(ols_g['r2']) else np.nan,
            'ols_p_slope': float(ols_g['p_value_slope']) if np.isfinite(ols_g['p_value_slope']) else np.nan,
            'perm_p_two_sided_pearson': float(perm_p_global) if np.isfinite(perm_p_global) else np.nan,
            'n_perm': N_PERM_GLOBAL,
        },
    }

    OUT_JSON.write_text(json.dumps(partial_payload, indent=2), encoding='utf-8')

    lines = [
        '# Intra-Period PC1-Group Tests',
        '',
        f'- Input file: `{INPUT_CSV}`',
        f'- Rows after dropping missing `pc1/period/group`: **{len(df_work)}**',
        f'- Random seed: `{SEED}`',
        f'- Within-period permutations per period: `{N_PERM_PERIOD}`',
        f'- Global residualized permutations: `{N_PERM_GLOBAL}`',
        '',
        '## Per-Period Results',
        '',
        '| period | n | pearson_r | pearson_p | spearman_rho | spearman_p | ols_r2 | ols_p_slope | perm_p_two_sided |',
        '|---:|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]

    for _, r in out_df.iterrows():
        lines.append(
            f"| {int(r['period'])} | {int(r['n'])} | {r['pearson_r_pc1_group']:.4f} | {r['pearson_p_pc1_group']:.4g} | "
            f"{r['spearman_rho_pc1_group']:.4f} | {r['spearman_p_pc1_group']:.4g} | "
            f"{r['ols_r2']:.4f} | {r['ols_p_slope']:.4g} | {r['perm_p_two_sided_pearson']:.4g} |"
        )

    g = partial_payload['pc1_resid_vs_group']
    lines.extend([
        '',
        '## Global Residualized Test',
        '',
        '- Residualization model: `pc1 ~ period`',
        f"- Pearson(`pc1_resid`, `group`) = **{g['pearson_r']:.4f}** (p={g['pearson_p']:.4g})",
        f"- Spearman(`pc1_resid`, `group`) = **{g['spearman_rho']:.4f}** (p={g['spearman_p']:.4g})",
        f"- OLS `pc1_resid ~ group`: R^2={g['ols_r2']:.4f}, slope p={g['ols_p_slope']:.4g}",
        f"- Permutation two-sided p-value (Pearson): **{g['perm_p_two_sided_pearson']:.4g}**",
    ])

    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print('\n=== Global Residualized Test ===')
    print(
        f"Residualization: pc1 ~ period | n={partial_payload['n']} | "
        f"Pearson r={g['pearson_r']:.4f}, p={g['pearson_p']:.4g} | "
        f"Spearman rho={g['spearman_rho']:.4f}, p={g['spearman_p']:.4g} | "
        f"OLS R2={g['ols_r2']:.4f}, p_slope={g['ols_p_slope']:.4g} | "
        f"perm p={g['perm_p_two_sided_pearson']:.4g}"
    )

    print('\nOutputs:')
    print(f'- {OUT_CSV}')
    print(f'- {OUT_JSON}')
    print(f'- {OUT_MD}')


if __name__ == '__main__':
    main()
