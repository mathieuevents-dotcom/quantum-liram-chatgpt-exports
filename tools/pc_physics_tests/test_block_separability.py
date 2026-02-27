#!/usr/bin/env python3
from pathlib import Path
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold

SEED = 20260220
np.random.seed(SEED)

INP = Path('reports/elements_pcs_atomicprops_merged.csv')
OUT_JSON = Path('reports/pc_physics_tests/block_separability.json')
OUT_CSV = Path('reports/pc_physics_tests/block_separability.csv')

FIG1 = Path('reports/pc_physics_tests/fig_pc1_vs_period.png')
FIG2 = Path('reports/pc_physics_tests/fig_pc1_vs_atomic_number.png')
FIG3 = Path('reports/pc_physics_tests/fig_pc_space_block.png')


def derive_block(row):
    symbol = str(row.get('symbol', ''))
    z = row.get('atomic_number', np.nan)
    g = row.get('group', np.nan)
    p = row.get('period', np.nan)

    if symbol == 'He':
        return 's'

    if pd.notna(z):
        z = int(z)
        if 57 <= z <= 71 or 89 <= z <= 103:
            return 'f'

    if pd.notna(g):
        g = int(g)
        if 1 <= g <= 2:
            return 's'
        if 13 <= g <= 18 and symbol != 'He':
            return 'p'
        if 3 <= g <= 12:
            return 'd'

    if pd.notna(p) and int(p) in {6, 7}:
        return 'f'

    return 'unknown'


