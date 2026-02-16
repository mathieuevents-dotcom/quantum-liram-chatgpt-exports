# Ablation C Summary

## Setup
- Labeling features: `atomic_number`, `atomic_mass`, `frequency_hz`
- Downstream classifier features: categorical symbolic fields only
- Numeric labeling features excluded from downstream classifier to avoid leakage
- Dataset SHA256: `00a17eb523e012b8a161a6af73731a3dbc26fab081ef40d7239468aba74a0df7`
- Random seed: `42`
- Permutations: `2000`

## Predictability Test
- Model: `LinearSVC`
- Evaluation: 5-fold stratified CV
- Fold accuracies: 0.166667, 0.083333, 0.083333, 0.043478, 0.086957
- Mean CV accuracy: 0.092754
- Naive baseline (most frequent class): 0.254348
- Permutation mean accuracy: 0.219748
- Permutation std: 0.051958
- Permutation p-value (acc_perm >= acc_obs): 9.965017e-01

## Interpretation
- Pass objective-signal criterion (`accuracy > naive` and permutation `p<0.01`): FAIL
