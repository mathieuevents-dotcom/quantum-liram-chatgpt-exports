# Analysis Summary

## Settings
- Input: `data/extracted/elements_labeled.csv`
- Random seed: `42`
- Permutations: `2000`

## A) Kruskal-Wallis (frequency_hz ~ class)
- H statistic: 0.205099
- p-value: 9.767620e-01
- epsilon-squared: 0.000000

## B) Chi-square Tests (field vs class)
- `vibratory_form`: chi2=354.000000, dof=21, p=2.851671e-62, Cramer's V=1.000000
- `vibratory_polarity`: chi2=354.000000, dof=21, p=2.851671e-62, Cramer's V=1.000000
- `symbolic_function`: chi2=354.000000, dof=21, p=2.851671e-62, Cramer's V=1.000000
- `vibratory_color`: chi2=354.000000, dof=21, p=2.851671e-62, Cramer's V=1.000000

## C) Predictability (5-fold Stratified CV)
- Model: LogisticRegression on frequency + one-hot categorical fields
- Fold accuracies: 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
- Mean CV accuracy: 1.000000
- Naive baseline accuracy (most-frequent class): 0.254348

## 4) Permutation Baseline
- Observed accuracy: 1.000000
- Permutation mean: 0.236309
- Permutation std: 0.052782
- Empirical p-value (perm >= observed): 4.997501e-04

## 6) Strong Evidence Check
- Criterion: Kruskal p<0.01 AND all chi-square p<0.01 AND permutation p<0.01
- Result: FAIL
