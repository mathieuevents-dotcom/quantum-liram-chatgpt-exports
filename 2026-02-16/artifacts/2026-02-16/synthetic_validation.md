# Synthetic Validation - Non-Degenerate Structure Test

Strictly information-geometry validation. No theoretical or physical claims.

## Setup
- Seed: `42`
- Latent groups: `3`
- Layers: `37`
- Samples: `300`
- Correlated band injections: `b06-b10`, `b22-b27`, `b32-b35`
- Gaussian noise: `sigma=0.35`
- Dataset: `data/external/processed/synthetic_37_layers.csv`

## Verification
- PCA explained variance (PC1, PC2, PC3): `0.640924`, `0.240521`, `0.084321`
- K-means best k: `3`
- K-means best silhouette: `0.575357`
- Non-NaN correlations vs Z: `37`
- Non-NaN correlations vs period: `37`
- Non-NaN correlations vs group: `37`
- Robustness mean silhouette (5 perturbation repeats): `0.574561`

## Files Produced
- `data/external/processed/synthetic_37_layers.csv`
- `reports/pca_variance_ratio.csv`
- `reports/kmeans_37_layers_metrics.csv`
- `reports/correlation_layers_vs_Z.csv`
- `reports/correlation_layers_vs_period.csv`
- `reports/correlation_layers_vs_group.csv`
- `artifacts/2026-02-16/synthetic_validation.md` (this report)
