# Sensitivity Validation (Recomputed)

## Inputs
- sensitivity_curve: 2026-02-16/reports/calibration/sensitivity_curve.csv

## Criterion
- pass if silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10

## Outcome
- minimal_detectable_strength: 0.800000
- status: PASS

## Reproducibility
- command: awk -F',' 'NR==1{next} {if($8+0>=0.10 && $11+0>=0.10 && found==0){mds=$1; found=1}} END{if(found) print mds; else print "not_detected"}' 2026-02-16/reports/calibration/sensitivity_curve.csv
