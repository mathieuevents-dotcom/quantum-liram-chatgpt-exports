#!/usr/bin/env bash
set -euo pipefail

SCRIPT='tools/analyze_pc2_pc3.py'

echo "Running: MPLBACKEND=Agg MPLCONFIGDIR=/tmp/mplconfig python3 ${SCRIPT}"
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/mplconfig python3 "${SCRIPT}"

echo "Saved outputs:"
echo "- reports/pc2_pc3_correlations.csv"
echo "- reports/pc2_pc3_partial_correlations.csv"
echo "- reports/pc2_pc3_correlations.json"
echo "- reports/pc2_pc3_snippet.tex"
echo "- reports/figures/fig_pc2_vs_period.png"
echo "- reports/figures/fig_pc3_vs_period.png"
echo "- reports/figures/fig_pc2_vs_ionization.png"
echo "- reports/figures/fig_pc3_vs_radius.png"
