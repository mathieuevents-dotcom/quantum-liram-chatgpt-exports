# Law Candidates (2026-02-16)

Guardrail: information geometry only. No physical claims.

## LC-01: Empty-input invariance for 37-layer feature schema
- Claim: If no valid lines/levels records are available, the pipeline still emits a deterministic 37-layer feature table with a stable header and zero rows.
- Metric definition: row count in `data/external/processed/features_37_layers.csv`; schema presence of required columns (`symbol`, `lines_total_count`, `levels_total_count`).
- Controls: random control = rerun with same empty inputs; shuffle/block-preserving controls are not applicable to zero-sample input and are marked N/A.
- Pass criteria: row count is exactly `0` and required columns are present.
- Falsification mode: any run where row count > 0 for empty input, or missing required columns.
- Evidence artifacts:
  - `data/external/processed/features_37_layers.csv`
  - `artifacts/2026-02-16/2026-02-16_robustness.log`
- Reproduce:
  - `bash scripts/run_daily_research.sh`
  - `wc -l data/external/processed/features_37_layers.csv`

## LC-02: PCA degeneracy under empty feature matrix
- Claim: When feature rows are empty, explained variance ratios for PC1-3 are deterministically `0.0`.
- Metric definition: values in `reports/pca_variance_ratio.csv` (`explained_variance_ratio`).
- Controls: shuffle = N/A, block-preserving = N/A, random = rerun with same empty input and fixed seed.
- Pass criteria: PC1, PC2, PC3 each equal `0.0`.
- Falsification mode: any non-zero value in PC1/PC2/PC3 for empty-input run.
- Evidence artifacts:
  - `reports/pca_variance_ratio.csv`
- Reproduce:
  - `bash scripts/run_daily_research.sh`
  - `sed -n '1,10p' reports/pca_variance_ratio.csv`

## LC-03: K-means abstention under empty feature matrix
- Claim: K sweep reports `empty_feature_matrix` status for each evaluated k and does not emit invalid silhouette values.
- Metric definition: `status` column in `reports/kmeans_37_layers_metrics.csv`.
- Controls: shuffle = N/A, block-preserving = N/A, random = rerun with identical inputs.
- Pass criteria: every row has `status=empty_feature_matrix` for k in configured sweep.
- Falsification mode: any k with non-empty status implying a fit on empty matrix.
- Evidence artifacts:
  - `reports/kmeans_37_layers_metrics.csv`
- Reproduce:
  - `bash scripts/run_daily_research.sh`
  - `sed -n '1,20p' reports/kmeans_37_layers_metrics.csv`
