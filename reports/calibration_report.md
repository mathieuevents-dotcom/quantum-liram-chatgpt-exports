# Calibration Report (Reproducible Replay)

Reference state: v1.0

## Configuration Source
- config_path: calibration/calibration_config.yaml
- dataset: synthetic_37_layers.csv
- seed: 42
- sample_size: 108
- noise_level: R4_gaussian_noise (5x perturbation regime; amplitude not explicitly specified in current reports)
- number_of_layers: 37

## Baseline Metrics (from config)
- pca_explained_variance: pc1=0.5830917104, pc2=0.2785509930, pc3=0.0545355122
- clustering_k: 2
- silhouette_score: 0.8615360666
- robustness_mean_ari_pairwise: 0.6900

## Sensitivity/Null Validation (from existing artifacts)
- sensitivity_curve_path: 2026-02-16/reports/calibration/sensitivity_curve.csv
- synthetic_null_pca_path: 2026-02-16/artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv
- null_control: pc1=0.045188, silhouette=0.028038, robustness_mean=0.028302, top_abs_corr=0.164569
- criterion: silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10
- minimal_detectable_strength: 0.800000

## Reproducibility
- command: scripts/run_calibration.sh calibration/calibration_config.yaml 2026-02-16/reports/calibration/sensitivity_curve.csv 2026-02-16/artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv reports/calibration_report.md
