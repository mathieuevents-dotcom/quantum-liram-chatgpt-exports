#!/usr/bin/env bash
set -euo pipefail

SCRIPT="tools/intra_period_tests.py"

if [[ ! -f "$SCRIPT" ]]; then
  echo "Missing script: $SCRIPT" >&2
  exit 1
fi

echo "Running: python3 $SCRIPT"
python3 "$SCRIPT"

echo "Saved outputs:"
echo "- reports/intra_period_group_stats.csv"
echo "- reports/partial_pc1_period_group.json"
echo "- reports/intra_period_summary.md"
