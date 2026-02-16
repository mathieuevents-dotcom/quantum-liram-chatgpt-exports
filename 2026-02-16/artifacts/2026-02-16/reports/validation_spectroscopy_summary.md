# Spectroscopy Validation Summary

## Methods
- Data source target: NIST ASD spectral lines (best-effort fetch per element).
- Features: centroid_frequency_hz, log_centroid, spectral_entropy, 10 band powers, line_count_total.
- Test 1: Kruskal-Wallis per feature across Fire/Water/Air/Earth with BH-FDR correction.
- Test 2: 5-fold CV multinomial logistic regression (standardized features), metrics accuracy and macro-F1.
- Test 3: 2000 label permutations for empirical p-values of CV accuracy and macro-F1.

## Key Results
- Elements with >=1 fetched spectral line: 0/118
- Data sufficiency gate (>=20 elements): FAIL
- CV accuracy mean: 0.254348
- CV macro-F1 mean: 0.101379
- Naive baseline accuracy: 0.254237
- Naive baseline macro-F1: 0.101351
- Permutation p-value (accuracy): 4.997501e-04
- Permutation p-value (macro-F1): 4.997501e-04
- Significant features after FDR (q<0.05): 0
- Spearman(quantum_hz, centroid_frequency_hz): rho=nan, p=nan, perm_p=nan
- Spearman(quantum_hz, log_centroid): rho=nan, p=nan, perm_p=nan

## Frequency Proxy Update Rule
- Proposed rule: Keep existing `frequency_hz` and add new spectral columns: `spectral_centroid_hz`, `spectral_entropy`, and `band_power_01..10`.

## Pass/Fail
- Criterion: pass data sufficiency gate AND outperform naive baseline with permutation significance, or have FDR-significant group features.
- Result: FAIL

## Decision
- Spectroscopy supports non-random alignment with current 4 elements: NO.
- Minimal pre-registered next change: derive classes from quantiles of `log_centroid` + `spectral_entropy` only, then rerun the same three tests without symbolic columns in label construction.
