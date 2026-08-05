#!/usr/bin/env bash
set -euo pipefail

repository_root="${1:?Usage: download-specs.sh <repository-root>}"
repository_root="$(cd "$repository_root" && pwd -P)"
release_tmp="$(mktemp -d)"
trap 'rm -rf -- "$release_tmp"' EXIT

openapi_repository="https://github.com/meraki/openapi.git"
refs="$(git ls-remote "$openapi_repository" refs/heads/master refs/heads/v1-beta)"
ga_sha="$(awk '$2 == "refs/heads/master" { print $1 }' <<<"$refs")"
beta_sha="$(awk '$2 == "refs/heads/v1-beta" { print $1 }' <<<"$refs")"

if [[ ! "$ga_sha" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Unable to resolve meraki/openapi master" >&2
  exit 1
fi
if [[ ! "$beta_sha" =~ ^[0-9a-f]{40}$ ]]; then
  echo "Unable to resolve meraki/openapi v1-beta" >&2
  exit 1
fi

download_spec() {
  local sha="$1"
  local output="$2"
  curl --silent --show-error --location --fail-with-body \
    --retry 4 --retry-all-errors \
    --connect-timeout 15 --max-time 120 \
    --output "$output" \
    "https://raw.githubusercontent.com/meraki/openapi/${sha}/openapi/spec3.json"
}

download_spec "$ga_sha" "$release_tmp/ga-spec3.json"
download_spec "$beta_sha" "$release_tmp/beta-spec3.json"

node "$repository_root/scripts/release/release-tools.mjs" validate-spec ga "$release_tmp/ga-spec3.json"
node "$repository_root/scripts/release/release-tools.mjs" validate-spec beta "$release_tmp/beta-spec3.json"
node "$repository_root/scripts/release/release-tools.mjs" write-manifest \
  --ga "$release_tmp/ga-spec3.json" \
  --ga-sha "$ga_sha" \
  --beta "$release_tmp/beta-spec3.json" \
  --beta-sha "$beta_sha" \
  --output "$release_tmp/manifest.json"

mkdir -p "$repository_root/specs/ga" "$repository_root/specs/beta"
install -m 0644 "$release_tmp/ga-spec3.json" "$repository_root/specs/ga/spec3.json"
install -m 0644 "$release_tmp/beta-spec3.json" "$repository_root/specs/beta/spec3.json"
install -m 0644 "$release_tmp/manifest.json" "$repository_root/specs/manifest.json"

echo "Downloaded GA ${ga_sha} and beta ${beta_sha}"
