# Percolation Threshold Detection

- seed=42, K=5..37, n_perm=2000
- graph weights: w_ij = max(0, L2_harmonic_phi score)
- threshold schemes: percentile {90,95,97,99} + fixed_density
- candidate detection uses fixed_density transition score

## Top candidate K values
- candidates: [('transition_score_peak', 11), ('max_slope_gcc', 11), ('max_slope_lambda2', 37), ('max_slope_efficiency', 18), ('gcc_cross_0.5', 8)]
- strongest candidate K*: 11
- K≈21 status: unsupported

## Metric support
- GCC crossing 0.5 at K: [8, 11]
- max slope GCC at K: 11
- max slope lambda2 at K: 37
- max slope efficiency at K: 18

## Output files
- reports/percolation/percolation_metrics.csv
- reports/percolation/adjacency_summaries.csv
