# Dynamic Stress Test

- seed=42, n_perm=2000
- protocols: baseline, shuffle_temporal_order, phase_randomized_surrogate

## Metrics
```text
                  protocol                   model  roc_auc   pr_auc    brier  p_perm_auc
                  baseline         L2_harmonic_phi 0.585735 0.443805 0.256801    0.000500
                  baseline L3_harmonic_phi_dynamic 0.585701 0.443807 0.256851    0.000500
    shuffle_temporal_order         L2_harmonic_phi 0.585735 0.443805 0.256801    0.000500
    shuffle_temporal_order L3_harmonic_phi_dynamic 0.585701 0.443803 0.256854    0.000500
phase_randomized_surrogate         L2_harmonic_phi 0.479322 0.372007 0.248898    0.978511
phase_randomized_surrogate L3_harmonic_phi_dynamic 0.479324 0.372007 0.248888    0.978011
```

## Delta (L3 - L2)
```text
                  protocol  delta_roc_auc_L3_minus_L2  delta_pr_auc_L3_minus_L2  delta_brier_L3_minus_L2
                  baseline                  -0.000035              1.673139e-06                 0.000050
    shuffle_temporal_order                  -0.000035             -1.947638e-06                 0.000054
phase_randomized_surrogate                   0.000003              9.634220e-09                -0.000010
```

## Falsification clause
- L3 does not significantly outperform L2 under any stress protocol; dynamic contribution is not empirically supported.
