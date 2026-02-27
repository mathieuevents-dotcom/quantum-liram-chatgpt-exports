#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

SEED = 20260220
N_PERM = 10000
RNG = np.random.default_rng(SEED)

MERGED_CANDIDATES = [
    Path('reports/elements_pcs_atomicprops_merged.csv'),
]
FEATURES_CANDIDATES = [
    Path('2026-02-16/artifacts/2026-02-16/reports/bandcount/K_37/features.csv'),
]

OUT1_JSON = Path('reports/pc1_vs_neff_results.json')
OUT1_FIG_A = Path('reports/fig_pc1_vs_sqrt_neff_A.png')
OUT1_FIG_B = Path('reports/fig_pc1_vs_sqrt_neff_B.png')

OUT2_JSON = Path('reports/pc2_vs_zeff_results.json')
OUT2_FIG_SLATER = Path('reports/fig_pc2_vs_zeff.png')
OUT2_FIG_PROXY = Path('reports/fig_pc2_vs_zeff_proxy.png')
OUT2_FIG_PROXY2 = Path('reports/fig_pc2_vs_zeff_proxy2.png')

OUT3_JSON = Path('reports/pca_robustness_fblock_excluded.json')
OUT3_FIG1 = Path('reports/fig_pc1_baseline_vs_new.png')
OUT3_FIG2 = Path('reports/fig_pc2_baseline_vs_new.png')
OUT3_FIG3 = Path('reports/fig_pc3_baseline_vs_new.png')

NUMERIC_COLS = [
    'atomic_number',
    'period',
    'group',
    'pc1',
    'pc2',
    'pc3',
    'ionization_energy_1',
    'electronegativity_pauling',
    'atomic_radius',
]

NOBLE_CORE_EXPANSIONS = {
    '[He]': '1s2',
    '[Ne]': '1s2 2s2 2p6',
    '[Ar]': '1s2 2s2 2p6 3s2 3p6',
    '[Kr]': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6',
    '[Xe]': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6',
    '[Rn]': '1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6p6',
}


def ensure_merged_exists() -> Path:
    for p in MERGED_CANDIDATES:
        if p.exists():
            return p

    # Rebuild with existing pipeline scripts if missing.
    steps = [
        ['python3', 'tools/compute_element_pcs.py'],
        ['python3', 'tools/merge_pcs_with_atomic_properties.py'],
    ]
    for cmd in steps:
        subprocess.check_call(cmd)

    for p in MERGED_CANDIDATES:
        if p.exists():
            return p
    raise FileNotFoundError('Could not locate or rebuild merged PCs table')


def get_features_path() -> Path:
    for p in FEATURES_CANDIDATES:
        if p.exists():
            return p
    found = sorted(Path('.').glob('**/bandcount/K_37/features.csv'))
    if found:
        return found[-1]
    raise FileNotFoundError('Could not locate K_37 features.csv')


