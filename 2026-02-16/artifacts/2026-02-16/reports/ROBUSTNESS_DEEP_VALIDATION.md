# Robustness Deep Validation

## A) Permutation test
- Permutations: 100
- Metrics evaluated per layer: block ANOVA F, period ANOVA F, periodicity strength.

### Strongest deviations from permutation baseline
- b07: p_period=0, z_period=8.99792, p_block=0.43, p_periodicity=0
- b16: p_period=0, z_period=6.87792, p_block=0.02, p_periodicity=0
- b18: p_period=0, z_period=6.88734, p_block=0.02, p_periodicity=0
- b17: p_period=0, z_period=8.64343, p_block=0.07, p_periodicity=0
- b26: p_period=0, z_period=58.659, p_block=0, p_periodicity=0
- b19: p_period=0, z_period=12.4857, p_block=0.89, p_periodicity=0
- b35: p_period=0, z_period=92.4987, p_block=0, p_periodicity=0
- b33: p_period=0, z_period=92.6757, p_block=0, p_periodicity=0
- b36: p_period=0, z_period=14.125, p_block=0.04, p_periodicity=0.01
- b34: p_period=0, z_period=46.6688, p_block=0, p_periodicity=0.01

## B) Z-independent structure (top-5 Z-correlated layers removed)
- Removed layers: b33, b35, b25, b26, b34

### Top remaining block-discriminant layers
- b23: anova_f_block=16.3334, anova_f_period=27.0734, periodicity=1.47959e+33
- b29: anova_f_block=15.3628, anova_f_period=15.9442, periodicity=3.67188e+32
- b28: anova_f_block=14.4596, anova_f_period=16.9501, periodicity=2.83875e+32
- b32: anova_f_block=11.4959, anova_f_period=8.91662, periodicity=5.33526e+33
- b31: anova_f_block=11.0951, anova_f_period=10.3416, periodicity=1.4413e+33
- b30: anova_f_block=9.96777, anova_f_period=11.9223, periodicity=7.8369e+32
- b21: anova_f_block=7.90674, anova_f_period=10.3792, periodicity=1.93042e+34
- b27: anova_f_block=7.90674, anova_f_period=10.3792, periodicity=2.14788e+13
- b22: anova_f_block=7.66624, anova_f_period=10.6188, periodicity=1.998e+34
- b24: anova_f_block=6.61452, anova_f_period=8.83267, periodicity=1.38138e+33

## C) Physical band mapping for discriminant layers
- b26 (levels): [4.582927e+11, 4.900228e+16] Hz, mean_energy=8.39674 eV, n=29998
- b23 (levels): [4.582927e+11, 4.900228e+16] Hz, mean_energy=8.39674 eV, n=29998
- b29 (levels): [9.812516e+14, 9.812516e+14] Hz, mean_energy=4.05761 eV, n=1499
- b28 (levels): [6.873969e+14, 6.873969e+14] Hz, mean_energy=2.86365 eV, n=1499
- b32 (levels): [3.786425e+15, 3.786425e+15] Hz, mean_energy=15.4998 eV, n=1499
- b31 (levels): [2.298053e+15, 2.298053e+15] Hz, mean_energy=9.53392 eV, n=1499
- b30 (levels): [1.449729e+15, 1.449729e+15] Hz, mean_energy=6.00597 eV, n=1499
- b33 (levels): [4.582927e+11, 9.812516e+14] Hz, mean_energy=2.88613 eV, n=7500
- b35 (levels): [2.298053e+15, 4.900228e+16] Hz, mean_energy=18.2553 eV, n=7500
- b25 (levels): [4.582927e+11, 4.900228e+16] Hz, mean_energy=8.39674 eV, n=29998
- b34 (levels): [9.812516e+14, 2.298053e+15] Hz, mean_energy=6.22247 eV, n=14998
- b20 (levels): [4.582927e+11, 4.900228e+16] Hz, mean_energy=8.39674 eV, n=29998

## Statistical interpretation
- Reported effects are based on empirical comparisons to permutation distributions and descriptive ANOVA/DFT statistics.
- No symbolic or non-statistical interpretation is included.
