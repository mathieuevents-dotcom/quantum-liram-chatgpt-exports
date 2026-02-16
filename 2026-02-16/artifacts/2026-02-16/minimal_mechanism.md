# Minimal Mechanism (2026-02-16)

Guardrail: information geometry only. No physical claims.

## Mechanism hypothesis (minimal)
1. Input inventory stage yields zero valid spectral records.
2. Schema-safe fallbacks construct deterministic default columns.
3. Feature builder emits zero-row matrix with fixed 37-layer schema.
4. Downstream PCA/K-means abstain deterministically (zero variance, empty fit status).

## Why this is falsifiable
- If any stage emits non-deterministic columns/order, LC-01 fails.
- If PCA reports non-zero variance on zero-row input, LC-02 fails.
- If K-means attempts fit without data, LC-03 fails.

## Reproducibility
- Runner: `bash scripts/run_daily_research.sh`
- Contract test: `python3 -m unittest -q tests/test_spectro_pipeline_offline.py`
- Artifacts:
  - `data/external/processed/features_37_layers.csv`
  - `reports/pca_variance_ratio.csv`
  - `reports/kmeans_37_layers_metrics.csv`
  - `reports/robustness/summary.csv`
