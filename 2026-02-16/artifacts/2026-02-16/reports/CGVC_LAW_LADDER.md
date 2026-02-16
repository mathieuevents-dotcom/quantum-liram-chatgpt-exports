# CGVC Law Ladder

- seed=42, n_perm=2000

```text
                  model  roc_auc   pr_auc  acc_best    brier  p_perm_auc
        L2_harmonic_phi 0.585735 0.443805  0.608438 0.256801      0.0005
L3_harmonic_phi_dynamic 0.585701 0.443807  0.608438 0.256851      0.0005
    L9_spectral_entropy 0.564443 0.410752  0.604483 0.481506      0.0005
      L10_spectral_rank 0.564443 0.410752  0.604483 0.458665      0.0005
     L8_spectral_lambda 0.407770 0.348786  0.604483 0.368699      1.0000
    L5_harmonic_tension 0.384190 0.314958  0.604483 0.317647      1.0000
       L1_harmonic_only 0.377098 0.311727  0.604483 0.338020      1.0000
      L4_harmonic_phase 0.376412 0.311030  0.604483 0.367437      1.0000
           L6_psy_triad 0.362008 0.317059  0.604812 0.342577      1.0000
   L7_psy_triad_dynamic 0.360301 0.316777  0.604812 0.347268      1.0000
```

## Falsification statement
- L1 (harmonic_only) is expected to be weak (already falsified in current benchmark).
- L2/L3 must beat L1 under permutation-corrected evaluation.

## What would falsify L2/L3 next?
1. L2/L3 fail to improve over L1 on independent replication datasets.
2. L2/L3 lose significance under stricter or matched-null permutation controls.
3. Gains disappear under pre-registered preprocessing perturbations.

## Spectral falsification note
- No spectral metric outperforms L2/L3 under permutation-corrected evaluation;
  harmonic structure is likely captured fully by simpler scalar kernels.
