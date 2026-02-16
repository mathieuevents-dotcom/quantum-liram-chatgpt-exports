# Compare Summary

## Settings
- Seed: `42`
- Permutations: `2000`

## Mode: physchem
- Frequency Spearman rho: 0.127074 (p=1.702986e-01)
- Robust regression (Theil-Sen): slope=3.300783, intercept=11739.148826
- Permutation p-value (|rho_perm| >= |rho_obs|): 1.794103e-01
- 4-class agreement: ARI=0.000000, NMI=0.000000

## Mode: spectroscopy
- Frequency Spearman rho: nan (p=nan)
- Robust regression (Theil-Sen): slope=nan, intercept=nan
- Permutation p-value (|rho_perm| >= |rho_obs|): nan
- 4-class agreement: ARI=0.000000, NMI=0.000000

## Mode: all
- Frequency Spearman rho: 0.127074 (p=1.702986e-01)
- Robust regression (Theil-Sen): slope=3.300783, intercept=11739.148826
- Permutation p-value (|rho_perm| >= |rho_obs|): 1.794103e-01
- 4-class agreement: ARI=0.000000, NMI=0.000000

## Stability Across Domain Ablations
- Spearman rho values: physchem=0.127074, spectroscopy=nan, all=0.127074
- Std across modes: 0.000000
- Interpretation: lower std means more stable agreement across domain-specific candidate constructions.
