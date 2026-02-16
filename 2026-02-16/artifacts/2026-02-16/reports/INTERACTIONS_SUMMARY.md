# INTERACTIONS SUMMARY

- Statistical scaffold only; no physical interpretation.
- Elements: 108; Pairs: 5778
- Scores: cosine, weighted cosine, dot product.
- Targets: same periodic group (AUC), period distance (Spearman).
- Null model: label permutation (1000).

## Metrics
```text
         target   metric  score     value
     same_group      AUC  S_cos  0.603968
     same_group      AUC S_wcos  0.553280
     same_group      AUC  S_dot  0.606745
period_distance Spearman  S_cos -0.442166
period_distance Spearman S_wcos -0.379515
period_distance Spearman  S_dot -0.483985
```

## Permutation p-values
```text
         target   metric  score  observed  perm_pvalue
     same_group      AUC  S_cos  0.603968     0.000999
     same_group      AUC S_wcos  0.553280     0.000999
     same_group      AUC  S_dot  0.606745     0.000999
period_distance Spearman  S_cos -0.442166     0.000999
period_distance Spearman S_wcos -0.379515     0.000999
period_distance Spearman  S_dot -0.483985     0.000999
```
