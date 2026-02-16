# ABL2_scaler_change

- compares StandardScaler vs RobustScaler on same feature build

```text
         config  n_bands  seed  best_k  mean_top10_anova_block  mean_top10_anova_period  periodicity_strength  silhouette_best     Z_R2  p_block  p_period  p_periodicity  p_silhouette   p_Z_R2  n_perm
scaler_standard       36    42       3                6.667255                26.987060            232.082465         0.732017 0.703871 0.004975  0.004975       0.019900      0.047619 0.004975     200
scaler_standard       37    42       3                6.677231                27.367966            235.383300         0.728436 0.693169 0.004975  0.004975       0.009950      0.047619 0.004975     200
scaler_standard       38    42       2                6.790695                22.133327            243.438867         0.746014 0.685685 0.004975  0.004975       0.014925      0.047619 0.004975     200
  scaler_robust       36    42       3                6.667255                26.987060         153401.997903         0.732017 0.703871 0.004975  0.004975       0.457711      0.047619 0.004975     200
  scaler_robust       37    42       3                6.677231                27.367966         115600.387503         0.728436 0.693169 0.004975  0.004975       0.726368      0.047619 0.004975     200
  scaler_robust       38    42       2                6.790695                22.133327          76305.240133         0.746014 0.685685 0.004975  0.004975       0.228856      0.047619 0.004975     200
```
