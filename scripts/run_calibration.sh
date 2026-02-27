#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH="${1:-calibration/calibration_config.yaml}"
CURVE_PATH="${2:-2026-02-16/reports/calibration/sensitivity_curve.csv}"
NULL_PCA_PATH="${3:-2026-02-16/artifacts/2026-02-16/synthetic_null/pca_variance_ratio.csv}"
OUT_REPORT="${4:-reports/calibration_report.md}"

if [[ ! -f "${CONFIG_PATH}" ]]; then
  echo "Missing config: ${CONFIG_PATH}" >&2
  exit 1
fi
if [[ ! -f "${CURVE_PATH}" ]]; then
  echo "Missing sensitivity curve: ${CURVE_PATH}" >&2
  exit 1
fi
if [[ ! -f "${NULL_PCA_PATH}" ]]; then
  echo "Missing synthetic-null PCA file: ${NULL_PCA_PATH}" >&2
  exit 1
fi

dataset=$(awk -F': ' '/^dataset:/{print $2}' "${CONFIG_PATH}")
seed=$(awk -F': ' '/^seed:/{print $2}' "${CONFIG_PATH}")
sample_size=$(awk -F': ' '/^sample_size:/{print $2}' "${CONFIG_PATH}")
noise_level=$(awk -F': ' '/^noise_level:/{sub(/^"/,"",$2);sub(/"$/,"",$2);print $2}' "${CONFIG_PATH}")
layers=$(awk -F': ' '/^number_of_layers:/{print $2}' "${CONFIG_PATH}")
cfg_pc1=$(awk -F': ' '/pc1:/{print $2}' "${CONFIG_PATH}")
cfg_pc2=$(awk -F': ' '/pc2:/{print $2}' "${CONFIG_PATH}")
cfg_pc3=$(awk -F': ' '/pc3:/{print $2}' "${CONFIG_PATH}")
cfg_k=$(awk -F': ' '/^clustering_k:/{print $2}' "${CONFIG_PATH}")
cfg_sil=$(awk -F': ' '/^silhouette_score:/{print $2}' "${CONFIG_PATH}")
cfg_rob=$(awk -F': ' '/ari_pairwise_mean:/{print $2}' "${CONFIG_PATH}")

min_detectable_strength=$(awk -F',' 'NR>1 && $8+0>=0.10 && $11+0>=0.10 {print $1; exit}' "${CURVE_PATH}")
if [[ -z "${min_detectable_strength}" ]]; then
  min_detectable_strength="not_detected"
fi

null_line=$(awk -F',' 'NR>1 && $1+0==0 {print $0; exit}' "${CURVE_PATH}")
null_pc1=$(echo "${null_line}" | awk -F',' '{print $4}')
null_sil=$(echo "${null_line}" | awk -F',' '{print $8}')
null_rob=$(echo "${null_line}" | awk -F',' '{print $11}')
null_top_corr=$(echo "${null_line}" | awk -F',' '{print $10}')

mkdir -p "$(dirname "${OUT_REPORT}")"
cat > "${OUT_REPORT}" <<EOF
# Calibration Report (Reproducible Replay)

Reference state: v1.0

## Configuration Source
- config_path: ${CONFIG_PATH}
- dataset: ${dataset}
- seed: ${seed}
- sample_size: ${sample_size}
- noise_level: ${noise_level}
- number_of_layers: ${layers}

## Baseline Metrics (from config)
- pca_explained_variance: pc1=${cfg_pc1}, pc2=${cfg_pc2}, pc3=${cfg_pc3}
- clustering_k: ${cfg_k}
- silhouette_score: ${cfg_sil}
- robustness_mean_ari_pairwise: ${cfg_rob}

## Sensitivity/Null Validation (from existing artifacts)
- sensitivity_curve_path: ${CURVE_PATH}
- synthetic_null_pca_path: ${NULL_PCA_PATH}
- null_control: pc1=${null_pc1}, silhouette=${null_sil}, robustness_mean=${null_rob}, top_abs_corr=${null_top_corr}
- criterion: silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10
- minimal_detectable_strength: ${min_detectable_strength}

## Reproducibility
- command: scripts/run_calibration.sh ${CONFIG_PATH} ${CURVE_PATH} ${NULL_PCA_PATH} ${OUT_REPORT}
EOF

echo "Generated: ${OUT_REPORT}"
