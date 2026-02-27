#!/usr/bin/env bash
set -euo pipefail

mkdir -p chatgpt_exports

RUN_ROOT=$(find . -type d -path './20??-??-??/artifacts/20??-??-??/reports' | sort | tail -n 1)
if [[ -z "${RUN_ROOT}" || ! -d "${RUN_ROOT}" ]]; then
  echo "Error: could not find deterministic run root under ./YYYY-MM-DD/artifacts/YYYY-MM-DD/reports" >&2
  exit 1
fi
RUN_PARENT="${RUN_ROOT%/reports}"

PCA_SRC="${RUN_ROOT}/robustness/R0_baseline/pca_variance_ratio.csv"
ROBUSTNESS_SRC="${RUN_ROOT}/robustness/summary.csv"
ROBUSTNESS_MD="${RUN_ROOT}/ROBUSTNESS_37_LAYERS.md"
SENS_CURVE_SRC="${RUN_ROOT}/calibration/sensitivity_curve.csv"
NULL_PCA_SRC="${RUN_PARENT}/synthetic_null/pca_variance_ratio.csv"

if [[ ! -f "${PCA_SRC}" ]]; then
  echo "Error: missing expected PCA source: ${PCA_SRC}" >&2
  exit 1
fi
if [[ ! -f "${SENS_CURVE_SRC}" ]]; then
  ALT_SENS_1="${RUN_PARENT%/artifacts/*}/reports/calibration/sensitivity_curve.csv"
  ALT_SENS_2="./2026-02-16/reports/calibration/sensitivity_curve.csv"
  if [[ -f "${ALT_SENS_1}" ]]; then
    SENS_CURVE_SRC="${ALT_SENS_1}"
  elif [[ -f "${ALT_SENS_2}" ]]; then
    SENS_CURVE_SRC="${ALT_SENS_2}"
  else
    echo "Error: missing expected sensitivity curve: ${SENS_CURVE_SRC}" >&2
    exit 1
  fi
fi
if [[ ! -f "${NULL_PCA_SRC}" ]]; then
  echo "Error: missing expected synthetic-null PCA: ${NULL_PCA_SRC}" >&2
  exit 1
fi

STAMP=$(date +%F_%H%M%S)
EXPORT_DIR="chatgpt_exports/${STAMP}"
mkdir -p "${EXPORT_DIR}"

# Core artifacts from a single deterministic run root.
cp "${PCA_SRC}" "${EXPORT_DIR}/pca_variance_ratio.csv"
cp "${SENS_CURVE_SRC}" "${EXPORT_DIR}/sensitivity_curve.csv"
cp "${NULL_PCA_SRC}" "${EXPORT_DIR}/synthetic_null_pca_variance_ratio.csv"

copied_corr=0
for corr_file in "${RUN_ROOT}"/correlation_layers_vs_*.csv; do
  if [[ -f "${corr_file}" ]]; then
    cp "${corr_file}" "${EXPORT_DIR}/"
    copied_corr=1
  fi
done
if [[ "${copied_corr}" -ne 1 ]]; then
  echo "Error: no correlation_layers_vs_*.csv found under ${RUN_ROOT}" >&2
  exit 1
fi

# Bring forward human logs when available.
if [[ -f "docs/DAILY_DIGEST.md" ]]; then
  cp "docs/DAILY_DIGEST.md" "${EXPORT_DIR}/DAILY_DIGEST.md"
fi
if [[ -f "docs/DISCOVERY_LOG.md" ]]; then
  cp "docs/DISCOVERY_LOG.md" "${EXPORT_DIR}/DISCOVERY_LOG.md"
fi

if [[ -f "calibration/calibration_config.yaml" ]]; then
  cp "calibration/calibration_config.yaml" "${EXPORT_DIR}/calibration_config.yaml"
elif [[ -f "calibration_config.yaml" ]]; then
  cp "calibration_config.yaml" "${EXPORT_DIR}/calibration_config.yaml"
else
  echo "Error: missing calibration_config.yaml in calibration/ or repo root" >&2
  exit 1
fi

# Ensure robustness summary is non-empty; derive from ROBUSTNESS_37_LAYERS.md if needed.
robustness_nonempty=0
if [[ -f "${ROBUSTNESS_SRC}" ]]; then
  if awk -F',' 'NR>1 && ($2!="" || $3!="" || $4!="" || $5!="" || $6!="" || $7!=""){ok=1} END{exit ok?0:1}' "${ROBUSTNESS_SRC}"; then
    cp "${ROBUSTNESS_SRC}" "${EXPORT_DIR}/robustness_summary.csv"
    robustness_nonempty=1
  fi
fi

