# Intra-Period PC1-Group Tests

- Input file: `reports/elements_pcs_atomicprops_merged.csv`
- Rows after dropping missing `pc1/period/group`: **80**
- Random seed: `20260220`
- Within-period permutations per period: `2000`
- Global residualized permutations: `5000`

## Per-Period Results

| period | n | pearson_r | pearson_p | spearman_rho | spearman_p | ols_r2 | ols_p_slope | perm_p_two_sided |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | nan | nan | nan | nan | nan | nan | nan |
| 2 | 8 | 0.6139 | 0.1054 | 0.4762 | 0.2329 | 0.3769 | 0.1054 | 0.07946 |
| 3 | 8 | 0.5698 | 0.1404 | 0.3095 | 0.4556 | 0.3246 | 0.1404 | 0.1609 |
| 4 | 18 | -0.0145 | 0.9544 | -0.2487 | 0.3196 | 0.0002 | 0.9544 | 0.953 |
| 5 | 18 | -0.3916 | 0.1081 | -0.5253 | 0.02518 | 0.1533 | 0.1081 | 0.09945 |
| 6 | 18 | -0.7008 | 0.001198 | -0.7833 | 0.0001208 | 0.4911 | 0.001198 | 0.001499 |
| 7 | 8 | -0.6212 | 0.1002 | -0.7910 | 0.01938 | 0.3859 | 0.1002 | 0.1034 |

## Global Residualized Test

- Residualization model: `pc1 ~ period`
- Pearson(`pc1_resid`, `group`) = **0.0747** (p=0.5101)
- Spearman(`pc1_resid`, `group`) = **0.1279** (p=0.2584)
- OLS `pc1_resid ~ group`: R^2=0.0056, slope p=0.5101
- Permutation two-sided p-value (Pearson): **0.5197**