def add_block_column(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if 'block' not in out.columns:
        out['block'] = 'unknown'

    z = pd.to_numeric(out['atomic_number'], errors='coerce')
    g = pd.to_numeric(out['group'], errors='coerce')

    fmask = ((z >= 57) & (z <= 71)) | ((z >= 89) & (z <= 103))
    out.loc[fmask, 'block'] = 'f'

    dmask = (~fmask) & g.between(3, 12, inclusive='both')
    pmask = g.between(13, 18, inclusive='both')
    smask = g.between(1, 2, inclusive='both')

    out.loc[dmask, 'block'] = 'd'
    out.loc[pmask, 'block'] = 'p'
    out.loc[smask, 'block'] = 's'

    out['block'] = out['block'].fillna('unknown').astype(str)
    return out


def corr_with_perm(x: np.ndarray, y: np.ndarray, n_perm: int, seed: int) -> Dict[str, float]:
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    n = len(d)
    if n < 3:
        return {
            'n': int(n),
            'pearson_r': np.nan,
            'pearson_p': np.nan,
            'spearman_rho': np.nan,
            'spearman_p': np.nan,
            'perm_p_two_sided_pearson': np.nan,
        }

    xv = d['x'].to_numpy(float)
    yv = d['y'].to_numpy(float)
    if np.allclose(xv, xv[0]) or np.allclose(yv, yv[0]):
        return {
            'n': int(n),
            'pearson_r': np.nan,
            'pearson_p': np.nan,
            'spearman_rho': np.nan,
            'spearman_p': np.nan,
            'perm_p_two_sided_pearson': np.nan,
        }

    pear_r, pear_p = stats.pearsonr(xv, yv)
    spe_r, spe_p = stats.spearmanr(xv, yv)

    rng = np.random.default_rng(seed)
    null = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        yp = rng.permutation(yv)
        null[i] = stats.pearsonr(xv, yp)[0]
    p_emp = (1 + np.sum(np.abs(null) >= abs(pear_r))) / (n_perm + 1)

    return {
        'n': int(n),
        'pearson_r': float(pear_r),
        'pearson_p': float(pear_p),
        'spearman_rho': float(spe_r),
        'spearman_p': float(spe_p),
        'perm_p_two_sided_pearson': float(p_emp),
    }


def plot_scatter(x: np.ndarray, y: np.ndarray, xlabel: str, ylabel: str, title: str, outpath: Path):
    d = pd.DataFrame({'x': x, 'y': y}).dropna()
    fig, ax = plt.subplots(figsize=(7.2, 5.0), dpi=250)
    ax.scatter(d['x'], d['y'], s=30, alpha=0.85, color='#1f77b4', edgecolors='black', linewidths=0.3)

    if len(d) >= 2 and not np.allclose(d['x'].to_numpy(float), d['x'].iloc[0]):
        m, b = np.polyfit(d['x'].to_numpy(float), d['y'].to_numpy(float), 1)
        xx = np.linspace(d['x'].min(), d['x'].max(), 200)
        ax.plot(xx, m * xx + b, '--', color='black', linewidth=1.2, label='Linear fit')
        ax.legend(loc='best', frameon=True)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)


def try_import_mendeleev():
    try:
        import mendeleev  # noqa: F401
        return True, 'already_installed'
    except Exception:
        pass

    target = Path('/tmp/mendeleev_pkg')
    target.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, '-m', 'pip', 'install', '--quiet', '--target', str(target), 'mendeleev']
    try:
        subprocess.check_call(cmd)
        if str(target) not in sys.path:
            sys.path.insert(0, str(target))
        import mendeleev  # noqa: F401
        return True, 'installed_to_tmp'
    except Exception as e:
        return False, f'install_failed: {e}'


def expand_noble_core(conf: str) -> str:
    c = conf.strip()
    for core, exp in NOBLE_CORE_EXPANSIONS.items():
        if core in c:
            c = c.replace(core, exp)
    return c


def parse_config(conf: str) -> List[Tuple[int, str, int]]:
    conf = expand_noble_core(conf)
    out = []
    for tok in conf.replace(',', ' ').split():
        tok = tok.strip()
        if not tok:
            continue
        if len(tok) < 3 or not tok[0].isdigit() or tok[1] not in 'spdf':
            continue
        try:
            n = int(tok[0])
            l = tok[1]
            e = int(tok[2:])
            out.append((n, l, e))
        except Exception:
            continue
    return out


def slater_zeff_nsnp_from_conf(Z: int, conf: str) -> float:
    orbitals = parse_config(conf)
    if not orbitals:
        return np.nan

    n_max = max(n for n, _, _ in orbitals)
    nmax_sp = sum(e for n, l, e in orbitals if n == n_max and l in {'s', 'p'})
    if nmax_sp <= 0:
        return np.nan

    same_sp = sum(e for n, l, e in orbitals if n == n_max and l in {'s', 'p'})
    n1_sp = sum(e for n, l, e in orbitals if n == n_max - 1 and l in {'s', 'p'})
    n1_df = sum(e for n, l, e in orbitals if n == n_max - 1 and l in {'d', 'f'})
    lower = sum(e for n, _, e in orbitals if n <= n_max - 2)

    S = 0.35 * max(same_sp - 1, 0) + 0.85 * n1_sp + 1.00 * (n1_df + lower)
    zeff = float(Z - S)
    return max(zeff, 0.0)


