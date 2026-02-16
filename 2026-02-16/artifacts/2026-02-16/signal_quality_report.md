# Signal Quality Report

- Date: `2026-02-16`
- Input: `data/external/processed/features_37_layers.csv`
- Shape: `0` rows x `226` columns

## Requested Metrics
- Column-wise variance: computed (numeric columns only).
- Percent NaN per column: computed for all columns.
- Number of unique values per column: computed (including and excluding NaN).

## Columns with Zero Variance
- Count: `0`
- None (for this snapshot).

## Columns with >50% NaN
- Count: `226` / `226`
- All columns exceed 50% NaN (empty dataset => 100% NaN by diagnostic definition).

## Columns Effectively Constant
- Definition: `n_unique_non_null <= 1` OR dominant non-null value frequency `>= 99%`.
- Count: `226` / `226`
- All columns are effectively constant in this snapshot (no observed rows).

## Concrete Feature-Engineering Improvements
1. Add non-empty bootstrap fixtures to force minimum signal: create a synthetic `lines/levels` fixture with at least 30 symbols and realistic frequency/intensity ranges; fail pipeline if output rows < 30.
2. Replace raw per-band sums with robust normalized features: add per-symbol z-scored band intensities, log1p-transformed counts, and within-symbol quantile features (`q25`, `q50`, `q75`) to reduce constant/degenerate columns.
3. Add automatic feature-pruning gate before modeling: drop columns with `nan_percent > 40`, `n_unique_non_null <= 1`, or variance below epsilon (e.g. `1e-10`), and persist a retained-feature manifest for reproducibility.

## Repro Command
```bash
python3 - <<'PY'
import pandas as pd
df=pd.read_csv('data/external/processed/features_37_layers.csv')
print(df.shape)
print(df.var(numeric_only=True).head())
print((df.isna().mean()*100).head())
print(df.nunique(dropna=False).head())
PY
```
