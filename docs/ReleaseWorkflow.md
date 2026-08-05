# API Documentation Release Workflow

This repository packages Meraki Dashboard API specifications and generated documentation for PubHub. PubHub remains the preview and production-publication approval system; GitHub Actions prepares and synchronizes the content.

This document is for repository maintainers and is not part of the public PubHub navigation.

## Release cadence

The **Release API documentation** workflow runs automatically every Wednesday at 20:00 UTC. It can also be run manually from GitHub Actions when an upstream release arrives late or a previous run needs to be retried.

Meraki normally publishes:

- a beta specification every Wednesday
- a GA specification on the first Wednesday of each month

The workflow downloads both channels every week and commits only when their content or generated artifacts change. Calendar position is not used to decide whether GA changed.

## Release inputs and outputs

The workflow resolves immutable commits from these upstream branches:

- GA: `meraki/openapi`, branch `master`
- Beta: `meraki/openapi`, branch `v1-beta`

The exact rendered inputs are stored in:

- `specs/ga/spec3.json`
- `specs/beta/spec3.json`
- `specs/manifest.json`

The manifest records each source branch and commit, API version, checksum, byte size, path count, operation count, and beta-operation count. `config.json` points PubHub at the two local snapshots, so the reference pages and generated index always represent the same release package.

The API index is generated from beta. The action-batches table is generated from GA.

## Scheduled API release sequence

The release workflow performs these operations in order:

1. Check out the newest `main` with full Git history.
2. Resolve both upstream branch commit SHAs in one request.
3. Download the specs at those immutable SHAs with retries and timeouts.
4. Validate structure, channel rules, operation IDs, and conservative size thresholds.
5. Write the local snapshots and deterministic provenance manifest.
6. Install locked API-index dependencies with `npm ci` on Node.js 24.
7. Generate the API index and action-batches table from local files.
8. Regenerate and compare outputs byte-for-byte.
9. Create one release commit if tracked output changed.
10. Rebase that commit onto the latest `main` and revalidate it.
11. Push the single commit to `main`.
12. Ask PubHub to synchronize only after the push succeeds.

The workflow does not use `[skip ci]`, does not modify `test.md`, and does not create separate generator commits.

## Ordinary documentation changes

Normal changes to guides, markdown, configuration, or images do not run the API release pipeline. When a maintainer pushes or merges one of these changes to `main`, the **Sync documentation with PubHub** workflow:

1. checks out that exact commit
2. validates `config.json` and its local file references
3. asks PubHub to synchronize the repository

This path does not download specifications, install generator dependencies, or regenerate API artifacts.

## Publishing in PubHub

A successful synchronization updates the preview for [PubHub project 2864](https://pubhub.cisco.com/detail/2864). Synchronization does not publish production documentation automatically.

Review the changed content in the PubHub portal and use its normal approval controls to publish. The repository's demo API key is intentionally read-only and remains embedded in `config.json` for interactive examples.

## Manual release or rerun

1. Open the repository's **Actions** tab.
2. Select **Release API documentation**.
3. Choose **Run workflow**.
4. Select the `main` branch and confirm the run.
5. Wait for snapshot validation, generation, push, and PubHub synchronization to finish.
6. Open PubHub project 2864 and confirm the expected GA/beta versions before publishing.

A manual run follows exactly the same validation and atomic-commit path as the Wednesday schedule.

## Failure recovery

| Failure stage | Result | Recovery |
| --- | --- | --- |
| Resolve or download | No repository or PubHub change | Confirm the upstream branches exist and rerun after GitHub connectivity recovers. |
| Spec validation | No repository or PubHub change | Inspect the reported version, count, release-stage, or missing `operationId`; confirm the upstream spec is complete before changing a safety threshold. |
| Generation or determinism | No repository or PubHub change | Reproduce with `npm ci` and `scripts/release/verify-release.sh "$PWD" --deterministic`, then fix the generator or input. |
| Rebase conflict | Release commit is not pushed and PubHub is not called | Review the concurrent `main` change, resolve it normally, and manually rerun the workflow. |
| Push rejected | PubHub is not called | Check branch protection and workflow `contents: write` permission, then rerun. |
| PubHub request | The release commit is already on `main` | Rerun the lightweight **Sync documentation with PubHub** workflow or push the intended follow-up documentation change; do not edit `test.md`. |

Detailed GitHub job output intentionally excludes tokens and unrestricted PubHub response bodies.

## Local verification

From the repository root, with the API-index dependencies installed:

```bash
cd docs/api-index/generate-api-index
npm ci
cd ../../..
node --test scripts/release/*.test.mjs
npm --prefix docs/api-index/generate-api-index test
scripts/release/verify-release.sh "$PWD" --deterministic
```

To prepare a new local snapshot deliberately, run `scripts/release/download-specs.sh "$PWD"` before generation. That command requires internet access and replaces both local specification files together.
