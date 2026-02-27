#!/usr/bin/env python3
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch

np.random.seed(20260220)

INPUT = Path('reports/elements_pcs_atomicprops_merged.csv')
FIG_DIR = Path('reports/figures')
OUT_ENRICHED = Path('reports/elements_pcs_atomicprops_merged_block.csv')
OUT_SNIPPET = Path('reports/pc_block_figures_snippet.tex')
README = Path('data/external/atomic_properties/README.md')


def normalize_block(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().lower()
    if s in {'s', 'p', 'd', 'f'}:
        return s
    return np.nan


def heuristic_block(row):
    z = row.get('atomic_number', np.nan)
    period = row.get('period', np.nan)
    group = row.get('group', np.nan)
    symbol = str(row.get('symbol', ''))

    if pd.notna(z):
        z = int(z)
        if 57 <= z <= 71 or 89 <= z <= 103:
            return 'f'
    if pd.notna(group):
        g = float(group)
        if 3 <= g <= 12:
            return 'd'
        if 13 <= g <= 18:
            return 'p'
        if 1 <= g <= 2:
            return 's'
    if symbol == 'He':
        return 's'
    if pd.notna(period) and int(period) in {6, 7} and pd.notna(z):
        z = int(z)
        if 57 <= z <= 71 or 89 <= z <= 103:
            return 'f'
    return np.nan


def load_block_mapping():
    candidates = [
        Path('data/external/atomic_properties/atomic_properties_raw.csv'),
        Path('data/external/atomic_properties/atomic_properties_clean.csv'),
        Path('data/external/atomic_properties/atomic_properties_raw.json'),
    ]
    for path in candidates:
        if not path.exists():
            continue
        try:
            if path.suffix.lower() == '.json':
                rdf = pd.read_json(path)
            else:
                rdf = pd.read_csv(path)
        except Exception:
            continue

        cols = {c.lower(): c for c in rdf.columns}
        block_col = cols.get('block')
        if not block_col:
            continue
        z_col = cols.get('atomicnumber') or cols.get('atomic_number')
        s_col = cols.get('symbol')

        if not z_col and not s_col:
            continue

        out = pd.DataFrame()
        if z_col:
            out['atomic_number'] = pd.to_numeric(rdf[z_col], errors='coerce')
        if s_col:
            out['symbol'] = rdf[s_col].astype(str).str.strip()
        out['block'] = rdf[block_col].map(normalize_block)
        out = out.dropna(subset=['block']).copy()

        # Prefer first occurrence with valid block
        if 'atomic_number' in out.columns:
            out = out.sort_values(['atomic_number']).drop_duplicates('atomic_number', keep='first')
        if 'symbol' in out.columns:
            out = out.drop_duplicates('symbol', keep='first')

        return out, path

    return None, None


def add_block_column(df):
    mapping, source_path = load_block_mapping()
    source_note = None

    if mapping is not None:
        out = df.copy()
        out['block'] = np.nan
        if 'atomic_number' in mapping.columns:
            zmap = mapping.dropna(subset=['atomic_number']).set_index('atomic_number')['block']
            out['block'] = out['atomic_number'].map(zmap)
        if 'symbol' in mapping.columns:
            smap = mapping.dropna(subset=['symbol']).set_index('symbol')['block']
            out.loc[out['block'].isna(), 'block'] = out.loc[out['block'].isna(), 'symbol'].map(smap)

        missing = out['block'].isna().sum()
        if missing > 0:
            out.loc[out['block'].isna(), 'block'] = out[out['block'].isna()].apply(heuristic_block, axis=1)
            source_note = (
                f"Primary block source: `{source_path}`. "
                f"Heuristic fallback used for {missing} rows with missing block mapping."
            )
        else:
            source_note = f"Block column derived from local dataset `{source_path}`."
        return out, source_note

    # No mapping dataset: heuristic only
    out = df.copy()
    out['block'] = out.apply(heuristic_block, axis=1)
    source_note = (
        'Block column derived using heuristic fallback: '
        'lanthanides/actinides -> f; groups 3-12 -> d; groups 13-18 -> p; '
        'groups 1-2 + He -> s.'
    )
    return out, source_note


def style_block_axes(ax, title, xlabel, ylabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)


def plot_scatter_by_block(df, xcol, ycol, outpath, title, xlabel, ylabel):
    color_map = {'s': '#1f77b4', 'p': '#ff7f0e', 'd': '#2ca02c', 'f': '#d62728'}
    marker_map = {'s': 'o', 'p': 's', 'd': '^', 'f': 'D'}

    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=250)
    for block in ['s', 'p', 'd', 'f']:
        sub = df[df['block'] == block]
        if len(sub) == 0:
            continue
        ax.scatter(
            sub[xcol], sub[ycol],
            label=f'{block}-block (n={len(sub)})',
            s=35,
            alpha=0.85,
            c=color_map[block],
            marker=marker_map[block],
            edgecolors='black',
            linewidths=0.3,
        )

    style_block_axes(ax, title, xlabel, ylabel)
    ax.legend(frameon=True, loc='best', title='Electron block')
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def assign_pc1_quantiles(values):
    v = pd.Series(values).astype(float)
    mask = v.notna()
    out = pd.Series(index=v.index, dtype='object')
    if mask.sum() == 0:
        return out

    # Deterministic quantiles with rank to avoid duplicate-edge failures
    ranks = v[mask].rank(method='first')
    q = pd.qcut(ranks, 5, labels=['Q1', 'Q2', 'Q3', 'Q4', 'Q5'])
    out.loc[mask] = q.astype(str)
    return out