def compute_slater_zeff(df: pd.DataFrame) -> Tuple[pd.Series, Dict[str, object]]:
    ok, mode = try_import_mendeleev()
    notes = {
        'attempted_mendeleev': True,
        'mendeleev_status': mode,
        'assumption': 'Slater-like Zeff for valence ns/np electron from electron configuration.',
    }
    if not ok:
        return pd.Series(np.nan, index=df.index), notes

    try:
        from mendeleev import element
    except Exception as e:
        notes['mendeleev_import_error'] = str(e)
        return pd.Series(np.nan, index=df.index), notes

    vals = []
    for _, r in df.iterrows():
        z = r.get('atomic_number', np.nan)
        if pd.isna(z):
            vals.append(np.nan)
            continue
        z = int(z)
        try:
            el = element(z)
        except Exception:
            vals.append(np.nan)
            continue

        conf = None
        for attr in ('econf', 'ec', 'electron_configuration'):
            if hasattr(el, attr):
                try:
                    v = getattr(el, attr)
                    conf = str(v)
                    if conf and conf.lower() != 'none':
                        break
                except Exception:
                    continue

        if not conf:
            vals.append(np.nan)
            continue

        zeff = slater_zeff_nsnp_from_conf(z, conf)
        vals.append(zeff)

    s = pd.Series(vals, index=df.index, dtype=float)
    notes['coverage_n'] = int(s.notna().sum())
    notes['coverage_total'] = int(len(s))
    return s, notes


def compute_pca_scores(X: np.ndarray, n_comp: int = 3) -> np.ndarray:
    mu = X.mean(axis=0)
    sd = X.std(axis=0, ddof=0)
    sd_safe = np.where(sd > 0, sd, 1.0)
    Xz = (X - mu) / sd_safe
    C = np.corrcoef(Xz, rowvar=False)
    vals, vecs = np.linalg.eigh(C)
    idx = np.argsort(vals)[::-1]
    vecs = vecs[:, idx]
    scores = Xz @ vecs[:, :n_comp]
    return scores


def best_signed_corr(a: np.ndarray, b: np.ndarray) -> Dict[str, object]:
    d = pd.DataFrame({'a': a, 'b': b}).dropna()
    if len(d) < 3:
        return {
            'n': int(len(d)),
            'corr_raw': np.nan,
            'best_abs_corr': np.nan,
            'flipped': False,
        }
    r = float(stats.pearsonr(d['a'], d['b'])[0])
    flipped = r < 0
    return {
        'n': int(len(d)),
        'corr_raw': r,
        'best_abs_corr': float(abs(r)),
        'flipped': bool(flipped),
    }


