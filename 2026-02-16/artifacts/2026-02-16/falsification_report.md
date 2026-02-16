# Falsification Report (2026-02-16)

Guardrail: information geometry only. No physical claims.

## Scope
- Dataset regime today: effectively empty parsed tables (`Lines files: 0`, `Levels files: 0`).
- Consequence: inferential claims on correlations/effect sizes are not validated today.

## Candidate-by-candidate status

1. LC-01 (Empty-input invariance)
- Status: not falsified.
- Check: `features_37_layers.csv` has header only (1 line total) and required columns.
- Evidence: `data/external/processed/features_37_layers.csv`

2. LC-02 (PCA degeneracy)
- Status: not falsified.
- Check: PC1-3 variance ratios are all zero.
- Evidence: `reports/pca_variance_ratio.csv`

3. LC-03 (K-means abstention)
- Status: not falsified.
- Check: all tested k rows marked `empty_feature_matrix`.
- Evidence: `reports/kmeans_37_layers_metrics.csv`

## Active falsifiers observed today
- Legacy parser path in `code/spectro_pipeline_offline.py` can still raise `KeyError: 'symbol'` on empty inventories.
- Evidence: `reports/logs/offline_parser_20260216_215535.log`
- Impact: robustness run completes by fallback path, but this is an uncertainty source and should be hardened.

## Repro commands
- `bash scripts/run_daily_research.sh`
- `python3 -m unittest -q tests/test_spectro_pipeline_offline.py`
- `sed -n '1,20p' reports/pca_variance_ratio.csv`
- `sed -n '1,20p' reports/kmeans_37_layers_metrics.csv`
