#!/usr/bin/env bash
set -euo pipefail

if ! command -v doxygen >/dev/null 2>&1; then
  echo "doxygen is required to build XML output" >&2
  exit 127
fi

for config in docs/doxygen/*/Doxyfile; do
  echo "Building Doxygen XML from ${config}"
  doxygen "${config}"
done
