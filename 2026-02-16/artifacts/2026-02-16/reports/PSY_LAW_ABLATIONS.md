# PSY Law Ablations

- seed=42, n_perm=2000

```text
        ablation  roc_auc   pr_auc  acc_best    brier  p_perm_auc  n_pairs
     baseline_L7 0.360301 0.316777  0.604812 0.347268         1.0     3034
 remove_phi_plus 0.371421 0.314636  0.604483 0.352346         1.0     3034
remove_phi_minus 0.425909 0.341782  0.604812 0.356246         1.0     3034
 remove_phi_zero 0.369111 0.319667  0.604812 0.355565         1.0     3034
   disable_psi_t 0.362008 0.317059  0.604812 0.342577         1.0     3034
```

Interpretation is strictly statistical (benchmark behavior only).
