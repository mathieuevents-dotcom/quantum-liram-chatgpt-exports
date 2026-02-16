# Discovery Log (chronological, append-only)

Rules:
- Append new entries only (no rewrites).
- Each entry includes: timestamp, agent, dataset, claim, evidence artifacts (paths), falsification status.

---

## 2026-02-16 21:57:19 +0100 — codex — daily multi-agent research run
- Scope guardrail: information geometry only; no physical claims.
- Repo health:
  - ## main...origin/main
 M docs/DAILY_DIGEST.md
 M reports/STEP0.md
 M reports/TREE_DEPTH4.md
 M reports/block_effect_sizes.csv
 M reports/block_means.csv
 M reports/correlation_layers_vs_Z.csv
 M reports/correlation_layers_vs_group.csv
 M reports/correlation_layers_vs_period.csv
 M reports/inventory.csv
 M reports/kmeans_37_layers_metrics.csv
 M reports/pca_37_layers_summary.md
 M reports/pca_variance_ratio.csv
 M reports/robustness/summary.csv
 M reports/spectro_37_layers_summary.md
?? artifacts/2026-02-16/
?? data/
?? reports/FINAL_REPORT.md.bak_20260216_213245
?? reports/FINAL_REPORT.md.bak_20260216_213915
?? reports/FINAL_REPORT.md.bak_20260216_213937
?? reports/FINAL_REPORT.md.bak_20260216_214253
?? reports/FINAL_REPORT.md.bak_20260216_214430
?? reports/FINAL_REPORT.md.bak_20260216_214533
?? reports/FINAL_REPORT.md.bak_20260216_214608
?? reports/FINAL_REPORT.md.bak_20260216_215243
?? reports/FINAL_REPORT.md.bak_20260216_215535
?? reports/RESULTS_TOPLINE.md.bak_20260216_213245
?? reports/RESULTS_TOPLINE.md.bak_20260216_213915
?? reports/RESULTS_TOPLINE.md.bak_20260216_213937
?? reports/RESULTS_TOPLINE.md.bak_20260216_214253
?? reports/RESULTS_TOPLINE.md.bak_20260216_214430
?? reports/RESULTS_TOPLINE.md.bak_20260216_214533
?? reports/RESULTS_TOPLINE.md.bak_20260216_214608
?? reports/RESULTS_TOPLINE.md.bak_20260216_215243
?? reports/RESULTS_TOPLINE.md.bak_20260216_215535
?? reports/inventory.csv.bak_20260216_213245
?? reports/inventory.csv.bak_20260216_213915
?? reports/inventory.csv.bak_20260216_213937
?? reports/inventory.csv.bak_20260216_214253
?? reports/inventory.csv.bak_20260216_214430
?? reports/inventory.csv.bak_20260216_214533
?? reports/inventory.csv.bak_20260216_214608
?? reports/inventory.csv.bak_20260216_215243
?? reports/inventory.csv.bak_20260216_215535
?? reports/logs/offline_parser_20260216_213245.log
?? reports/logs/offline_parser_20260216_213915.log
?? reports/logs/offline_parser_20260216_213937.log
?? reports/logs/offline_parser_20260216_214253.log
?? reports/logs/offline_parser_20260216_214430.log
?? reports/logs/offline_parser_20260216_214533.log
?? reports/logs/offline_parser_20260216_214608.log
?? reports/logs/offline_parser_20260216_215243.log
?? reports/logs/offline_parser_20260216_215535.log
?? reports/logs/run_20260216_213245.log
?? reports/logs/run_20260216_213915.log
?? reports/logs/run_20260216_213937.log
?? reports/logs/run_20260216_214253.log
?? reports/logs/run_20260216_214430.log
?? reports/logs/run_20260216_214533.log
?? reports/logs/run_20260216_214608.log
?? reports/logs/run_20260216_215243.log
?? reports/logs/run_20260216_215535.log executed.
  -  attempted; environment lacks  launcher and  package in offline mode.
  - Equivalent contract check executed:  (6 tests passed).
  - Lines files: 0
