#!/usr/bin/env bash
set -euo pipefail

repository_root="${1:?Usage: verify-release.sh <repository-root> [--deterministic]}"
mode="${2:-}"
repository_root="$(cd "$repository_root" && pwd -P)"
release_tmp="$(mktemp -d)"
trap 'rm -rf -- "$release_tmp"' EXIT

node "$repository_root/scripts/release/release-tools.mjs" validate-spec ga "$repository_root/specs/ga/spec3.json"
node "$repository_root/scripts/release/release-tools.mjs" validate-spec beta "$repository_root/specs/beta/spec3.json"
node "$repository_root/scripts/release/release-tools.mjs" validate-config "$repository_root/config.json" "$repository_root"

manifest_path="$repository_root/specs/manifest.json"
ga_sha="$(node -e 'const m = require(process.argv[1]); process.stdout.write(m.ga.commitSha)' "$manifest_path")"
beta_sha="$(node -e 'const m = require(process.argv[1]); process.stdout.write(m.beta.commitSha)' "$manifest_path")"
node "$repository_root/scripts/release/release-tools.mjs" write-manifest \
  --ga "$repository_root/specs/ga/spec3.json" \
  --ga-sha "$ga_sha" \
  --beta "$repository_root/specs/beta/spec3.json" \
  --beta-sha "$beta_sha" \
  --output "$release_tmp/manifest.json"
cmp "$manifest_path" "$release_tmp/manifest.json"

if [[ "$mode" == "--deterministic" ]]; then
  generated_files=(
    docs/api-index/api-index-html.script.js
    docs/api-index/api-index-html.styles.css
    docs/api-index/meraki-api-index.csv
    docs/api-index/meraki-api-index.md
    docs/api-index/meraki-api-index.html
    docs/ActionBatchesResources.md
  )
  for relative_path in "${generated_files[@]}"; do
    mkdir -p "$release_tmp/before/$(dirname "$relative_path")"
    cp "$repository_root/$relative_path" "$release_tmp/before/$relative_path"
  done

  "$repository_root/scripts/release/generate-release.sh" "$repository_root"

  for relative_path in "${generated_files[@]}"; do
    cmp "$release_tmp/before/$relative_path" "$repository_root/$relative_path"
  done
elif [[ -n "$mode" ]]; then
  echo "Unknown verification option: $mode" >&2
  exit 1
fi

echo "Release package verification passed"
