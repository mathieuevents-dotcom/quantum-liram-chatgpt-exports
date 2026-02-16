# Final Report

## Methods
- Offline deterministic execution (seed=42; single-thread BLAS/OMP).
- End-to-end single entrypoint: `bash scripts/run_all.sh`.
- Pipeline stages include parsing/features, PCA/KMeans/correlations, structural/comparative/stress/falsification, law+geometry, and qliram exports.

## Datasets Used
- Local processed spectroscopy tables in `data/external/processed/` (lines, levels, features, coverage).
- Local element metadata from `data/reference/periodic_table_min.csv` and/or `data/external/elements_table.csv`.
- No internet source used during this run.

## Key Results Snapshot
- Coverage: 108 elements (94 with both lines+levels).
- Best n_bands: block=50, period=37, silhouette=39.
- Fine sweep K=37 classes: block=C, period=A, periodicity=C.
- Global permutation p-values: block=0.000999001, period=0.000999001, periodicity=0.130869.

## Artifact List
- `reports/RESULTS_TOPLINE.md`
- `reports/FINE_SWEEP_SUMMARY.md`
- `reports/SUBGROUP_K_ANALYSIS.md`
- `reports/permutation_pvalues_37_layers.csv`
- `reports/cv_37_layers.csv`
- `reports/stability_37_layers.csv`
- `reports/bootstrap_37_layers.csv`
- `reports/ood_tests_37_layers.csv`
- `reports/band_perturbation_robustness.csv`
- `reports/tables/score_sweep_full.csv`
- `reports/tables/peaks_local_maxima.csv`
- `reports/tables/stability_rebinning.csv`
- `reports/tables/geometry_metrics.csv`
- `reports/qliram_signatures_37D.csv`
- `reports/qliram_periodic_table.csv`
- `reports/qliram_periodic_table.html`
- `reports/qliram_pair_scores.csv`
- `reports/qliram_interaction_tests.csv`
- `reports/qliram_interaction_tests.md`

## Falsifiability Checklist
- Re-run with same seed and confirm hashes in `reports/manifest.sha256` are identical.
- Recompute metrics after perturbing bins and compare against recorded degradations.
- Verify permutation p-values remain in similar range under repeated deterministic runs.
- Check whether conclusions change when excluding subdomains (noble gases, lanthanides).
