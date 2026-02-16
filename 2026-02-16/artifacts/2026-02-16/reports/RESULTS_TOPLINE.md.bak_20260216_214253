# Results Topline

## Regression Z on 37 layers
- R2 (in-sample): 0.821256853825

## Properties beyond Z (R2 comparison)
- atomic_mass: R2_Z=0.998154843207, R2_layers=0.818181434639, delta=-0.179973408568, n=108
- atomic_radius: R2_Z=NaN, R2_layers=NaN, delta=NaN, n=0
- electronegativity: R2_Z=NaN, R2_layers=NaN, delta=NaN, n=0
- ionization_energy: R2_Z=NaN, R2_layers=NaN, delta=NaN, n=0

## Top independent layers (partial corr | Z)
- b23: mean_abs_partial=0.649736924013, max_abs_partial=0.649736924013
- b26: mean_abs_partial=0.604861532231, max_abs_partial=0.604861532231
- b28: mean_abs_partial=0.520344519758, max_abs_partial=0.520344519758
- b29: mean_abs_partial=0.492266188828, max_abs_partial=0.492266188828
- b35: mean_abs_partial=0.472279190136, max_abs_partial=0.472279190136
- b31: mean_abs_partial=0.471488354280, max_abs_partial=0.471488354280
- b33: mean_abs_partial=0.471307631034, max_abs_partial=0.471307631034
- b20: mean_abs_partial=0.449257764561, max_abs_partial=0.449257764561
- b32: mean_abs_partial=0.448438883977, max_abs_partial=0.448438883977
- b27: mean_abs_partial=0.447602340717, max_abs_partial=0.447602340717

## PCA variance ratios
- PC1: 0.235851109602
- PC2: 0.172315953842
- PC3: 0.113696352031

## K-means best k
- best_k: 6
- silhouette: 0.434639470848

## Top-10 correlations vs Z
- b33: r=0.648171582874
- b35: r=0.647557471211
- b25: r=-0.627758850226
- b26: r=-0.627266633880
- b34: r=-0.579065690156
- b23: r=-0.517126457613
- b17: r=-0.496957948510
- b22: r=-0.482223637854
- b19: r=-0.474788493918
- b21: r=-0.452336906327

## Added diagnostics
- Layer correlation matrix: `reports/layer_correlation_matrix.csv`
- PCA plots: `reports/pca_pc1_vs_z.svg`, `reports/pca_pc2_vs_z.svg`, `reports/pca_pc1_vs_pc2_by_z.svg`
- Cluster vs periodic group: `reports/cluster_vs_periodic.csv`
- Property regression comparison: `reports/property_regression_comparison.csv`
- Partial correlations controlling Z: `reports/partial_correlation_layers_vs_properties.csv`
- Independent layer power: `reports/independent_layer_power.csv`

## Comparative Validation

### Cross-validation (5 folds stratified by period)
- mean_top10_anova_block=3.12866, var=0.738619
- mean_top10_anova_period=35.1938, var=3295.72

### Layer-count comparison
- 16 layers: block=4.58049, period=12.2168, periodicity=5.3278e+07, best_k=2.0, silhouette=0.745048
- 24 layers: block=5.00975, period=15.3065, periodicity=5.3887e+07, best_k=2.0, silhouette=0.73937
- 37 layers: block=6.67723, period=27.368, periodicity=4.98736e+07, best_k=3.0, silhouette=0.728436
- 50 layers: block=7.12151, period=23.9643, periodicity=4.68615e+07, best_k=2.0, silhouette=0.733099

### Baseline comparison
- embedding_37: block=6.67723, period=27.368, periodicity=4.98736e+07, best_k=3, silhouette=0.728436
- baseline_uniform_hist: block=1.6432, period=0.895899, periodicity=1.49622e+08, best_k=3, silhouette=0.956489
- baseline_shell_proxy: block=3.30795, period=9.28831, periodicity=5.35079e+07, best_k=2, silhouette=0.459538