Levels files: 0
Parsed lines rows: 0
Parsed levels rows: 0
Coverage rows: 0
Features rows: 0
Parse errors: 0
First 3 rows of features_37_layers.csv:
Empty DataFrame
Columns: [symbol, lines_total_count, lines_intensity_sum_total, levels_total_count, lines_count_b01, lines_intensity_sum_b01, lines_intensity_mean_b01, lines_intensity_max_b01, lines_count_b02, lines_intensity_sum_b02, lines_intensity_mean_b02, lines_intensity_max_b02, lines_count_b03, lines_intensity_sum_b03, lines_intensity_mean_b03, lines_intensity_max_b03, lines_count_b04, lines_intensity_sum_b04, lines_intensity_mean_b04, lines_intensity_max_b04, lines_count_b05, lines_intensity_sum_b05, lines_intensity_mean_b05, lines_intensity_max_b05, lines_count_b06, lines_intensity_sum_b06, lines_intensity_mean_b06, lines_intensity_max_b06, lines_count_b07, lines_intensity_sum_b07, lines_intensity_mean_b07, lines_intensity_max_b07, lines_count_b08, lines_intensity_sum_b08, lines_intensity_mean_b08, lines_intensity_max_b08, lines_count_b09, lines_intensity_sum_b09, lines_intensity_mean_b09, lines_intensity_max_b09, lines_count_b10, lines_intensity_sum_b10, lines_intensity_mean_b10, lines_intensity_max_b10, lines_count_b11, lines_intensity_sum_b11, lines_intensity_mean_b11, lines_intensity_max_b11, lines_count_b12, lines_intensity_sum_b12, lines_intensity_mean_b12, lines_intensity_max_b12, lines_count_b13, lines_intensity_sum_b13, lines_intensity_mean_b13, lines_intensity_max_b13, lines_count_b14, lines_intensity_sum_b14, lines_intensity_mean_b14, lines_intensity_max_b14, lines_count_b15, lines_intensity_sum_b15, lines_intensity_mean_b15, lines_intensity_max_b15, lines_count_b16, lines_intensity_sum_b16, lines_intensity_mean_b16, lines_intensity_max_b16, lines_count_b17, lines_intensity_sum_b17, lines_intensity_mean_b17, lines_intensity_max_b17, lines_count_b18, lines_intensity_sum_b18, lines_intensity_mean_b18, lines_intensity_max_b18, lines_count_b19, lines_intensity_sum_b19, lines_intensity_mean_b19, lines_intensity_max_b19, lines_count_b20, lines_intensity_sum_b20, lines_intensity_mean_b20, lines_intensity_max_b20, lines_count_b21, lines_intensity_sum_b21, lines_intensity_mean_b21, lines_intensity_max_b21, lines_count_b22, lines_intensity_sum_b22, lines_intensity_mean_b22, lines_intensity_max_b22, lines_count_b23, lines_intensity_sum_b23, lines_intensity_mean_b23, lines_intensity_max_b23, lines_count_b24, lines_intensity_sum_b24, lines_intensity_mean_b24, lines_intensity_max_b24, ...]
Index: []
Explained variance ratios (PC1, PC2, PC3):
0.000000000000, 0.000000000000, 0.000000000000
Best k by silhouette: k=1, silhouette=nan
Top 5 layers most correlated with Z:
           layer_feature  pearson_r  abs_pearson_r
         lines_count_b01        NaN            NaN
 lines_intensity_sum_b01        NaN            NaN
lines_intensity_mean_b01        NaN            NaN
 lines_intensity_max_b01        NaN            NaN
         lines_count_b02        NaN            NaN
Top 5 layers most correlated with period:
           layer_feature  pearson_r  abs_pearson_r
         lines_count_b01        NaN            NaN
 lines_intensity_sum_b01        NaN            NaN
lines_intensity_mean_b01        NaN            NaN
 lines_intensity_max_b01        NaN            NaN
         lines_count_b02        NaN            NaN
Top 5 layers most correlated with group:
           layer_feature  pearson_r  abs_pearson_r
         lines_count_b01        NaN            NaN
 lines_intensity_sum_b01        NaN            NaN
lines_intensity_mean_b01        NaN            NaN
 lines_intensity_max_b01        NaN            NaN
         lines_count_b02        NaN            NaN
Top 5 layers by block eta^2:
           layer_feature  eta_squared
         lines_count_b01          NaN
 lines_intensity_sum_b01          NaN
lines_intensity_mean_b01          NaN
 lines_intensity_max_b01          NaN
         lines_count_b02          NaN
No feature rows available; wrote placeholder robustness summary: reports/robustness/summary.csv

