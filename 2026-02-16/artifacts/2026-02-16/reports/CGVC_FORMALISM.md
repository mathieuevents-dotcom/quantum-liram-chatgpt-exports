# CGVC Formalism

## 1) Objects and notation
Let \(E\) be the finite set of elements in the analyzed dataset, and let \(d \in \mathbb{N}\) be the feature dimension.

For each element \(e \in E\), define a feature vector:
\[
x_e \in \mathbb{R}^d.
\]

In the current pipeline, a common choice is \(d=37\) (band features), but the same formalism applies to any \(d=K\).

## 2) Optional diagonal weighting
Define an optional diagonal weight matrix:
\[
W = \mathrm{diag}(w_1,\dots,w_d), \quad w_i \ge 0.
\]

If no weighting is used, set \(W=I_d\).

## 3) Similarity
Define weighted cosine similarity between elements \(e,f\):
\[
s(e,f) = \cos_W(x_e,x_f)
= \frac{x_e^\top W x_f}{\sqrt{x_e^\top W x_e}\sqrt{x_f^\top W x_f}}.
\]

Unweighted cosine is recovered with \(W=I_d\).

## 4) Affinity graph
Construct an undirected affinity graph \(G=(V,\mathcal{E},A)\):
- \(V = E\)
- \(A_{ef} = s(e,f)\) (dense form), or \(A_{ef}=0\) outside a k-NN neighborhood (sparse form)
- \(\mathcal{E}=\{(e,f): A_{ef}\neq 0\}\)

Graph-derived quantities (e.g., modularity, clustering coefficient) are computed from \(A\).

## 5) Definition of layer count \(K\)
\(K\) denotes a model-size control variable, interpreted as either:
1. feature embedding dimension (\(d=K\), e.g., number of frequency bands), or
2. clustering regime size (e.g., candidate cluster count in a sweep).

The repository uses both interpretations in separate procedures.

## 6) Objective functions
For each \(K\), define evaluation scores used by existing analyses:

1. Period discrimination metric:
\[
J_{\mathrm{period}}(K)=\mathrm{mean\_top10}\{F_j^{(\mathrm{period})}\}_{j=1}^d
\]
where \(F_j^{(\mathrm{period})}\) is an ANOVA-style \(F\)-statistic for feature \(j\) across period labels.

2. Block discrimination metric:
\[
J_{\mathrm{block}}(K)=\mathrm{mean\_top10}\{F_j^{(\mathrm{block})}\}_{j=1}^d.
\]

3. Clustering separation metric:
\[
J_{\mathrm{sil}}(K)=\max_{k \in \{2,\dots,12\}} \mathrm{Silhouette}(k; X_K).
\]

No physical interpretation is assumed in these objective definitions.

## 7) Link to concrete repository outputs
- Element features (\(x_e\)): `data/external/processed/features_37_layers.csv`
- Release mirror of same: `release/processed/features_37_layers.csv`
- Pairwise similarity outputs: `reports/atom_pair_scores.csv`, `reports/qliram_pair_scores.csv`
- Best-\(K\) and sweep summaries:
  - `reports/fine_K_sweep.csv`
  - `reports/bandcount_comparison_full.csv`
  - `reports/layer_count_comparison.csv`
  - `reports/FINE_SWEEP_SUMMARY.md`
  - `reports/RESULTS_TOPLINE.md`

## 8) What 37 could mean (testable hypotheses only)

### H1: Intrinsic-dimension optimum
\(K=37\) approximates a dimension where discrimination objectives are locally optimized:
\[
J(K=37) > J(36),\; J(37) > J(38)
\]
for one or more objectives \(J \in \{J_{\mathrm{period}},J_{\mathrm{block}},J_{\mathrm{sil}}\}\).

### H2: Stability plateau/local maximum
\(K=37\) belongs to a statistically stable neighborhood under perturbations (bootstrap, permutations, re-binning), even if not a strict isolated maximum.

### H3: Artifact hypothesis
Observed preference for \(K=37\) is a pipeline artifact (parser, binning, or evaluation leakage), not a stable property of the data-generating process.

Falsification route: verify that \(K=37\) does not persist under independent datasets, null-label controls, and alternative preprocessing choices.

