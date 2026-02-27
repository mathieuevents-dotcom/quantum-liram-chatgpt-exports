# Daily Digest

## Top 5 Validated Results
1. Calibration replay report generated from config and existing artifacts: `reports/calibration_report.md`
2. Null-control metrics extracted from sensitivity curve (amplitude=0): `2026-02-16/reports/calibration/sensitivity_curve.csv`
3. Sensitivity criterion passed with minimal detectable strength 0.800000: `reports/sensitivity_validation.md`
4. Sensitivity outcome artifact written with reproducible commands: `artifacts/2026-02-17/sensitivity_result.md`
5. Synthetic-null PCA reference path validated as present: `2026-02-16/artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv`

## Top 3 Failures / Uncertainties
1. Referenced calibration runner missing: `code/calibration_sweep.py`
2. Historical sensitivity note reported `nan` threshold (now superseded by recompute): `2026-02-16/artifacts/2026-02-16/sensitivity_validation.md`
3. `agents/00_SYSTEM_RULES.md` not found in this repo snapshot

## Next 3 Experiments (Tomorrow)
1. Restore/locate original `code/calibration_sweep.py` and rerun native calibration pipeline
2. Add deterministic wrapper to regenerate `2026-02-16/reports/calibration/sensitivity_curve.csv` from source code
3. Cross-check calibration replay values against `2026-02-16/artifacts/2026-02-16/calibration_sweep.md`
