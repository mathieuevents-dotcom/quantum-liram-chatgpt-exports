# Calibration Reference Baseline v1.0

This document records the current structural metrics as **reference state v1.0**.

## Scope
- Dataset: `synthetic_37_layers.csv`
- Sample size: 108
- Layers analyzed: 37
- Seed: 42

## Current Structural Metrics
- Best KMeans `k`: 2
- Best silhouette: 0.8615360666
- PCA explained variance:
  - PC1: 0.5830917104
  - PC2: 0.2785509930
  - PC3: 0.0545355122
- Robustness regime mean (R4 Gaussian noise, 5 repeats):
  - ARI pairwise mean: 0.6900

## Baseline Values
- `mean_top10_anova_block`: 12.7889
- `mean_top10_anova_period`: 28.0869
- `periodicity_strength`: 3.51651e+44
- OOD baseline `n`: 108

## Structural Validation Snapshot
- Strongest block-discriminant layer (ANOVA F): `b26 = 21.3458`
- Strongest period-discriminant layer (ANOVA F): `b33 = 56.7664`
- Highest target-band DFT power layer: `b03 = 1.75209e+45`

## Notes
- This file is a calibration reference only.
- No theoretical interpretation is included in this baseline record.
