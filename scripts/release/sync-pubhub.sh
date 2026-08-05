#!/usr/bin/env bash
set -euo pipefail

project_id="${1:?Usage: sync-pubhub.sh <project-id> <token> <commit-sha>}"
pubhub_token="${2:?Usage: sync-pubhub.sh <project-id> <token> <commit-sha>}"
commit_sha="${3:?Usage: sync-pubhub.sh <project-id> <token> <commit-sha>}"
response_file="$(mktemp)"
trap 'rm -f -- "$response_file"' EXIT

curl --silent --show-error --location --fail-with-body \
  --retry 4 --retry-all-errors \
  --connect-timeout 15 --max-time 90 \
  --header "Authorization: Token ${pubhub_token}" \
  --output "$response_file" \
  "https://devnet.cisco.com/v1/pubhub/projects/sync/${project_id}/"

echo "PubHub synchronization accepted for commit ${commit_sha}"
