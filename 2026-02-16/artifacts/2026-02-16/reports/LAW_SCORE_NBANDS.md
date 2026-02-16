# LAW score(n_bands)

- seed: 42
- sweep range: [8, 80]
- permutations per n_bands: 200

## Shape diagnostics per metric
- `mean_top10_anova_block`: oscillating; strict local maxima count = 15
- `mean_top10_anova_period`: oscillating; strict local maxima count = 8
- `periodicity_strength`: oscillating; strict local maxima count = 16
- `silhouette_best`: oscillating; strict local maxima count = 21
- `Z_R2`: oscillating; strict local maxima count = 18

## Model comparison (AIC/BIC + 5-fold CV MSE)
- `mean_top10_anova_block` best candidate: poly3 (cv_mse=0.213263, AIC=556.577, BIC=565.738)
- `mean_top10_anova_period` best candidate: spline (cv_mse=5.48861, AIC=482.569, BIC=496.311)
- `periodicity_strength` best candidate: spline (cv_mse=8.49467e+13, AIC=2522.03, BIC=2535.78)
- `silhouette_best` best candidate: gaussian2 (cv_mse=0.00129952, AIC=579.569, BIC=595.602)
- `Z_R2` best candidate: spline (cv_mse=0.000258952, AIC=577.632, BIC=591.375)

## Classification of n_bands=37
Legend: A=strict local maximum; B=plateau; C=not statistically distinguishable from neighbors.
- `mean_top10_anova_block`: C | mean_top10_anova_block: 36=6.66726, 37=6.67723, 38=6.7907; p36=0.004975, p37=0.004975, p38=0.004975
- `mean_top10_anova_period`: A | mean_top10_anova_period: 36=26.9871, 37=27.368, 38=22.1333; p36=0.004975, p37=0.004975, p38=0.004975
- `periodicity_strength`: C | periodicity_strength: 36=1.38415e+07, 37=1.34818e+07, 38=1.63528e+07; p36=0.204, p37=0.2289, p38=0.1244
- `silhouette_best`: C | silhouette_best: 36=0.732017, 37=0.728436, 38=0.746014; p36=0.04762, p37=0.04762, p38=0.04762
- `Z_R2`: C | Z_R2: 36=0.703871, 37=0.693169, 38=0.685685; p36=0.004975, p37=0.004975, p38=0.004975

## Conclusion (statistical)
- Regime: multi-scale
- Statement limited to observed score curves and permutation-calibrated metrics.


## Re-binning invariance
- Methods: linear bins, log-spaced bins, quantile bins (frequency distribution quantiles).
- Stability metrics are computed against log baseline at fixed n_bands.

```text
          feature_corr_vs_log  top_layers_jaccard_vs_log  cluster_ari_vs_log
binning                                                                     
linear              -0.010466                   0.109229           -0.019941
log                  1.000000                   1.000000            1.000000
quantile             0.274041                   0.130092            0.037684
```
