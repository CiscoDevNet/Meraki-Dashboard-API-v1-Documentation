#!/usr/bin/env bash
set -euo pipefail

repository_root="${1:?Usage: generate-release.sh <repository-root>}"
repository_root="$(cd "$repository_root" && pwd -P)"
index_generator="$repository_root/docs/api-index/generate-api-index"
index_output="$index_generator/output"

(
  cd "$index_generator"
  node generate.js "$repository_root/specs/beta/spec3.json"
)

index_files=(
  api-index-html.script.js
  api-index-html.styles.css
  meraki-api-index.csv
  meraki-api-index.md
  meraki-api-index.html
)

for file in "${index_files[@]}"; do
  source_file="$index_output/$file"
  if [[ ! -f "$source_file" ]]; then
    echo "Expected API-index output missing: $source_file" >&2
    exit 1
  fi
  install -m 0644 "$source_file" "$repository_root/docs/api-index/$file"
done

node "$repository_root/docs/action-batches/generate-action-batches/generate-action-batches-table.js" \
  "$repository_root/specs/ga/spec3.json" \
  "$repository_root/docs/ActionBatchesResources.md"
