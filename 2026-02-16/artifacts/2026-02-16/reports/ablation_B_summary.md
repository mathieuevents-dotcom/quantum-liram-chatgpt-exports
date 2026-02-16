# Ablation B Summary

## Setup
- Labeling feature: `frequency_hz` only (quantile-based 4 bins)
- Downstream tests: categorical symbolic fields only (`vibratory_form`, `vibratory_polarity`, `symbolic_function`, `vibratory_color`)
- `frequency_hz` excluded from downstream tests to avoid leakage
- Dataset SHA256: `00a17eb523e012b8a161a6af73731a3dbc26fab081ef40d7239468aba74a0df7`
- Random seed: `42`

## Chi-square Over-representation Tests
- `vibratory_form`: chi2=1.742551, dof=21, p=1.000000e+00, Cramer's V=0.070160
- `vibratory_polarity`: chi2=1.742551, dof=21, p=1.000000e+00, Cramer's V=0.070160
- `symbolic_function`: chi2=1.742551, dof=21, p=1.000000e+00, Cramer's V=0.070160
- `vibratory_color`: chi2=1.742551, dof=21, p=1.000000e+00, Cramer's V=0.070160

## Standardized Residuals
- Residual tables written to:
- `reports/ablation_B_residuals_vibratory_form.csv`
- `reports/ablation_B_residuals_vibratory_polarity.csv`
- `reports/ablation_B_residuals_symbolic_function.csv`
- `reports/ablation_B_residuals_vibratory_color.csv`

## Interpretation
- Pass objective-signal criterion (all chi-square `p<0.01`): FAIL