def main():
    np.random.seed(SEED)

    merged_path = ensure_merged_exists()
    features_path = get_features_path()

    df = pd.read_csv(merged_path)
    for c in NUMERIC_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    df = add_block_column(df)

    saved_paths: List[str] = []

    # TEST 1: PC1 vs sqrt(n_eff)
    n_eff_A = df['period'].copy()
    n_eff_B = df['period'].copy()
    n_eff_B = np.where(df['block'].eq('d'), n_eff_B - 1, n_eff_B)
    n_eff_B = np.where(df['block'].eq('f'), n_eff_B - 2, n_eff_B)
    n_eff_B = pd.Series(np.clip(pd.to_numeric(n_eff_B, errors='coerce'), 1, None), index=df.index)

    sqrt_A = np.sqrt(pd.to_numeric(n_eff_A, errors='coerce'))
    sqrt_B = np.sqrt(pd.to_numeric(n_eff_B, errors='coerce'))

    t1_A = corr_with_perm(df['pc1'].to_numpy(float), sqrt_A.to_numpy(float), n_perm=N_PERM, seed=SEED + 11)
    t1_B = corr_with_perm(df['pc1'].to_numpy(float), sqrt_B.to_numpy(float), n_perm=N_PERM, seed=SEED + 12)

    plot_scatter(
        sqrt_A.to_numpy(float),
        df['pc1'].to_numpy(float),
        xlabel='sqrt(n_eff_A)',
        ylabel='PC1',
        title='PC1 vs sqrt(n_eff_A), n_eff_A = period',
        outpath=OUT1_FIG_A,
    )
    plot_scatter(
        sqrt_B.to_numpy(float),
        df['pc1'].to_numpy(float),
        xlabel='sqrt(n_eff_B)',
        ylabel='PC1',
        title='PC1 vs sqrt(n_eff_B), block-adjusted',
        outpath=OUT1_FIG_B,
    )

    out1 = {
        'input': str(merged_path),
        'seed': SEED,
        'n_perm': N_PERM,
        'definitions': {
            'n_eff_A': 'period',
            'n_eff_B': 'period (s/p), period-1 (d), period-2 (f), clipped >=1',
        },
        'results': {
            'pc1_vs_sqrt_neff_A': t1_A,
            'pc1_vs_sqrt_neff_B': t1_B,
        },
        'figures': [str(OUT1_FIG_A), str(OUT1_FIG_B)],
    }
    OUT1_JSON.write_text(json.dumps(out1, indent=2), encoding='utf-8')
    saved_paths += [str(OUT1_JSON), str(OUT1_FIG_A), str(OUT1_FIG_B)]

    # TEST 2: PC2 vs Zeff (approx)
    zeff_slater, slater_meta = compute_slater_zeff(df)
    zeff_proxy = df['atomic_number'] / df['atomic_radius']
    zeff_proxy2 = df['ionization_energy_1'] * (df['period'] ** 2)

    variants = {
        'slater_nsnp': zeff_slater,
        'proxy_z_over_radius': zeff_proxy,
        'proxy_ie_period2': zeff_proxy2,
    }

    results2 = {}
    for i, (name, vec) in enumerate(variants.items()):
        res = corr_with_perm(df['pc2'].to_numpy(float), pd.to_numeric(vec, errors='coerce').to_numpy(float), n_perm=N_PERM, seed=SEED + 100 + i)
        results2[name] = res

    # Figures
    if zeff_slater.notna().sum() >= 3:
        plot_scatter(
            zeff_slater.to_numpy(float), df['pc2'].to_numpy(float),
            xlabel='Zeff (Slater approx, ns/np valence)', ylabel='PC2',
            title='PC2 vs Zeff (Slater approx)', outpath=OUT2_FIG_SLATER,
        )
        saved_paths.append(str(OUT2_FIG_SLATER))

    plot_scatter(
        zeff_proxy.to_numpy(float), df['pc2'].to_numpy(float),
        xlabel='Zeff proxy = Z / atomic_radius', ylabel='PC2',
        title='PC2 vs Zeff Proxy (Z / radius)', outpath=OUT2_FIG_PROXY,
    )
    plot_scatter(
        zeff_proxy2.to_numpy(float), df['pc2'].to_numpy(float),
        xlabel='Zeff proxy2 = ionization_energy_1 * period^2', ylabel='PC2',
        title='PC2 vs Zeff Proxy2 (IE * period^2)', outpath=OUT2_FIG_PROXY2,
    )
    saved_paths += [str(OUT2_FIG_PROXY), str(OUT2_FIG_PROXY2)]

    out2 = {
        'input': str(merged_path),
        'seed': SEED,
        'n_perm': N_PERM,
        'methods': {
            'slater_nsnp': {
                'description': 'Slater-like Zeff for valence ns/np electron using electron configuration from mendeleev if available.',
                'status': 'used' if zeff_slater.notna().sum() >= 3 else 'not_available_fallback_to_proxy',
                'meta': slater_meta,
            },
            'proxy_z_over_radius': {
                'formula': 'atomic_number / atomic_radius',
                'requires': ['atomic_number', 'atomic_radius'],
            },
            'proxy_ie_period2': {
                'formula': 'ionization_energy_1 * period^2',
                'requires': ['ionization_energy_1', 'period'],
            },
        },
        'results': results2,
        'figures': [
            str(OUT2_FIG_SLATER) if OUT2_FIG_SLATER.exists() else None,
            str(OUT2_FIG_PROXY),
            str(OUT2_FIG_PROXY2),
        ],
    }
    OUT2_JSON.write_text(json.dumps(out2, indent=2), encoding='utf-8')
    saved_paths.append(str(OUT2_JSON))

    # TEST 3: Robustness removing lanthanides + actinides
    features = pd.read_csv(features_path)
    band_cols = [c for c in features.columns if c.startswith('b')]

    base = df[['symbol', 'atomic_number', 'period', 'pc1', 'pc2', 'pc3']].drop_duplicates('symbol')
    merged_feat = features.merge(base[['symbol', 'atomic_number', 'period']], on='symbol', how='inner')

    excl_mask = ((merged_feat['atomic_number'] >= 57) & (merged_feat['atomic_number'] <= 71)) | ((merged_feat['atomic_number'] >= 89) & (merged_feat['atomic_number'] <= 103))
    kept = merged_feat.loc[~excl_mask].copy()

    X_new = kept[band_cols].to_numpy(float)
    scores_new = compute_pca_scores(X_new, n_comp=3)
    pcs_new = pd.DataFrame({
        'symbol': kept['symbol'].to_numpy(),
        'pc1_new': scores_new[:, 0],
        'pc2_new': scores_new[:, 1],
        'pc3_new': scores_new[:, 2],
    })

    comp = base.merge(pcs_new, on='symbol', how='inner').merge(
        kept[['symbol', 'period', 'atomic_number']], on='symbol', how='left'
    )
    if 'period' not in comp.columns:
        if 'period_x' in comp.columns:
            comp['period'] = comp['period_x']
        elif 'period_y' in comp.columns:
            comp['period'] = comp['period_y']

    # align signs for plotting and period correlation reporting
    def align(pc_old: str, pc_new: str):
        r = stats.pearsonr(comp[pc_old], comp[pc_new])[0]
        if r < 0:
            comp[f'{pc_new}_aligned'] = -comp[pc_new]
            flipped = True
        else:
            comp[f'{pc_new}_aligned'] = comp[pc_new]
            flipped = False
        return float(r), flipped

    r1_raw, f1 = align('pc1', 'pc1_new')
    r2_raw, f2 = align('pc2', 'pc2_new')
    r3_raw, f3 = align('pc3', 'pc3_new')

    c1 = best_signed_corr(comp['pc1'].to_numpy(float), comp['pc1_new'].to_numpy(float))
    c2 = best_signed_corr(comp['pc2'].to_numpy(float), comp['pc2_new'].to_numpy(float))
    c3 = best_signed_corr(comp['pc3'].to_numpy(float), comp['pc3_new'].to_numpy(float))

    before_period_r = float(stats.pearsonr(comp['pc1'].to_numpy(float), comp['period'].to_numpy(float))[0]) if len(comp) >= 3 else np.nan
    after_period_r = float(stats.pearsonr(comp['pc1_new_aligned'].to_numpy(float), comp['period'].to_numpy(float))[0]) if len(comp) >= 3 else np.nan

    plot_scatter(
        comp['pc1'].to_numpy(float), comp['pc1_new_aligned'].to_numpy(float),
        xlabel='Baseline PC1', ylabel='New PC1 (f-block excluded, sign-aligned)',
        title='PC1 Baseline vs New (f-block excluded)', outpath=OUT3_FIG1,
    )
    plot_scatter(
        comp['pc2'].to_numpy(float), comp['pc2_new_aligned'].to_numpy(float),
        xlabel='Baseline PC2', ylabel='New PC2 (f-block excluded, sign-aligned)',
        title='PC2 Baseline vs New (f-block excluded)', outpath=OUT3_FIG2,
    )
    plot_scatter(
        comp['pc3'].to_numpy(float), comp['pc3_new_aligned'].to_numpy(float),
        xlabel='Baseline PC3', ylabel='New PC3 (f-block excluded, sign-aligned)',
        title='PC3 Baseline vs New (f-block excluded)', outpath=OUT3_FIG3,
    )

    out3 = {
        'input_merged': str(merged_path),
        'input_features': str(features_path),
        'exclusion': 'atomic_number in [57..71] U [89..103]',
        'n_baseline_rows': int(len(base)),
        'n_overlap_after_exclusion': int(len(comp)),
        'pc_correspondence': {
            'pc1': c1,
            'pc2': c2,
            'pc3': c3,
        },
        'period_correlation_pc1': {
            'before_exclusion_baseline_pc1': before_period_r,
            'after_exclusion_new_pc1_sign_aligned': after_period_r,
        },
        'sign_alignment': {
            'pc1_raw_corr': r1_raw,
            'pc1_flipped': f1,
            'pc2_raw_corr': r2_raw,
            'pc2_flipped': f2,
            'pc3_raw_corr': r3_raw,
            'pc3_flipped': f3,
        },
        'figures': [str(OUT3_FIG1), str(OUT3_FIG2), str(OUT3_FIG3)],
    }
    OUT3_JSON.write_text(json.dumps(out3, indent=2), encoding='utf-8')
    saved_paths += [str(OUT3_JSON), str(OUT3_FIG1), str(OUT3_FIG2), str(OUT3_FIG3)]

    print('Saved outputs:')
    for p in saved_paths:
        print(f'- {p}')


if __name__ == '__main__':
    main()
