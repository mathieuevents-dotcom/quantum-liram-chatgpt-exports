# CGVC Compound Benchmark

- n_pairs: 3034
- positives: 1200
- negatives: 1834
- permutation_n: 2000

## Metrics
```text
        score  roc_auc   pr_auc  acc_best  thr_best    brier    n
            V 0.505100 0.390134  0.607449 33.315325 0.337479 3034
ch_minus_plus 0.500000 0.395517  0.604483       inf 0.250000 3034
ch_plus_minus 0.500000 0.395517  0.604483       inf 0.250000 3034
          S_V 0.494900 0.365572  0.604483       inf 0.472268 3034
 ch_zero_zero 0.429666 0.340321  0.604483 46.943147 0.316324 3034
```

## Permutation test
```text
score  observed_auc  null_mean_auc  null_std_auc  p_empirical  n_perm
  S_V        0.4949       0.500044       0.01066     0.683658    2000
    V        0.5051       0.499956       0.01066     0.316842    2000
```

## Comparison vs existing compound benchmark
- baseline_best: S_dot (ROC_AUC=0.411018)
- cgvc_best: V (ROC_AUC=0.505100)
- delta_ROC_AUC: 0.094082
- summary: helps_or_matches
