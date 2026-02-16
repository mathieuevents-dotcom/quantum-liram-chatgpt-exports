# Interaction Protocol (Statistical Scaffold)

## Element Signature Vector
- Source table: `reports/qliram_signatures_37D.csv`.
- Vector per element: standardized 37D feature vector `(b01..b37)`.
- Standardization convention: z-score across elements, deterministic seed=42.

## Pairwise Compatibility Scores
For each unordered pair `(a,b)`:
- `S_cos`: cosine similarity between 37D vectors.
- `S_wcos`: weighted cosine, with non-negative diagonal weights learned by ridge on available proxy target (priority: Z, fallback uniform).
- `S_dot`: raw dot product on standardized 37D vectors.

## Validation Targets
- `same_group`: binary target from periodic group equality (if available).
- `period_distance`: absolute distance in periodic row index.

## Statistical Evaluation
- For `same_group`: AUC per score.
- For `period_distance`: Spearman correlation per score.

## Null Models
- Permutation null with 1000 shuffles.
- For AUC: permute target labels across pairs.
- For Spearman: permute period-distance labels across pairs.

## Reporting
- Outputs:
  - `reports/atom_pair_scores.csv`
  - `reports/interaction_metrics.csv`
  - `reports/interaction_permutation_pvalues.csv`
  - `reports/INTERACTIONS_SUMMARY.md`
- Claims are restricted to statistical association and permutation p-values.
