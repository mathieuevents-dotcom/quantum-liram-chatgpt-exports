#!/usr/bin/env python3
from pathlib import Path
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

SEED = 20260220
N_PERM = 5000

INPUT = Path('reports/elements_pcs_atomicprops_merged.csv')
FIG_DIR = Path('reports/figures')
OUT_CORR_CSV = Path('reports/pc2_pc3_correlations.csv')
OUT_PARTIAL_CSV = Path('reports/pc2_pc3_partial_correlations.csv')
OUT_JSON = Path('reports/pc2_pc3_correlations.json')
OUT_TEX = Path('reports/pc2_pc3_snippet.tex')

PCS = ['pc2', 'pc3']
TARGETS = [
    'period',
    'group',
    'atomic_number',
    'electronegativity_pauling',
    'ionization_energy_1',
    'atomic_radius',
]

TARGET_LABELS = {
    'period': 'Period',
    'group': 'Group',
    'atomic_number': 'Atomic number',
    'electronegativity_pauling': 'Electronegativity (Pauling)',
    'ionization_energy_1': 'First ionization energy (eV)',
    'atomic_radius': 'Atomic radius (pm)',
}

PLOT_FILES = {
    'pc2_primary': Path('reports/figures/fig_pc2_vs_period.png'),
    'pc2_secondary': Path('reports/figures/fig_pc2_vs_ionization.png'),
    'pc3_primary': Path('reports/figures/fig_pc3_vs_period.png'),
    'pc3_secondary': Path('reports/figures/fig_pc3_vs_radius.png'),
}


def corr_stats(x, y, method='pearson'):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    n = len(d)
    if n < 3:
        return {'n': int(n), 'r': np.nan, 'p': np.nan}

    xv = d['x'].to_numpy(dtype=float)
    yv = d['y'].to_numpy(dtype=float)
    if np.allclose(xv, xv[0]) or np.allclose(yv, yv[0]):
        return {'n': int(n), 'r': np.nan, 'p': np.nan}

    if method == 'pearson':
        r, p = stats.pearsonr(xv, yv)
    elif method == 'spearman':
        r, p = stats.spearmanr(xv, yv)
    else:
        raise ValueError(f'Unsupported method: {method}')

    return {'n': int(n), 'r': float(r), 'p': float(p)}


def permutation_pvalue(x, y, method='pearson', n_perm=N_PERM, seed=SEED):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    n = len(d)
    if n < 3:
        return {'n': int(n), 'r_obs': np.nan, 'perm_p': np.nan}

    xv = d['x'].to_numpy(dtype=float)
    yv = d['y'].to_numpy(dtype=float)
    if np.allclose(xv, xv[0]) or np.allclose(yv, yv[0]):
        return {'n': int(n), 'r_obs': np.nan, 'perm_p': np.nan}

    if method == 'pearson':
        r_obs = float(stats.pearsonr(xv, yv)[0])
    elif method == 'spearman':
        r_obs = float(stats.spearmanr(xv, yv)[0])
    else:
        raise ValueError(f'Unsupported method: {method}')

    rng = np.random.default_rng(seed)
    null = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        xp = rng.permutation(xv)
        if method == 'pearson':
            null[i] = stats.pearsonr(xp, yv)[0]
        else:
            null[i] = stats.spearmanr(xp, yv)[0]

    p_emp = float((1 + np.sum(np.abs(null) >= abs(r_obs))) / (n_perm + 1))
    return {'n': int(n), 'r_obs': r_obs, 'perm_p': p_emp}