### Stability summary
- jaccard_perm_block_mean: value=0.193727
- jaccard_perm_block_std: value=0.0918297
- jaccard_perm_period_mean: value=0.149029
- jaccard_perm_period_std: value=0.151356
- jaccard_cv_block_pairwise_mean: value=0.18897
- jaccard_cv_block_pairwise_std: value=0.123464
- jaccard_cv_period_pairwise_mean: value=0.245804
- jaccard_cv_period_pairwise_std: value=0.15781

## Stress Tests

### Bootstrap confidence intervals (n=1000)
- mean_top10_anova_block CI95: [10.575, 27.6441]
- mean_top10_anova_period CI95: [21.6005, 92.5495]
- mean_top10_periodicity_strength CI95: [6.71172e+33, 1.77442e+45]

### OOD robustness
- baseline: block=12.7889, period=28.0869, periodicity=3.51651e+44, n=108
- remove_noble_gases: block=11.0525, period=27.9033, periodicity=3.06094e+44, n=102
- remove_lanthanides: block=18.0447, period=22.7981, periodicity=3.32404e+44, n=93

### Band stability summary (50 perturbations)
- degradation_block: mean=0.0442198, std=0.27013
- degradation_period: mean=2.40223, std=4.66024
- degradation_periodicity: mean=513559, std=1.35942e+06

## Final Falsification Test

### Null distribution summary (1000 label permutations)
- mean_top10_anova_block: null_mean=1.94344, null_std=0.675916, null_q95=3.16685, observed=12.7889
- mean_top10_anova_period: null_mean=2.00498, null_std=1.03695, null_q95=3.86303, observed=28.0869
- periodicity_strength: null_mean=3.16338e+44, null_std=6.04335e+43, null_q95=3.51652e+44, observed=3.51651e+44

### Empirical p-values
- mean_top10_anova_block: observed=12.7889, empirical_p=0.000999001
- mean_top10_anova_period: observed=28.0869, empirical_p=0.000999001
- periodicity_strength: observed=3.51651e+44, empirical_p=0.130869

### Final statistical conclusion
- Significant metrics at alpha=0.05: 2/3.
- Mixed evidence: only a subset of summary statistics exceeds the permutation null expectation.

## Law + Geometry
### LAW: score(n_bands)
- Full sweep computed in `reports/tables/score_sweep_full.csv`.
- Local maxima and plateaus in `reports/tables/peaks_local_maxima.csv`.
- Functional candidates compared in `reports/tables/law_model_comparison.csv` (if available).
### GEOMETRY: manifold + graph
- Geometry metrics for 32/37/64 in `reports/tables/geometry_metrics.csv`.
- Figures: `manifold_pca.svg`, `manifold_umap.svg`, `knn_graph_metrics.svg`.
### What would falsify this next?
1. Re-running same protocol on an independent local spectroscopy corpus with inconsistent peak structure.
2. Loss of significance for block/period metrics under stricter permutation baselines.
3. Instability of manifold/graph metrics under deterministic re-binning stress tests.

## Interaction-law benchmark (single summary)
- Benchmark: `data/benchmarks/compounds_binary_pairs.csv`
- Evaluation: ROC AUC, PR AUC, acc@best-threshold, Brier, permutation-corrected p-values
- Permutation setup: `n_perm=2000`, `seed=42`

### Model comparison
- Baseline `L1_harmonic_only`: ROC_AUC=0.377098, PR_AUC=0.311727, Brier=0.338020, p_perm=1.000000
- `L2_harmonic_phi`: ROC_AUC=0.585735, PR_AUC=0.443805, Brier=0.256801, p_perm=0.000500
- `L3_harmonic_phi_dynamic`: ROC_AUC=0.585701, PR_AUC=0.443807, Brier=0.256851, p_perm=0.000500
- `L4_harmonic_phase`: ROC_AUC=0.376412, PR_AUC=0.311030, Brier=0.367437, p_perm=1.000000
- `L5_harmonic_tension`: ROC_AUC=0.384190, PR_AUC=0.314958, Brier=0.317647, p_perm=1.000000
- `L6_psy_triad`: ROC_AUC=0.362008, PR_AUC=0.317059, Brier=0.342577, p_perm=1.000000
- `L7_psy_triad_dynamic`: ROC_AUC=0.360301, PR_AUC=0.316777, Brier=0.347268, p_perm=1.000000

