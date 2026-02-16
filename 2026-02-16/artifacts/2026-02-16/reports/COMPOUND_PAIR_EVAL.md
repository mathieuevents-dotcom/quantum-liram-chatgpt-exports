# Compound Pair Evaluation

- n_pairs: 3034
- seed: 42
- metrics: ROC AUC, PR AUC, accuracy@best-threshold, Brier

## Overall + stratified results
```text
      stratum  score  roc_auc   pr_auc  acc_best   thr_best    brier    n
          all  S_cos 0.370533 0.308743  0.604483        inf 0.328928 3034
          all S_wcos 0.377816 0.311076  0.604483        inf 0.354439 3034
          all  S_dot 0.411018 0.327625  0.604483 165.555659 0.308536 3034
 same_group=0  S_cos 0.374506 0.333399  0.578652        inf 0.326909 2848
 same_group=0 S_wcos 0.380443 0.335414  0.578652        inf 0.351431 2848
 same_group=0  S_dot 0.415033 0.353071  0.578652  87.959124 0.327025 2848
 same_group=1  S_cos      NaN      NaN       NaN        NaN      NaN  186
 same_group=1 S_wcos      NaN      NaN       NaN        NaN      NaN  186
 same_group=1  S_dot      NaN      NaN       NaN        NaN      NaN  186
same_period=0  S_cos 0.373246 0.312134  0.601876        inf 0.322139 2665
same_period=0 S_wcos 0.385494 0.316659  0.601876        inf 0.346698 2665
same_period=0  S_dot 0.418970 0.329571  0.601876        inf 0.311911 2665
same_period=1  S_cos 0.317485 0.276900  0.623306        inf 0.379376  369
same_period=1 S_wcos 0.293807 0.270958  0.623306        inf 0.405284  369
same_period=1  S_dot 0.381389 0.328919  0.626016  87.959124 0.314943  369
```

## Permutation test (AUC)
```text
 score  observed_auc  null_mean_auc  null_std_auc  p_empirical  n_perm
S_wcos      0.377816       0.499721      0.010573          1.0    2000
 S_cos      0.370533       0.499971      0.011068          1.0    2000
```