def residualize_on_period(df, pc_col):
    d = df[[pc_col, 'period']].dropna().copy()
    x = d['period'].to_numpy(dtype=float)
    y = d[pc_col].to_numpy(dtype=float)
    X = np.column_stack([np.ones(len(d)), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    out = d.copy()
    out[f'{pc_col}_resid_period'] = resid
    return out[[f'{pc_col}_resid_period']]


def line_fit(ax, x, y):
    if len(x) < 2:
        return
    xs = np.asarray(x, dtype=float)
    ys = np.asarray(y, dtype=float)
    if np.allclose(xs, xs[0]):
        return
    m, b = np.polyfit(xs, ys, 1)
    xx = np.linspace(xs.min(), xs.max(), 200)
    yy = m * xx + b
    ax.plot(xx, yy, color='black', linestyle='--', linewidth=1.2, label='Linear fit')


def make_scatter(df, pc_col, target, outpath):
    d = df[[pc_col, target]].dropna().copy()
    fig, ax = plt.subplots(figsize=(7.5, 5.2), dpi=250)

    ax.scatter(d[target], d[pc_col], s=30, alpha=0.8, color='#1f77b4', edgecolors='black', linewidths=0.3)
    line_fit(ax, d[target].to_numpy(float), d[pc_col].to_numpy(float))

    pear = corr_stats(d[pc_col], d[target], method='pearson')
    ax.set_xlabel(TARGET_LABELS.get(target, target))
    ax.set_ylabel(pc_col.upper())
    ax.set_title(f"{pc_col.upper()} vs {TARGET_LABELS.get(target, target)}")
    ax.legend(loc='best', frameon=True)
    ax.grid(alpha=0.25)

    txt = f"n={pear['n']}, Pearson r={pear['r']:.3f}" if np.isfinite(pear['r']) else f"n={pear['n']}, Pearson r=NA"
    ax.text(0.02, 0.98, txt, transform=ax.transAxes, va='top', ha='left', fontsize=9,
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def build_latex(top_rows, plot_mapping):
    lines = [
        '% Auto-generated snippet: PC2/PC3 analysis',
        '\\begin{table}[t]',
        '  \\centering',
        '  \\caption{Top PC2/PC3 Pearson correlations by absolute effect size.}',
        '  \\begin{tabular}{l l r r r}',
        '    \\hline',
        '    PC & Variable & $n$ & $r$ & $p_{perm}$ \\\\',
        '    \\hline',
    ]

    for _, r in top_rows.iterrows():
        lines.append(
            f"    {r['pc']} & {r['target']} & {int(r['n'])} & {r['r']:.3f} & {r['perm_p']:.4g} \\\\"
        )

    lines.extend([
        '    \\hline',
        '  \\end{tabular}',
        '  \\label{tab:pc2-pc3-topcorr}',
        '\\end{table}',
        '',
    ])

    for slot in ['pc2_primary', 'pc2_secondary', 'pc3_primary', 'pc3_secondary']:
        meta = plot_mapping[slot]
        fig_rel = str(PLOT_FILES[slot]).replace('reports/', '')
        lines.extend([
            '\\begin{figure}[t]',
            '  \\centering',
            f'  \\includegraphics[width=0.82\\linewidth]{{{fig_rel}}}',
            f"  \\caption{{{meta['pc'].upper()} vs {TARGET_LABELS.get(meta['target'], meta['target'])}.}}",
            f"  \\label{{fig:{meta['pc']}-{meta['target']}}}",
            '\\end{figure}',
            '',
        ])

    OUT_TEX.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f'Missing input file: {INPUT}')

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT)

    corr_rows = []
    pair_idx = 0
    for pc in PCS:
        for target in TARGETS:
            for method in ('pearson', 'spearman'):
                c = corr_stats(df[pc], df[target], method=method)
                perm = permutation_pvalue(df[pc], df[target], method=method, n_perm=N_PERM, seed=SEED + pair_idx)
                pair_idx += 1
                corr_rows.append({
                    'pc': pc,
                    'target': target,
                    'method': method,
                    'n': c['n'],
                    'r': c['r'],
                    'p': c['p'],
                    'perm_p': perm['perm_p'],
                    'n_perm': N_PERM,
                })

    corr_df = pd.DataFrame(corr_rows)
    corr_df.to_csv(OUT_CORR_CSV, index=False)

    # Partial via residualization: residualize each PC on period, then test vs properties.
    properties = ['group', 'atomic_number', 'electronegativity_pauling', 'ionization_energy_1', 'atomic_radius']
    partial_rows = []
    for pc in PCS:
        resid_col = f'{pc}_resid_period'
        resid = residualize_on_period(df, pc)
        tmp = df.join(resid, how='left')
        for target in properties:
            for method in ('pearson', 'spearman'):
                c = corr_stats(tmp[resid_col], tmp[target], method=method)
                partial_rows.append({
                    'pc': pc,
                    'residualized_on': 'period',
                    'target': target,
                    'method': method,
                    'n': c['n'],
                    'r': c['r'],
                    'p': c['p'],
                })

    partial_df = pd.DataFrame(partial_rows)
    partial_df.to_csv(OUT_PARTIAL_CSV, index=False)

    # Choose most correlated pairs automatically (Pearson |r|): top 2 for each PC.
    pear = corr_df[corr_df['method'] == 'pearson'].copy()
    pear['abs_r'] = pear['r'].abs()

    plot_mapping = {}
    for pc, slots in [('pc2', ['pc2_primary', 'pc2_secondary']), ('pc3', ['pc3_primary', 'pc3_secondary'])]:
        top = pear[pear['pc'] == pc].sort_values('abs_r', ascending=False).dropna(subset=['r']).head(2)
        top_records = top.to_dict('records')
        for i, slot in enumerate(slots):
            if i < len(top_records):
                plot_mapping[slot] = {'pc': pc, 'target': top_records[i]['target']}
            else:
                fallback = 'period' if slot.endswith('primary') else 'atomic_number'
                plot_mapping[slot] = {'pc': pc, 'target': fallback}

    for slot, meta in plot_mapping.items():
        make_scatter(df, meta['pc'], meta['target'], PLOT_FILES[slot])

    top10 = pear.sort_values('abs_r', ascending=False).head(10).copy()
    top10 = top10[['pc', 'target', 'n', 'r', 'p', 'perm_p']]

    payload = {
        'input': str(INPUT),
        'seed': SEED,
        'n_perm': N_PERM,
        'targets': TARGETS,
        'correlations': {
            'csv': str(OUT_CORR_CSV),
            'rows': corr_df.to_dict(orient='records'),
        },
        'partial_correlations': {
            'csv': str(OUT_PARTIAL_CSV),
            'rows': partial_df.to_dict(orient='records'),
        },
        'selected_plots': {k: {'pc': v['pc'], 'target': v['target'], 'file': str(PLOT_FILES[k])} for k, v in plot_mapping.items()},
        'top10_by_abs_r_pearson': top10.to_dict(orient='records'),
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding='utf-8')

    build_latex(top10.head(8), plot_mapping)

    print('Outputs:')
    print(f'- {OUT_CORR_CSV}')
    print(f'- {OUT_PARTIAL_CSV}')
    print(f'- {OUT_JSON}')
    print(f'- {OUT_TEX}')
    for slot in ['pc2_primary', 'pc2_secondary', 'pc3_primary', 'pc3_secondary']:
        print(f"- {PLOT_FILES[slot]} ({plot_mapping[slot]['pc']} vs {plot_mapping[slot]['target']})")

    print('\nTop 10 strongest (Pearson, |r|) with permutation p-values:')
    print(top10.to_string(index=False))


if __name__ == '__main__':
    main()