### Falsification clause
- Interaction-law claims are falsified if `L2`/`L3` fail to outperform `L1` under permutation-corrected evaluation.
- Dynamic enrichment is not supported if `L3` does not improve over `L2` under the same permutation protocol.

## Percolation Threshold Test (K=5..37)
- K≈21 status: unsupported
- strongest threshold candidate: K=11
- controls p-values: K21(shuffle=0.553723, phase=0.516242), K*=11(shuffle=0.056972, phase=0.021489)
- reproduce from: code/percolation_threshold_test.py, reports/percolation/percolation_metrics.csv, reports/PERCOLATION_THRESHOLD.md, reports/PERCOLATION_CONTROLS.md

## Interpretation guardrails
- information geometry only; no physical claim.
- Terminology used: supported / not supported / weak-mixed / falsified.

## H1/H2 structural summary
| Hypothesis | Status | Supporting tests | Contradicting tests |
|---|---|---|---|
| K≈21 transition (H1) | not supported | structural event traces near 21 in some metrics | percolation candidate K*=11, shuffle-control attenuation, bootstrap variability |
| K≈37 plateau/memory (H2) | weak-mixed | structural plateau onset near 37, lambda2 slope at 37 | no dynamic gain L3>L2, Kmax sensitivity to padding variant |

Repro files: reports/STRUCTURAL_TRANSITIONS_MULTISEED.md, reports/STRUCTURAL_TRANSITIONS_BOOTSTRAP.md, reports/STRUCTURAL_TRANSITIONS_SHUFFLECONTROL.md, reports/KMAX_EXTENSION_TEST.md, reports/JANUS_DIRECTIONALITY.md, reports/MEMORY_PLATEAU_TEST.md

## Mechanism hypothesis
- Working hypothesis status: not clearly consistent with compact low-rank core + hierarchical refinements + saturation.
- Evidence: K@90=11, K@95=13, collapse_k=14, knee_k=6, percolation_k*=11, modularity_k_max=45
- Interpretation guardrails: information geometry only; no physical claim.

## Generative mechanism scan
- best model=M1 lambda=0.1 match_score=10.817879
- best metrics: erank=11.268, alpha=1.599, K90=9, percolation_k*=5, modularity_k_max=45
- verdict: specific-to-real-structure
- See reports/GENERATIVE_SWEEP.md and reports/GENERATIVE_FALSIFICATION.md
- Guardrail: information geometry only; no physical claim.

## Mechanism update
- Core dimension remains compact: K@90≈11 (see `reports/LOWRANK_DECOMP.md` and `reports/variance_entropy_vs_K.csv`).
- Phi-like proxy: supported; local derivative extrema include K≈22 and K≈34, with strong contrast vs controls (`reports/PHI_LIKE.md`).
- Conditional entropy proxy: supported; change-point candidates include K≈20 and K≈36 (`reports/COND_ENTROPY.md`).
- Synchronization proxy (no native time-series; ordered-by-Z proxy): supported; S rises to K≈37 then flattens (`reports/SYNCHRONIZATION.md`).
- Variance/entropy collapse proxy: supported; local maxima include K≈38, but strongest collapse pattern is multi-site (`reports/VARIANCE_COLLAPSE.md`).
- Joint readout: no single universal transition uniquely pinned to 21 or 37 across all new metrics.
- Information geometry only; no physical claim.

## Extracted laws and minimal mechanism (v1)
- Laws extracted in `reports/LAWS_v1.md` and `reports/LAWS_v1.json`.
- Universality battery outputs: `reports/UNIVERSALITY_TABLE.csv` and `reports/UNIVERSALITY_REPORT.md`.
- Minimal mechanism ablation outputs: `reports/mechanism_minimal_set.csv` and `reports/MECHANISM_MINIMAL_SET.md`.
- Comparator verdicts are mixed (PASS/WEAK/FAIL by law and dataset), indicating partial but non-universal signature transfer.
- Minimal-set sensitivity indicates multi-component dependence (cascade/latent/range constraints), not a single-factor explanation.
- Guardrail: information geometry only; no consciousness/energy/field claims.