Key outputs:
 - data/external/processed/features_37_layers.csv
 - data/external/processed/coverage_37_layers.csv
 - data/external/processed/pca_37_layers.csv
 - data/external/processed/kmeans_37_layers_labels.csv
 - reports/pca_variance_ratio.csv
 - reports/kmeans_37_layers_metrics.csv
 - reports/correlation_layers_vs_Z.csv
 - reports/correlation_layers_vs_period.csv
 - reports/correlation_layers_vs_group.csv
 - reports/block_effect_sizes.csv
 - reports/block_means.csv
 - reports/robustness/summary.csv
 - reports/ROBUSTNESS_37_LAYERS.md completed with exit code 0.
- Daily artifacts created:
  - 
  - 
  - 
  - 
- Key evidence files:
  - 
  - 
  - 
  - 
  - 
- Falsification status:
  - Empty-input invariance, PCA degeneracy, and K-means abstention not falsified today.
  - Cross-element correlation/effect-size laws remain unvalidated due to zero-row features.

## 2026-02-16 21:57:50 +0100 — codex — daily multi-agent research run
- Scope guardrail: information geometry only; no physical claims.
- Repo health:
  - `git status --short --branch` executed.
  - `python -m pytest -q` attempted; environment lacks `python` launcher and `pytest` package in offline mode.
  - Equivalent contract check executed: `python3 -m unittest -q tests/test_spectro_pipeline_offline.py` (6 tests passed).
  - `bash scripts/run_daily_research.sh` completed with exit code 0.
- Daily artifacts created:
  - `artifacts/2026-02-16/law_candidates.md`
  - `artifacts/2026-02-16/falsification_report.md`
  - `artifacts/2026-02-16/minimal_mechanism.md`
  - `artifacts/2026-02-16/liram_links.md`
- Key evidence files:
  - `data/external/processed/features_37_layers.csv`
  - `reports/pca_variance_ratio.csv`
  - `reports/kmeans_37_layers_metrics.csv`
  - `reports/robustness/summary.csv`
  - `reports/logs/offline_parser_20260216_215535.log`
- Falsification status:
  - Empty-input invariance, PCA degeneracy, and K-means abstention not falsified today.
  - Cross-element correlation/effect-size laws remain unvalidated due to zero-row features.

## 2026-02-16 22:24:12 +0100 — codex — synthetic validation non-degenerate structure test
- Scope guardrail: information geometry only; no physical claims.
- Generator added: `code/synthetic_generator.py`.
- Synthetic artifact created:
  - `data/external/processed/synthetic_37_layers.csv`
- Configuration:
  - seed=`42`, samples=`300`, latent groups=`3`, layers=`37`, Gaussian noise sigma=`0.35`
  - correlated injections in bands: `b06-b10`, `b22-b27`, `b32-b35`
- Existing pipeline analyses executed:
  - `reports/pca_variance_ratio.csv`
  - `reports/kmeans_37_layers_metrics.csv`
  - `reports/correlation_layers_vs_Z.csv`
  - `reports/correlation_layers_vs_period.csv`
  - `reports/correlation_layers_vs_group.csv`
- Verification outcomes:
  - PCA non-degenerate: PC1=`0.640924`, PC2=`0.240521`, PC3=`0.084321`
  - Clustering non-degenerate: best silhouette=`0.575357` at k=`3`
  - Correlation tables are non-NaN (37/37 finite in each table)
  - Robustness perturbation mean silhouette=`0.574561`
- Validation report:
  - `artifacts/2026-02-16/synthetic_validation.md`

## 2026-02-16 22:43:01 +0100 — codex — synthetic null validation spurious-structure control
- Scope guardrail: information geometry only; no theoretical interpretation.
- Deterministic null dataset generated:
  - `data/external/processed/synthetic_null_37_layers.csv`
  - seed=`123`, samples=`300`, features=`signal_b01..signal_b37`, distribution=`N(0,1)`, injected structure=`none`
- Full control analysis executed (reproducible outputs):
  - `artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv`
  - `artifacts/2026-02-16/synthetic_null/kmeans_sweep.csv`
  - `artifacts/2026-02-16/synthetic_null/correlation_vs_Z.csv`
  - `artifacts/2026-02-16/synthetic_null/correlation_vs_group.csv`
  - `artifacts/2026-02-16/synthetic_null/block_effect_sizes.csv`
  - `artifacts/2026-02-16/synthetic_null/robustness_metrics.csv`
