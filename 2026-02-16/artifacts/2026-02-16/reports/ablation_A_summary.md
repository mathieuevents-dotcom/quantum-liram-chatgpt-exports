# Ablation A Summary

## Setup
- Labeling features: `atomic_number`, `atomic_mass`
- Excluded from labeling: `frequency_hz`, categorical symbolic fields
- Downstream test variable: `frequency_hz`
- Dataset SHA256: `00a17eb523e012b8a161a6af73731a3dbc26fab081ef40d7239468aba74a0df7`
- Random seed: `42`
- Permutations: `2000`

## Kruskal-Wallis (frequency_hz across classes)
- H statistic: 109.689076
- p-value: 1.280113e-23
- Epsilon-squared: 0.935869
- Permutation p-value (H_perm >= H_obs): 4.997501e-04

## Interpretation
- Pass objective-signal criterion (`p<0.01` and permutation `p<0.01`): PASS
