#!/usr/bin/env bash
set -euo pipefail

export MPLBACKEND=Agg
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/mplconfig}"
mkdir -p "${MPLCONFIGDIR}"

python3 tools/spectral_mp_audit.py

echo "Key outputs:"
echo "  reports/spectral_mp_summary.json"
echo "  reports/spectral_pvalue.json"
echo "  reports/montecarlo_lambda1_null.csv"
echo "  reports/spectral_mp_report.tex"
echo "  reports/figures/eigen_spectrum_vs_mp.png"
echo "  reports/figures/lambda1_null_hist.png"
