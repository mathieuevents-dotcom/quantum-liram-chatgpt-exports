# Spectral Model Selection

- seed=42, n_perm=1000
- data: eigenvalue spectrum from padded K=1..60 layer matrix
- fitted models: power-law spectrum, exponential cumulative saturation, hard-cutoff k=37

## Model comparison (AIC/BIC)
```text
                    model      sse         aic         bic            a     alpha    tau       c1  c2  k_break
exp_saturation_cumulative 0.001892 -619.883278 -617.788933          NaN       NaN 4.1402      NaN NaN      NaN
       power_law_spectrum 1.558431 -215.039891 -210.851202 4.160112e+09 11.393594    NaN      NaN NaN      NaN
          hard_cutoff_k37 7.025613 -124.686924 -120.498235          NaN       NaN    NaN 1.009346 0.0     37.0
```

## Permutation test for model preference
- observed delta AIC (2nd-best - best): 404.843387
- null mean delta AIC: 42.632335
- p-value preference: 0.000999

## K≈37 checks
- cumulative variance saturation near 37: not supported (score=nan)
- spectral gap near 37: not supported (gap37=0.000000, prominence=-0.000000)

- information geometry only; no physical claim.
