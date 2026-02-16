# ROBUSTNESS 37 LAYERS

## Dataset coverage
- Raw lines HTML files: 97
- Raw levels HTML files: 105
- Elements in `coverage_37_layers.csv`: 108
- Elements with parsed lines: 97
- Elements with parsed levels: 105
- Elements with both lines and levels: 94

## Baseline results (R0)
- Best KMeans k: 2
- Best silhouette: 0.8615360666
- PCA explained variance ratios:
  - PC1: 0.5830917104
  - PC2: 0.2785509930
  - PC3: 0.0545355122
- Top correlations vs Z (absolute Pearson):
  1. `levels_count_b21` (|r|=0.4936)
  2. `levels_energy_sum_b21` (|r|=0.4924)
  3. `lines_count_b21` (|r|=0.3835)
  4. `levels_count_b22` (|r|=0.3327)
  5. `levels_energy_sum_b22` (|r|=0.3242)

## Stability summary
Source: `reports/robustness/summary.csv`

| Regime | best_k | best_silhouette | PC1 | PC2 | PC3 | ARI mean | Procrustes vs R0 | Spearman corr-rank vs R0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| R0_baseline | 2 | 0.8615 | 0.5831 | 0.2786 | 0.0545 | NA | 0.0000 | 1.0000 |
| R1_standardized | 2 | 0.8445 | 0.2654 | 0.2157 | 0.1103 | NA | 1.8078 | 0.9996 |
| R2_band_only | 2 | 0.8615 | 0.5831 | 0.2786 | 0.0545 | NA | ~0 | 1.0000 |
| R3_drop10pct_rows (5x) | 2 | 0.7312 | 0.5659 | 0.2617 | 0.0732 | 0.3462 | 0.0112 | 0.9341 |
| R4_gaussian_noise (5x) | 2 | 0.8178 | 0.5832 | 0.2784 | 0.0546 | 0.6900 | 0.0001 | 0.9947 |

## Interpretation notes (factual)
- Stable points across regimes:
  - Best k remains 2 in all tested regimes.
  - PCA structure is highly stable for `R2_band_only` and `R4_gaussian_noise` (very low Procrustes disparity vs R0).
  - Rank order of layer correlations vs Z remains high vs baseline (Spearman ~0.99 for R1/R4, ~0.93 for R3).
- Sensitive points:
  - Row-drop perturbation (`R3`) lowers silhouette and ARI consistency the most.
  - Standardization (`R1`) changes PCA variance distribution strongly (PC1 reduced), while clustering quality remains close to baseline.
- Most consistent layer associations observed:
  - Z and period: strong recurring signal around layer 21, then 22.
  - Group: strongest association also centered on layer 21 (and nearby layer 20/22).
  - Block effects (eta²): strongest on `levels_energy_sum_b21`, `levels_count_b21`, then layers 20/23.
