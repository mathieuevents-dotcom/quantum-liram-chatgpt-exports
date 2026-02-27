#!/usr/bin/env bash
set -euo pipefail

SEED="${SEED:-42}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

mkdir -p reports figures
export MPLBACKEND="${MPLBACKEND:-Agg}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-/tmp/mplconfig}"
mkdir -p "${MPLCONFIGDIR}"

echo "[phi3] seed=${SEED}"
echo "[phi3] Step 1/2: build merged PC+atomic table"
bash tools/run_atomicprops_analysis.sh

echo "[phi3] Step 2/2: generate phi3 outputs"
python3 tools/generate_phi3_outputs.py --seed "${SEED}"

required=(
  "reports/overview.html"
  "reports/phi3_projection.csv"
  "reports/phi3_projection_shuffled.csv"
  "reports/phi3_geometry_analysis.md"
  "figures/phi3_cluster_labeled.svg"
)

echo "[phi3] Verifying required outputs"
for f in "${required[@]}"; do
  if [[ ! -f "${f}" ]]; then
    echo "[phi3] Missing required artifact: ${f}" >&2
    exit 1
  fi
  echo "[phi3] OK ${f}"
done

echo "[phi3] Completed successfully"
