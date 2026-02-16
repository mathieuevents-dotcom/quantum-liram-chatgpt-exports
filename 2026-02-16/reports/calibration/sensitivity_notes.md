# Calibration Sensitivity Notes

Deterministic information-geometry amplitude sweep using the same analysis functions as robustness workflows.

## Reproducibility
- Command: `python3 code/calibration_sweep.py`
- Timestamp (UTC): `2026-02-16 22:28:39 UTC`

## Pipeline
1. Generate synthetic `signal_b01..signal_b37` with `mode=banded-noise`.
2. Inject amplitude into three correlated bands: `b06-b10`, `b22-b27`, `b32-b35`.
3. Run existing metrics through `run_existing_analysis(...)` (PCA/KMeans/correlations/robustness).
4. Aggregate per-amplitude metrics into `reports/calibration/sensitivity_curve.csv`.

## Parameters
- base_seed: `4200` (per amplitude seed = base_seed + index)
- n_samples: `300`
- n_layers: `37`
- groups: `3`
- bands: `[(6, 10), (22, 27), (32, 35)]`
- noise_sigma: `1.0`
- amplitudes: `[0.0, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]`

## Metrics (definitions)
- `pc1_explained_variance_ratio`, `pc2_explained_variance_ratio`, `pc3_explained_variance_ratio`: PCA variance ratios for first three components.
- `kmeans_silhouette`: maximum silhouette score over KMeans `k in [2..8]` from the shared pipeline function.
- `best_k`: argmax k for silhouette.
- `non_nan_correlations_count`: finite-count sum across Z, period, and group Pearson correlation tables.
- `top_abs_correlation`: max absolute Pearson correlation among Z/group correlation outputs.
- `robustness_silhouette_mean`: mean silhouette over deterministic perturbation repeats in `run_existing_analysis`.

## Null Control (amplitude=0.0)
- Primary null pass criteria: `kmeans_silhouette < 0.10`, `top_abs_correlation < 0.30`, `pc1_explained_variance_ratio < 0.15`.
- Spurious-structure control status: `none`.
- Falsification mode: if null control breaches criteria, activate `spurious_structure_control.csv` and compare all amplitudes to null q95 envelope.
