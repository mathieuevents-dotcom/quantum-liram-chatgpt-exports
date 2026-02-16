# Layer Bound Test

- seed=42, n_perm=2000
- model: L2_harmonic_phi only
- tested K: 15, 21, 30, 37, 45(zero/noise), 60(zero/noise)

## Metrics table
```text
 K      mode  roc_auc  p_perm_auc  perm_auc_std  perm_auc_mean  mean_spectral_entropy
15 truncated 0.507756    0.226887      0.010639       0.499926               0.554491
21 truncated 0.495493    0.654673      0.010494       0.499820               0.613235
30 truncated 0.613349    0.000500      0.010801       0.499687               0.613109
37 reference 0.585735    0.000500      0.010772       0.499697               0.620058
45     noise 0.575499    0.000500      0.010767       0.499723               0.660296
45      zero 0.585735    0.000500      0.010772       0.499697               0.620058
60     noise 0.556812    0.000500      0.010620       0.499665               0.676152
60      zero 0.585735    0.000500      0.010772       0.499697               0.620058
```

## Structural necessity checks
- Peak near K=37: NO (reference ROC_AUC=0.585735, max=0.613349)
- K=21 local optimum (within truncated set 15/21/30): NO

## Decision rule note
- Judgement uses ROC AUC ranking + permutation stability + spectral-entropy context.
