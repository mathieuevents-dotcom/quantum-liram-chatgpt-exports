#!/usr/bin/env bash
set -euo pipefail

export MPLBACKEND=Agg
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/mplconfig}"
mkdir -p "${MPLCONFIGDIR}"

python3 tools/build_atomic_properties_table.py
python3 tools/compute_element_pcs.py
python3 tools/merge_pcs_with_atomic_properties.py
python3 tools/analyze_pc_atomic_correlations.py
python3 tools/make_pc_atomicprops_figures.py

echo "Outputs saved under:"
echo "  data/external/atomic_properties/"
echo "  reports/elements_pcs_atomicprops.csv"
echo "  reports/elements_pcs_atomicprops_merged.csv"
echo "  reports/pc_atomicprops_correlations.json"
echo "  reports/pc_atomicprops_partial_correlations.json"
echo "  reports/pc_atomicprops_permutation_pvalues.json"
echo "  reports/pc_atomicprops_permutation_null_samples.csv"
echo "  reports/figures/fig_pc1_vs_*.png"
