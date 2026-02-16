# Daily Digest - 2026-02-16

Artifacts folder: `artifacts/2026-02-16`

## Top 5 validated results
1. Offline regression test suite passed (`Ran 6 tests`, `OK`).
   - `tests/test_spectro_pipeline_offline.py`
2. Daily pipeline script exited successfully (code 0).
   - `scripts/run_daily_research.sh`
   - `artifacts/2026-02-16/2026-02-16_robustness.log`
3. 37-layer feature output is schema-stable with zero rows under empty input.
   - `data/external/processed/features_37_layers.csv`
4. PCA output is deterministically zero-variance (PC1-3 = 0.0) for empty feature matrix.
   - `reports/pca_variance_ratio.csv`
5. K-means sweep abstains deterministically with `empty_feature_matrix` status.
   - `reports/kmeans_37_layers_metrics.csv`

## Top 3 failures / uncertainties
1. Legacy parser path recorded `KeyError: 'symbol'` in one offline parser run.
   - `reports/logs/offline_parser_20260216_215535.log`
2. Correlation outputs are undefined (`NaN`) due to empty feature rows.
   - `reports/correlation_layers_vs_Z.csv`
3. Robustness summary is placeholder-only (`R0_baseline` with empty metrics).
   - `reports/robustness/summary.csv`

## Next 3 experiments
1. Add a non-empty synthetic fixture dataset and verify non-degenerate PCA/K-means outputs.
   - target: `tests/test_spectro_pipeline_offline.py`
2. Harden legacy parser inventory sort path against zero-row inventories.
   - target: `code/spectro_pipeline_offline.py`
3. Add a daily guardrail test that fails when `features_37_layers.csv` is empty unexpectedly.
   - target: `tests/`

## Synthetic Structure Validation (2026-02-16)
- Generated deterministic synthetic dataset with 300 samples, 3 latent groups, and 37 layer features:
  - `data/external/processed/synthetic_37_layers.csv`
- Existing analysis pipeline functions executed on synthetic matrix (`run_pca_analysis`, `run_kmeans_analysis`, `run_correlations_and_block_effects`).
- Validation checks passed:
  - PCA explained variance ratios: PC1 `0.640924`, PC2 `0.240521`, PC3 `0.084321`
  - K-means best silhouette: `0.575357` (best k=`3`)
  - Correlation tables non-NaN: Z `37/37`, period `37/37`, group `37/37`
- Robustness check (deterministic noise/drop perturbations, 5 repeats): mean silhouette `0.574561`.
- Report:
  - `artifacts/2026-02-16/synthetic_validation.md`

## Synthetic Null Control (2026-02-16)
- Dataset: `data/external/processed/synthetic_null_37_layers.csv` (seed=123, n=300, 37 layers, Gaussian N(0,1), no injected structure).
- Control metrics:
  - PCA variance ratios: PC1 `0.045514`, PC2 `0.044588`, PC3 `0.042451`
  - Best k: `3`
  - Best silhouette: `0.028095`
  - Non-NaN correlations (Z + group): `74`
  - Top absolute correlation (Z/group): `0.136530`
  - Robustness silhouette mean: `0.026305`
- Validation artifact:
  - `artifacts/2026-02-16/synthetic_null_validation.md`

## Sensitivity Experiment (2026-02-16)
- Extended generator with `injected_correlation_strength` and `banded-noise` mode.
- Sweep strengths: `0.05, 0.10, 0.15, 0.20, 0.30` (3 correlated bands; all other layers pure noise).
- Output table:
  - `reports/sensitivity_curve.csv`
- Output figure:
  - `reports/figures/sensitivity_curve.png`
- Summary artifact:
  - `artifacts/2026-02-16/sensitivity_validation.md`
- Operational minimal-detection criterion (`silhouette >= 0.10` and `robustness >= 0.10`) was not reached on this grid.

## Calibration (2026-02-16)
- Deterministic amplitude sweep completed on `amplitude in [0.00, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.60, 0.80, 1.00]` with per-step seed `4200 + idx`.
- Core metrics captured per amplitude: `PC1/PC2/PC3 explained variance`, `best_k + silhouette`, `non_nan_correlations_count`, `top_abs_correlation`, `robustness_silhouette_mean`.
- Null control (`amplitude=0.00`) remained below spurious-structure thresholds (`silhouette < 0.10`, `top_abs_corr < 0.30`, `pc1 < 0.15`), so no extra spurious-structure correction was required.
- Top scaling signal: `pc1` rose from `0.045188` (amp `0.00`) to `0.376351` (amp `1.00`); silhouette rose from `0.028038` to `0.233514`.
- Files:
  - `reports/calibration/sensitivity_curve.csv`
  - `reports/calibration/sensitivity_notes.md`
  - `artifacts/2026-02-16/calibration_sweep.md`
