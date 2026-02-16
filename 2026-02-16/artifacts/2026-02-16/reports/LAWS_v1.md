# LAWS_v1
- Scope: empirical, non-metaphysical laws from current offline battery.
- Guardrail: information geometry only; no physical claim.

## L1_phi_excess — Integrated Coupling Excess
- Operational definition: Phi-like normalized coupling is above block-preserving shuffle baseline over cumulative K, with elevated value at K=37.
- Metrics used: phi_norm(K), dPhi/dK extrema, empirical p-value vs controls
- Evidence summary: PHI_LIKE.md: phi_norm(21)=1.1789, phi_norm(37)=1.3916, strongest z=47.5, p=0.0005
- Pass criteria: phi_norm(37)>1 and min empirical p<0.05 with supported verdict
- Current status: supported
- Failure mode / falsification: collapses under within-layer/block-preserving/random controls or phi_norm near 1

## L2_conditional_structure — Adjacent-Layer Conditional Structure
- Operational definition: Cumulative adjacent conditional entropy profile shows non-trivial structure and control separation.
- Metrics used: H_disc(K), H_gauss(K), dH/dK change points, empirical p-value
- Evidence summary: COND_ENTROPY.md: change points include K≈20,36; strongest z=106.99, p=0.0005
- Pass criteria: supported verdict with control-separated entropy profile (p<0.05)
- Current status: supported
- Failure mode / falsification: entropy profile converges to controls or permutation p>=0.05

## L3_sync_surplus — Cross-layer Synchronization Surplus
- Operational definition: Synchronization proxy based on max-lag correlations exceeds shuffled/phase/random controls.
- Metrics used: S(K), dS/dK, empirical p-value vs temporal/phase/random controls
- Evidence summary: SYNCHRONIZATION.md: S(21)=0.3459, S(37)=0.3967, strongest z=39.68, p=0.0005
- Pass criteria: supported verdict and p<0.05 under primary control
- Current status: supported
- Failure mode / falsification: no separation under temporal-order or phase-randomized controls

## L4_entropy_collapse_pattern — Variance-Entropy Collapse Pattern
- Operational definition: Spectral entropy/top-variance cumulative profile exhibits structured collapse peaks rather than monotone triviality.
- Metrics used: spectral entropy(K), top1 variance ratio(K), collapse_score(K), empirical p-value
- Evidence summary: VARIANCE_COLLAPSE.md: maxima include K≈38; strongest z=5.19, p=0.0005
- Pass criteria: supported verdict and non-trivial collapse-score maxima with p<0.05
- Current status: supported
- Failure mode / falsification: collapse-score becomes flat/noisy and matches shuffled baselines

## L5_anchor_non_uniqueness — Anchor Non-uniqueness
- Operational definition: No single K universally dominates all metrics; anchors are distributed across multiple K bands.
- Metrics used: percolation K*, modularity Kmax, multi-metric extrema sets
- Evidence summary: RESULTS_TOPLINE.md + mechanism update: K*≈11, extrema near 20–22 and 34–38
- Pass criteria: joint readout indicates distributed anchors, not single-K lock-in
- Current status: supported
- Failure mode / falsification: all metrics converge to same narrow K under controls

