# Interaction Law Topline

## Definitions (implemented)
- psi: z-scored K-band feature vector per element from `data/external/processed/features_37_layers.csv`.
- psi+, psi-, psi0: diagonal-mask projections from `Pplus`, `Pminus`, `P0` over bands.
- psi(t): currently represented by the dissimilarity term `||psi_a-psi_b||^2` weighted by lambda in V.
- interaction potential: `V(a,b) = -alpha<psi_a+,psi_b-> - beta<psi_a-,psi_b+> + gamma<psi_a0,psi_b0> + lambda||psi_a-psi_b||^2`.

## Inputs / outputs
- inputs: `data/external/processed/features_37_layers.csv`, `data/benchmarks/compounds_binary_pairs.csv`
- outputs: `reports/cgvc_psi_K.csv`, `reports/cgvc_projections.json`, `reports/cgvc_compound_pair_scores.csv`, `reports/cgvc_compound_pair_permtest.csv`, `reports/CGVC_COMPOUND_BENCHMARK.md`

## Benchmark setup
- task: binary pair classification (`y_exists`) on the existing compound benchmark.
- metrics: ROC AUC, PR AUC, accuracy@best-threshold, Brier.
- permutation test: label shuffling, `n_perm=2000`, `seed=42`.

## Current best scores
- baseline best (`S_dot`): ROC_AUC=0.411018, PR_AUC=0.327625, ACC=0.604483, Brier=0.308536
- CGVC interaction law best (`V`): ROC_AUC=0.505100, PR_AUC=0.390134, ACC=0.607449, Brier=0.337479, p_perm=0.316842
- best kernel (`kernel_rbf`): ROC_AUC=0.478989, PR_AUC=0.354909, ACC=0.604483, Brier=0.365262, p_perm=0.974013

## Delta vs baseline
- delta ROC_AUC (V - baseline) = 0.094082
- meaning: statistical benchmark delta only; no physics claim.
