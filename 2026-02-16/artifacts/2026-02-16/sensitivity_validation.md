# Sensitivity Validation

Strictly information-geometry sensitivity experiment.

## Setup
- Generator mode: `banded-noise`
- Correlated bands: `b06-b10`, `b22-b27`, `b32-b35`
- Non-band layers: pure Gaussian noise
- Seed: `42`
- Samples per run: `300`
- Strength grid: `[0.05, 0.1, 0.15, 0.2, 0.3]`

## Outputs
- Curve table: `reports/sensitivity_curve.csv`
- Figure: `reports/figures/sensitivity_curve.png`

## Recorded Metrics per Strength
- `pc1_variance`
- `best_k`
- `silhouette`
- `top_abs_correlation`
- `robustness_silhouette_mean`

## Minimal Detectable Strength (Operational Criterion)
- Criterion: silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10
- Minimal detected strength: `nan`
