#!/usr/bin/env bash
set -euo pipefail

if [[ ! -d "chatgpt_exports" ]]; then
  echo "Error: missing directory: chatgpt_exports/" >&2
  exit 1
fi

LATEST=$(ls -1 chatgpt_exports | sort | tail -n 1)

if [[ -z "${LATEST}" ]]; then
  echo "Error: no dated folder found in chatgpt_exports/" >&2
  exit 1
fi

if [[ ! -d "chatgpt_exports/${LATEST}" ]]; then
  echo "Error: latest entry is not a directory: chatgpt_exports/${LATEST}" >&2
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