- Extracted control metrics:
  - PCA (PC1, PC2, PC3)=`0.045514`, `0.044588`, `0.042451`
  - best_k=`3`
  - silhouette=`0.028095`
  - non_nan_correlations_Z+group=`74`
  - top_abs_correlation_Z_or_group=`0.136530`
  - robustness_silhouette_mean=`0.026305`
- Validation report:
  - `artifacts/2026-02-16/synthetic_null_validation.md`

## 2026-02-16 22:58:54 +0100 — codex — sensitivity experiment minimal detectable structure
- Scope guardrail: information geometry only; no theoretical interpretation.
- Generator update:
  - `code/synthetic_generator.py` now supports `injected_correlation_strength` and mode `banded-noise`.
- Sensitivity sweep runner:
  - `code/sensitivity_experiment.py`
- Deterministic setup:
  - seed=`42`, n=`300`, layers=`37`, strengths=`[0.05, 0.10, 0.15, 0.20, 0.30]`
  - structure model: correlated bands `b06-b10`, `b22-b27`, `b32-b35`; remaining bands pure Gaussian noise.
- Per-strength datasets written:
  - `data/external/processed/synthetic_37_layers_r0p05.csv`
  - `data/external/processed/synthetic_37_layers_r0p10.csv`
  - `data/external/processed/synthetic_37_layers_r0p15.csv`
  - `data/external/processed/synthetic_37_layers_r0p20.csv`
  - `data/external/processed/synthetic_37_layers_r0p30.csv`
- Recorded metrics file:
  - `reports/sensitivity_curve.csv`
- Figure:
  - `reports/figures/sensitivity_curve.png`
- Artifact summary:
  - `artifacts/2026-02-16/sensitivity_validation.md`
- Extracted outcomes by strength (pc1_var, best_k, silhouette, top_abs_corr, robustness_mean):
  - r=0.05 -> 0.046167, 2, 0.027945, 0.157007, 0.029161
  - r=0.10 -> 0.046264, 2, 0.028765, 0.157007, 0.028436
  - r=0.15 -> 0.046817, 2, 0.029396, 0.157007, 0.029525
  - r=0.20 -> 0.049110, 2, 0.031133, 0.157007, 0.031119
  - r=0.30 -> 0.059933, 2, 0.037789, 0.157007, 0.038689

## 2026-02-16 23:27:49 +0100 — codex — calibration amplitude sensitivity sweep
- Scope guardrail: information geometry only; no physical claims.
- Repro command:
  -             `python3 code/calibration_sweep.py`
- Artifacts:
  - `reports/calibration/sensitivity_curve.csv`
  - `reports/calibration/sensitivity_notes.md`
  - `artifacts/2026-02-16/calibration_sweep.md`

### Claim 1: null control is non-spurious at amplitude=0.00
- (a) Metric definition:
  - `kmeans_silhouette`, `top_abs_correlation`, `pc1_explained_variance_ratio`
- (b) Controls:
  - amplitude fixed at `0.00` (no injected structure)
- (c) Pass criteria:
  - `silhouette < 0.10`, `top_abs_correlation < 0.30`, `pc1 < 0.15`
- (d) Falsification mode:
  - if any threshold is breached, enable spurious-structure control () and classify rows against null q95 envelope
- (e) Result:
  - observed null metrics = `silhouette=0.028038`, `top_abs_correlation=0.164569`, `pc1=0.045188` (pass)

### Claim 2: structure metrics scale with injected amplitude on upper grid
- (a) Metric definition:
  - trend in `pc1_explained_variance_ratio`, `kmeans_silhouette`, `robustness_silhouette_mean` across amplitude grid
- (b) Controls:
  - fixed generator mode `banded-noise`, fixed `N=300`, `layers=37`, fixed bands, deterministic per-amplitude seed
- (c) Pass criteria:
  - upper amplitudes show higher values than null baseline
- (d) Falsification mode:
  - if upper amplitudes do not exceed null baseline, scaling claim fails
- (e) Result:
  - amp `0.00 -> 1.00`: `pc1 0.045188 -> 0.376351`, `silhouette 0.028038 -> 0.233514`, `robustness 0.028302 -> 0.234615` (pass)

## 2026-02-16 23:28:06 +0100 — codex — calibration log correction
- Scope guardrail: information geometry only.
- Correction to prior entry:
  - In Claim 1 falsification mode, the control filename is explicitly 
        `reports/calibration/spurious_structure_control.csv`.
- This correction is append-only and does not alter prior records.