if [[ "${robustness_nonempty}" -ne 1 ]]; then
  if [[ ! -f "${ROBUSTNESS_MD}" ]]; then
    echo "Error: robustness summary csv is empty and fallback markdown is missing: ${ROBUSTNESS_MD}" >&2
    exit 1
  fi
  awk -F'|' '
  BEGIN {
    OFS=",";
    print "regime,best_k,best_silhouette,pc1_var,pc2_var,pc3_var,ari_pairwise_mean,procrustes_disparity_vs_R0,spearman_corr_vs_Z_rank_vs_R0";
  }
  /^\| R[0-9]_/ {
    regime=$2; best_k=$3; best_s=$4; pc1=$5; pc2=$6; pc3=$7; ari=$8; proc=$9; spear=$10;
    gsub(/^[ \t]+|[ \t]+$/, "", regime);
    gsub(/^[ \t]+|[ \t]+$/, "", best_k);
    gsub(/^[ \t]+|[ \t]+$/, "", best_s);
    gsub(/^[ \t]+|[ \t]+$/, "", pc1);
    gsub(/^[ \t]+|[ \t]+$/, "", pc2);
    gsub(/^[ \t]+|[ \t]+$/, "", pc3);
    gsub(/^[ \t]+|[ \t]+$/, "", ari);
    gsub(/^[ \t]+|[ \t]+$/, "", proc);
    gsub(/^[ \t]+|[ \t]+$/, "", spear);
    gsub(/~/, "", proc);
    print regime,best_k,best_s,pc1,pc2,pc3,ari,proc,spear;
  }' "${ROBUSTNESS_MD}" > "${EXPORT_DIR}/robustness_summary.csv"
fi

# Build bundle-local sensitivity validation.
MDS=$(awk -F',' 'NR>1{if($8+0>=0.10 && $11+0>=0.10 && found==0){mds=$1; found=1}} END{if(found) print mds; else print "not_detected"}' "${EXPORT_DIR}/sensitivity_curve.csv")
cat > "${EXPORT_DIR}/sensitivity_validation.md" <<EOF
# Sensitivity Validation

## Inputs
- sensitivity_curve: sensitivity_curve.csv

## Criterion
- pass if silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10

## Outcome
- minimal_detectable_strength: ${MDS}
- status: $(if [[ "${MDS}" != "not_detected" ]]; then echo PASS; else echo FAIL; fi)
EOF

pc1=$(awk -F',' 'NR==2{print $2}' "${EXPORT_DIR}/pca_variance_ratio.csv")
pc2=$(awk -F',' 'NR==3{print $2}' "${EXPORT_DIR}/pca_variance_ratio.csv")
pc3=$(awk -F',' 'NR==4{print $2}' "${EXPORT_DIR}/pca_variance_ratio.csv")
r4_ari=$(awk -F',' 'NR>1 && $1 ~ /^R4_gaussian_noise/ {print $7; exit}' "${EXPORT_DIR}/robustness_summary.csv")
if [[ -z "${r4_ari}" ]]; then
  r4_ari=$(awk -F',' 'NR==2{print $7}' "${EXPORT_DIR}/robustness_summary.csv")
fi
if [[ -z "${r4_ari}" ]]; then
  r4_ari="unavailable"
fi

cat > "${EXPORT_DIR}/calibration_report.md" <<EOF
# Calibration Report (Bundle-Local)

Reference state: v1.0

## Configuration Source
- config_path: calibration_config.yaml
- dataset: $(awk -F': ' '/^dataset:/{print $2}' "${EXPORT_DIR}/calibration_config.yaml")
- seed: $(awk -F': ' '/^seed:/{print $2}' "${EXPORT_DIR}/calibration_config.yaml")
- sample_size: $(awk -F': ' '/^sample_size:/{print $2}' "${EXPORT_DIR}/calibration_config.yaml")
- noise_level: $(awk -F': ' '/^noise_level:/{sub(/^"/,"",$2);sub(/"$/,"",$2);print $2}' "${EXPORT_DIR}/calibration_config.yaml")
- number_of_layers: $(awk -F': ' '/^number_of_layers:/{print $2}' "${EXPORT_DIR}/calibration_config.yaml")

## Baseline Metrics
- pca_explained_variance: pc1=${pc1}, pc2=${pc2}, pc3=${pc3}
- robustness_mean_ari_pairwise: ${r4_ari}

## Sensitivity/Null Validation
- sensitivity_curve_path: sensitivity_curve.csv
- synthetic_null_pca_path: synthetic_null_pca_variance_ratio.csv
- criterion: silhouette >= 0.10 AND robustness_silhouette_mean >= 0.10
- minimal_detectable_strength: ${MDS}

## Reproducibility
- command: scripts/export_for_chatgpt.sh
EOF

echo "Run root: $(realpath "${RUN_ROOT}")"
echo "PCA source: $(realpath "${PCA_SRC}")"
if [[ -f "${ROBUSTNESS_SRC}" ]]; then
  echo "Robustness source candidate: $(realpath "${ROBUSTNESS_SRC}")"
fi
echo "Export folder: $(realpath "${EXPORT_DIR}")"

LATEST=$(ls -1 chatgpt_exports | sort | tail -n 1)
if [[ -z "${LATEST}" || ! -d "chatgpt_exports/${LATEST}" ]]; then
  echo "Error: no dated folder found in chatgpt_exports/" >&2
  exit 1
fi

ARCHIVE="chatgpt_exports_${LATEST}.tar.gz"
tar -czf "${ARCHIVE}" "chatgpt_exports/${LATEST}"

if [[ ! -f "${ARCHIVE}" ]]; then
  echo "Error: archive was not created: ${ARCHIVE}" >&2
  exit 1
fi

SIZE=$(du -h "${ARCHIVE}" | awk '{print $1}')
echo "Archive: $(pwd)/${ARCHIVE}"
echo "Size: ${SIZE}"
