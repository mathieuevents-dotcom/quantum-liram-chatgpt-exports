# Synthetic Null Validation

Strict falsification control. Information-geometry only.

## Dataset
- Seed: `123`
- Samples: `300`
- Layers: `37`
- Distribution: Gaussian noise N(0,1)
- Injected structure: none
- Source file: `data/external/processed/synthetic_null_37_layers.csv`

## Results
- PCA explained variance: PC1 `0.045514`, PC2 `0.044588`, PC3 `0.042451`
- Best k (silhouette sweep): `3`
- Silhouette score (best): `0.028095`
- Number of non-NaN correlations (Z + group): `74`
- Top absolute correlation value (Z/group tables): `0.136530`
- Robustness silhouette mean: `0.026305`

## Reproducible Outputs
- `artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv`
- `artifacts/2026-02-16/synthetic_null/kmeans_sweep.csv`
- `artifacts/2026-02-16/synthetic_null/correlation_vs_Z.csv`
- `artifacts/2026-02-16/synthetic_null/correlation_vs_group.csv`
- `artifacts/2026-02-16/synthetic_null/block_effect_sizes.csv`
- `artifacts/2026-02-16/synthetic_null/robustness_metrics.csv`
