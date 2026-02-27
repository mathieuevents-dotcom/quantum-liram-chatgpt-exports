# PC Physics Tests

## Key Results

- `pc1` vs `period` (Pearson): r=0.4384, p=2.08e-06, permutation p=0.000999, n=108.
- `pc1` vs `atomic_number` (Pearson): r=0.2693, p=0.00482, permutation p=0.00799, n=108.
- Partial `corr(pc1, period | atomic_number)` (Pearson residualized): r=0.6269, p=3.94e-13, permutation p=0.000999, n=108.
- Partial `corr(pc1, atomic_number | period)` (Pearson residualized): r=-0.5505, p=6.75e-10, permutation p=0.000999, n=108.
- Block separability classifier (`[pc1,pc2,pc3]`): accuracy=0.4628, macro-F1=0.4403.
- Best held-out-period model for `ionization_energy_1` by mean Spearman: `M3_period_group` (rho=0.8555±0.1176, MAE=2.8606±2.2883).
- Best held-out-period model for `electronegativity_pauling` by mean Spearman: `M3_period_group` (rho=0.8606±0.1812, MAE=0.3834±0.2091).
- Best held-out-period model for `atomic_radius` by mean Spearman: `M3_period_group` (rho=0.9990±0.0023, MAE=20.2104±13.7100).

## Interpretation Rules

- Supports shell-ordering if `pc1` keeps a significant association with `period` after controlling for `atomic_number` (partial permutation p < 0.05).
- Supports mostly-Z-ordering if `corr(pc1, atomic_number | period)` remains strong/significant while `corr(pc1, period | atomic_number)` is weak/non-significant.
- Supports shell/block structure beyond Z if `[pc1, pc2, pc3]` classify block above chance with stable macro-F1 and if block tests on `pc2/pc3` are significant (ANOVA/Kruskal p < 0.05).
- Predictive evidence is stronger when held-out-period CV metrics remain good for models using PCs and not only for raw Z/period/group baselines.

## File List

- `reports/pc_physics_tests/block_separability.csv`
- `reports/pc_physics_tests/block_separability.json`
- `reports/pc_physics_tests/fig_pc1_vs_atomic_number.png`
- `reports/pc_physics_tests/fig_pc1_vs_period.png`
- `reports/pc_physics_tests/fig_pc_space_block.png`
- `reports/pc_physics_tests/pc1_shell_vs_Z.csv`
- `reports/pc_physics_tests/pc1_shell_vs_Z.json`
- `reports/pc_physics_tests/property_prediction_details.csv`
- `reports/pc_physics_tests/property_prediction_summary.csv`
- `reports/pc_physics_tests/property_prediction_summary.json`

## Reproduce

```bash
python3 tools/pc_physics_tests/test_pc1_shell_vs_Z.py
python3 tools/pc_physics_tests/predict_atomic_properties_from_pcs.py
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/mplconfig python3 tools/pc_physics_tests/test_block_separability.py
```
