# Spectral Law

- seed=42, n_perm=2000
- pair coupling matrix: `C = 0.5*(psi_A psi_B^T + psi_B psi_A^T)`

## Added spectral scores
- `L8_spectral_lambda`: largest eigenvalue of C
- `L9_spectral_entropy`: entropy of normalized absolute eigenspectrum
- `L10_spectral_rank`: effective rank = exp(entropy)

```text
              model  roc_auc   pr_auc  acc_best    brier  p_perm_auc
L9_spectral_entropy 0.564443 0.410752  0.604483 0.481506      0.0005
  L10_spectral_rank 0.564443 0.410752  0.604483 0.458665      0.0005
 L8_spectral_lambda 0.407770 0.348786  0.604483 0.368699      1.0000
```

## Falsification note
- If no spectral metric outperforms L2/L3 under permutation-corrected evaluation,
  harmonic structure is likely captured fully by simpler scalar kernels.
