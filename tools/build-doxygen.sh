#!/usr/bin/env bash
set -euo pipefail

if ! command -v doxygen >/dev/null 2>&1; then
  echo "doxygen is required to build XML output" >&2
  exit 127
fi

mkdir -p docs/doxygen/build

for config in docs/doxygen/*/Doxyfile; do
  echo "Building Doxygen XML from ${config}"

  inputs="$(
    awk -F= '/^[[:space:]]*INPUT[[:space:]]*=/ {
      sub(/^[^=]*=[[:space:]]*/, "")
      print
      exit
    }' "${config}"
  )"
  existing_inputs=()
  for input in ${inputs}; do
    if [ -e "${input}" ]; then
      existing_inputs+=("${input}")
    fi
  done

  if [ "${#existing_inputs[@]}" -eq 0 ]; then
    echo "No configured Doxygen inputs exist for ${config}" >&2
    exit 1
  fi

  tmp_config="$(mktemp docs/doxygen/build/Doxyfile.XXXXXX)"
  awk -v input_line="INPUT                  = ${existing_inputs[*]}" '
    /^[[:space:]]*INPUT[[:space:]]*=/ {
      print input_line
      next
    }
    { print }
  ' "${config}" >"${tmp_config}"

  if ! doxygen "${tmp_config}"; then
    rm -f "${tmp_config}"
    exit 1
  fi
  rm -f "${tmp_config}"
done
