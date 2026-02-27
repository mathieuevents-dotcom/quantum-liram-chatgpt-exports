#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd

FEATURES = Path('2026-02-16/artifacts/2026-02-16/reports/bandcount/K_37/features.csv')
MAP_CANDIDATES = [
    Path('2026-02-16/artifacts/2026-02-16/reports/qliram_signatures_37D.csv'),
    Path('2026-02-16/artifacts/2026-02-16/reports/qliram_periodic_table.csv'),
]
OUT = Path('reports/elements_pcs_atomicprops.csv')


def main():
    if not FEATURES.exists():
        raise FileNotFoundError(f'Missing features file: {FEATURES}')

    fmap = None
    for c in MAP_CANDIDATES:
        if c.exists():
            fmap = c
            break
    if fmap is None:
        raise FileNotFoundError('No mapping file found for symbol->atomic metadata')

    f = pd.read_csv(FEATURES)
    band_cols = [c for c in f.columns if c.startswith('b')]
    X = f[band_cols].to_numpy(dtype=float)

    mu = X.mean(axis=0)
    sd = X.std(axis=0, ddof=0)
    sd_safe = np.where(sd > 0, sd, 1.0)
    Xz = (X - mu) / sd_safe

    C = np.corrcoef(Xz, rowvar=False)
    vals, vecs = np.linalg.eigh(C)
    idx = np.argsort(vals)[::-1]
    vecs = vecs[:, idx]
    scores = Xz @ vecs[:, :3]

    meta = pd.read_csv(fmap)
    z_col = 'Z' if 'Z' in meta.columns else 'atomic_number'
    keep = ['symbol']
    if z_col in meta.columns:
        keep.append(z_col)
    if 'period' in meta.columns:
        keep.append('period')
    if 'group' in meta.columns:
        keep.append('group')
    meta = meta[keep].drop_duplicates('symbol')

    out = pd.DataFrame({
        'symbol': f['symbol'],
        'pc1': scores[:, 0],
        'pc2': scores[:, 1],
        'pc3': scores[:, 2],
    }).merge(meta, on='symbol', how='left')

    if z_col in out.columns:
        out = out.rename(columns={z_col: 'atomic_number'})

    OUT.parent.mkdir(parents=True, exist_ok=True)
    out[['symbol', 'atomic_number', 'pc1', 'pc2', 'pc3']].to_csv(OUT, index=False)

    print(f'Wrote: {OUT}')
    # Print requested diagnostic correlations.
    if 'period' in out.columns:
        print(f"Pearson corr(pc1, period): {out['pc1'].corr(out['period'], method='pearson')}")
    if 'group' in out.columns:
        print(f"Pearson corr(pc2, group): {out['pc2'].corr(out['group'], method='pearson')}")
    if 'atomic_number' in out.columns:
        print(f"Pearson corr(pc1, atomic_number): {out['pc1'].corr(out['atomic_number'], method='pearson')}")


if __name__ == '__main__':
    main()
