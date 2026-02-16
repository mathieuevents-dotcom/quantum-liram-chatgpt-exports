# LiRam Links (2026-02-16)

Guardrail: information geometry only. No physical claims.

## Validated
1. Empty-input geometric state -> deterministic 37-layer schema output.
- Evidence: `data/external/processed/features_37_layers.csv`
- Repro: `bash scripts/run_daily_research.sh`

2. Empty-input geometric state -> PCA zero-variance output.
- Evidence: `reports/pca_variance_ratio.csv`
- Repro: `sed -n '1,10p' reports/pca_variance_ratio.csv`

3. Empty-input geometric state -> K sweep abstention (`empty_feature_matrix`).
- Evidence: `reports/kmeans_37_layers_metrics.csv`
- Repro: `sed -n '1,20p' reports/kmeans_37_layers_metrics.csv`

## Speculative
1. Any cross-element correlation law from this run.
- Reason: correlation tables are undefined/NaN under zero-row features.
- Evidence: `reports/correlation_layers_vs_Z.csv`

2. Any block effect-size law from this run.
- Reason: effect sizes are undefined with no populated features.
- Evidence: `reports/block_effect_sizes.csv`

3. Robust universality claim across datasets.
- Reason: current run lacks non-empty parsed rows.
- Evidence: `reports/robustness/summary.csv`