def plot_with_fit(x, y, xlabel, ylabel, title, outpath):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    fig, ax = plt.subplots(figsize=(7.2, 5.0), dpi=250)
    ax.scatter(d['x'], d['y'], s=30, alpha=0.85, color='#1f77b4', edgecolors='black', linewidths=0.3)
    if len(d) >= 2 and not np.allclose(d['x'].to_numpy(float), d['x'].iloc[0]):
        m, b = np.polyfit(d['x'].to_numpy(float), d['y'].to_numpy(float), 1)
        xx = np.linspace(d['x'].min(), d['x'].max(), 200)
        ax.plot(xx, m * xx + b, '--', color='black', linewidth=1.2, label='Linear fit')
        ax.legend(frameon=True)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def plot_pc_space(df, outpath):
    cmap = {'s': '#1f77b4', 'p': '#ff7f0e', 'd': '#2ca02c', 'f': '#d62728', 'unknown': '#7f7f7f'}
    fig, ax = plt.subplots(figsize=(7.2, 5.4), dpi=250)
    for block, sub in df.groupby('block'):
        ax.scatter(sub['pc1'], sub['pc2'], s=35, alpha=0.85, c=cmap.get(block, '#7f7f7f'),
                   label=f'{block} (n={len(sub)})', edgecolors='black', linewidths=0.3)
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_title('PC Space (PC1, PC2) Colored by Block')
    ax.grid(alpha=0.25)
    ax.legend(frameon=True, loc='best', title='Block')
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def main():
    if not INP.exists():
        raise FileNotFoundError(INP)
    df = pd.read_csv(INP)

    for c in ['atomic_number', 'period', 'group', 'pc1', 'pc2', 'pc3']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    df['block'] = df.apply(derive_block, axis=1)

    # Figures requested in section E
    plot_with_fit(df['period'], df['pc1'], 'Period', 'PC1', 'PC1 vs Period', FIG1)
    plot_with_fit(df['atomic_number'], df['pc1'], 'Atomic Number', 'PC1', 'PC1 vs Atomic Number', FIG2)
    plot_pc_space(df.dropna(subset=['pc1', 'pc2']), FIG3)

    clf_df = df.dropna(subset=['pc1', 'pc2', 'pc3']).copy()
    clf_df = clf_df[clf_df['block'] != 'unknown'].copy()

    X = clf_df[['pc1', 'pc2', 'pc3']].to_numpy(float)
    y = clf_df['block'].to_numpy()

    class_counts = clf_df['block'].value_counts()
    min_class = int(class_counts.min()) if len(class_counts) else 0
    n_splits = max(2, min(5, min_class)) if min_class >= 2 else 0

    fold_rows = []
    acc_mean = np.nan
    acc_std = np.nan
    f1_mean = np.nan
    f1_std = np.nan

    if n_splits >= 2 and len(np.unique(y)) >= 2:
        cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=SEED)
        for i, (tr, te) in enumerate(cv.split(X, y), 1):
            model = LogisticRegression(max_iter=2000, random_state=SEED)
            model.fit(X[tr], y[tr])
            pred = model.predict(X[te])
            acc = accuracy_score(y[te], pred)
            f1 = f1_score(y[te], pred, average='macro')
            fold_rows.append({'fold': i, 'n_train': int(len(tr)), 'n_test': int(len(te)), 'accuracy': float(acc), 'macro_f1': float(f1)})

        acc_vals = np.array([r['accuracy'] for r in fold_rows], dtype=float)
        f1_vals = np.array([r['macro_f1'] for r in fold_rows], dtype=float)
        acc_mean, acc_std = float(acc_vals.mean()), float(acc_vals.std(ddof=0))
        f1_mean, f1_std = float(f1_vals.mean()), float(f1_vals.std(ddof=0))

    # Statistical tests by block for pc2 and pc3
    test_rows = []
    stats_payload = {}

    for pc in ['pc2', 'pc3']:
        d = clf_df.dropna(subset=[pc]).copy()
        groups = []
        for b in ['s', 'p', 'd', 'f']:
            vals = d[d['block'] == b][pc].to_numpy(float)
            if len(vals) > 0:
                groups.append((b, vals))

        anova_p = np.nan
        kruskal_p = np.nan

        if len(groups) >= 2 and all(len(v) >= 2 for _, v in groups):
            anova_stat, anova_p = stats.f_oneway(*[v for _, v in groups])
        if len(groups) >= 2 and all(len(v) >= 1 for _, v in groups):
            kru_stat, kruskal_p = stats.kruskal(*[v for _, v in groups])

        stats_payload[pc] = {
            'groups_n': {b: int(len(v)) for b, v in groups},
            'anova_p': float(anova_p) if np.isfinite(anova_p) else np.nan,
            'kruskal_p': float(kruskal_p) if np.isfinite(kruskal_p) else np.nan,
        }

        test_rows.append({'section': 'group_tests', 'test': f'{pc}_anova', 'value': stats_payload[pc]['anova_p']})
        test_rows.append({'section': 'group_tests', 'test': f'{pc}_kruskal', 'value': stats_payload[pc]['kruskal_p']})

    test_rows.extend([
        {'section': 'classifier', 'test': 'n_samples', 'value': int(len(clf_df))},
        {'section': 'classifier', 'test': 'n_splits', 'value': int(n_splits)},
        {'section': 'classifier', 'test': 'accuracy_mean', 'value': acc_mean},
        {'section': 'classifier', 'test': 'accuracy_std', 'value': acc_std},
        {'section': 'classifier', 'test': 'macro_f1_mean', 'value': f1_mean},
        {'section': 'classifier', 'test': 'macro_f1_std', 'value': f1_std},
    ])

    payload = {
        'input': str(INP),
        'seed': SEED,
        'block_rule': 's: groups 1-2 + He; p: groups 13-18 except He; d: groups 3-12; f: Z 57-71 or 89-103, fallback period 6-7 with missing group.',
        'class_counts': {k: int(v) for k, v in clf_df['block'].value_counts().to_dict().items()},
        'classifier': {
            'model': 'LogisticRegression(multinomial)',
            'features': ['pc1', 'pc2', 'pc3'],
            'cv': f'{n_splits}-fold StratifiedKFold' if n_splits else 'insufficient_class_counts',
            'fold_metrics': fold_rows,
            'accuracy_mean': acc_mean,
            'accuracy_std': acc_std,
            'macro_f1_mean': f1_mean,
            'macro_f1_std': f1_std,
        },
        'pc_block_tests': stats_payload,
        'figures': [str(FIG1), str(FIG2), str(FIG3)],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    pd.DataFrame(test_rows).to_csv(OUT_CSV, index=False)

    print(f'Wrote: {OUT_JSON}')
    print(f'Wrote: {OUT_CSV}')
    print(f'Wrote: {FIG1}')
    print(f'Wrote: {FIG2}')
    print(f'Wrote: {FIG3}')


if __name__ == '__main__':
    main()