def plot_periodic_heatmap_pc1(df, out_png, out_pdf):
    tbl = df.dropna(subset=['group', 'period', 'pc1']).copy()
    tbl['group'] = pd.to_numeric(tbl['group'], errors='coerce')
    tbl['period'] = pd.to_numeric(tbl['period'], errors='coerce')
    tbl = tbl.dropna(subset=['group', 'period']).copy()
    tbl['group'] = tbl['group'].astype(int)
    tbl['period'] = tbl['period'].astype(int)
    tbl['pc1_quantile'] = assign_pc1_quantiles(tbl['pc1'])

    quantile_order = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    cmap = plt.cm.viridis
    q_colors = {q: cmap(i / 4) for i, q in enumerate(quantile_order)}

    fig, ax = plt.subplots(figsize=(14, 6), dpi=250)
    ax.set_xlim(0.5, 18.5)
    ax.set_ylim(7.5, 0.5)
    ax.set_aspect('equal')

    for _, r in tbl.iterrows():
        g, p = int(r['group']), int(r['period'])
        q = r['pc1_quantile']
        color = q_colors.get(q, (0.85, 0.85, 0.85, 1.0))
        rect = Rectangle((g - 0.5, p - 0.5), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(g, p, str(r['symbol']), ha='center', va='center', fontsize=6, fontweight='bold')

    ax.set_xticks(range(1, 19))
    ax.set_yticks(range(1, 8))
    ax.set_xlabel('Group')
    ax.set_ylabel('Period')
    ax.set_title('Periodic Table Heatmap: PC1 Quantile by Element')
    ax.grid(False)

    handles = [Patch(facecolor=q_colors[q], edgecolor='black', label=q) for q in quantile_order]
    ax.legend(handles=handles, title='PC1 quantile', loc='upper right', frameon=True)

    fig.tight_layout()
    fig.savefig(out_png)
    fig.savefig(out_pdf)
    plt.close(fig)


def plot_periodic_dominant_band(df, out_png, out_pdf):
    sig_candidates = [
        Path('reports/elements_quantum_liram_full_signature.csv'),
        Path('reports/elements_quantum_liram_signature.csv'),
    ]
    sig_path = next((p for p in sig_candidates if p.exists()), None)
    if sig_path is None:
        return None

    sig = pd.read_csv(sig_path)
    if 'dominant_band' not in sig.columns:
        return None

    join_cols = ['symbol', 'atomic_number', 'dominant_band']
    join_cols = [c for c in join_cols if c in sig.columns]
    dom = sig[join_cols].copy()

    base = df.copy()
    if 'atomic_number' in dom.columns:
        merged = base.merge(dom[['atomic_number', 'dominant_band']].drop_duplicates(), on='atomic_number', how='left')
    else:
        merged = base.merge(dom[['symbol', 'dominant_band']].drop_duplicates(), on='symbol', how='left')

    tbl = merged.dropna(subset=['group', 'period', 'dominant_band']).copy()
    if len(tbl) == 0:
        return None

    tbl['group'] = pd.to_numeric(tbl['group'], errors='coerce')
    tbl['period'] = pd.to_numeric(tbl['period'], errors='coerce')
    tbl = tbl.dropna(subset=['group', 'period']).copy()
    tbl['group'] = tbl['group'].astype(int)
    tbl['period'] = tbl['period'].astype(int)

    bands = sorted(tbl['dominant_band'].astype(str).unique())
    cmap = plt.cm.tab20
    colors = {b: cmap(i / max(1, len(bands) - 1)) for i, b in enumerate(bands)}

    fig, ax = plt.subplots(figsize=(14, 6), dpi=250)
    ax.set_xlim(0.5, 18.5)
    ax.set_ylim(7.5, 0.5)
    ax.set_aspect('equal')

    for _, r in tbl.iterrows():
        g, p = int(r['group']), int(r['period'])
        b = str(r['dominant_band'])
        rect = Rectangle((g - 0.5, p - 0.5), 1, 1, facecolor=colors[b], edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
        ax.text(g, p, str(r['symbol']), ha='center', va='center', fontsize=6, fontweight='bold')

    ax.set_xticks(range(1, 19))
    ax.set_yticks(range(1, 8))
    ax.set_xlabel('Group')
    ax.set_ylabel('Period')
    ax.set_title('Periodic Table by Dominant Spectral Band')

    handles = [Patch(facecolor=colors[b], edgecolor='black', label=b) for b in bands]
    ax.legend(handles=handles, title='Dominant band', loc='upper right', frameon=True, ncol=2, fontsize=7)

    fig.tight_layout()
    fig.savefig(out_png)
    fig.savefig(out_pdf)
    plt.close(fig)

    return sig_path


def write_snippet(include_dominant):
    lines = [
        '% Auto-generated figure snippet for PC1 block analysis',
        '\\begin{figure}[t]',
        '  \\centering',
        '  \\includegraphics[width=0.85\\linewidth]{figures/fig_pc1_vs_period_block.png}',
        '  \\caption{PC1 versus period, colored by electron block (s/p/d/f).}',
        '  \\label{fig:pc1-period-block}',
        '\\end{figure}',
        '',
        '\\begin{figure}[t]',
        '  \\centering',
        '  \\includegraphics[width=0.85\\linewidth]{figures/fig_pc1_vs_atomic_number_block.png}',
        '  \\caption{PC1 versus atomic number, colored by electron block (s/p/d/f).}',
        '  \\label{fig:pc1-z-block}',
        '\\end{figure}',
        '',
        '\\begin{figure}[t]',
        '  \\centering',
        '  \\includegraphics[width=0.95\\linewidth]{figures/fig_periodic_table_pc1_heatmap.png}',
        '  \\caption{Periodic-table layout with cells colored by PC1 quantile (Q1--Q5).}',
        '  \\label{fig:ptable-pc1-heatmap}',
        '\\end{figure}',
    ]

    if include_dominant:
        lines.extend([
            '',
            '\\begin{figure}[t]',
            '  \\centering',
            '  \\includegraphics[width=0.95\\linewidth]{figures/fig_periodic_table_dominant_band.png}',
            '  \\caption{Periodic-table layout colored by dominant spectral band.}',
            '  \\label{fig:ptable-dominant-band}',
            '\\end{figure}',
        ])

    OUT_SNIPPET.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def maybe_append_readme(note):
    if note is None:
        return
    if not README.exists():
        return

    content = README.read_text(encoding='utf-8')
    marker = '## Block Mapping Note'
    if marker in content:
        return

    append = f"\n{marker}\n\n- {note}\n"
    README.write_text(content.rstrip() + '\n' + append, encoding='utf-8')


def main():
    if not INPUT.exists():
        raise FileNotFoundError(f'Missing input file: {INPUT}')

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT)
    enriched, block_note = add_block_column(df)
    enriched.to_csv(OUT_ENRICHED, index=False)

    maybe_append_readme(block_note)

    p1 = FIG_DIR / 'fig_pc1_vs_period_block.png'
    p2 = FIG_DIR / 'fig_pc1_vs_atomic_number_block.png'
    p3 = FIG_DIR / 'fig_periodic_table_pc1_heatmap.png'
    p4 = FIG_DIR / 'fig_periodic_table_pc1_heatmap.pdf'

    plot_scatter_by_block(
        enriched.dropna(subset=['period', 'pc1', 'block']),
        xcol='period',
        ycol='pc1',
        outpath=p1,
        title='PC1 Structure by Period and Electron Block',
        xlabel='Period',
        ylabel='PC1',
    )

    plot_scatter_by_block(
        enriched.dropna(subset=['atomic_number', 'pc1', 'block']),
        xcol='atomic_number',
        ycol='pc1',
        outpath=p2,
        title='PC1 Structure by Atomic Number and Electron Block',
        xlabel='Atomic number',
        ylabel='PC1',
    )

    plot_periodic_heatmap_pc1(enriched, p3, p4)

    p5 = FIG_DIR / 'fig_periodic_table_dominant_band.png'
    p6 = FIG_DIR / 'fig_periodic_table_dominant_band.pdf'
    sig_path = plot_periodic_dominant_band(enriched, p5, p6)

    write_snippet(include_dominant=(sig_path is not None and p5.exists() and p6.exists()))

    print('Saved files:')
    print(f'- {OUT_ENRICHED}')
    print(f'- {p1}')
    print(f'- {p2}')
    print(f'- {p3}')
    print(f'- {p4}')
    if sig_path is not None and p5.exists() and p6.exists():
        print(f'- {p5}')
        print(f'- {p6}')
        print(f'- dominant band source: {sig_path}')
    print(f'- {OUT_SNIPPET}')
    if block_note:
        print(f'- block note: {block_note}')


if __name__ == '__main__':
    main()
