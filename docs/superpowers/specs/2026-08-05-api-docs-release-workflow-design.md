# API Documentation Release Workflow Design

## Objective

Make API documentation releases deterministic and atomic while preserving PubHub as the human review and publication gate. A scheduled workflow will package the GA specification, beta specification, and all generated documentation into one commit. Ordinary documentation changes will continue to synchronize with PubHub without running the specification release pipeline.

## Release cadence and triggers

- Run the API release workflow every Wednesday at 20:00 UTC.
- Support `workflow_dispatch` so a late or failed upstream release can be processed manually.
- Fetch both upstream branches on every API release run:
  - GA: `meraki/openapi` branch `master`
  - Beta: `meraki/openapi` branch `v1-beta`
- Expect beta to change weekly and GA normally to change on the first Wednesday of each month, but determine changes from content rather than calendar position.
- Do not use changes to `test.md` or ordinary guide files to trigger API regeneration.
- Continue synchronizing ordinary documentation pushes to `main` with PubHub through a lightweight workflow.

## Release package

The repository will contain the exact specifications rendered by PubHub:

- `specs/ga/spec3.json`
- `specs/beta/spec3.json`
- `specs/manifest.json`

The manifest will record, for each specification:

- source repository and branch
- resolved upstream Git commit SHA
- OpenAPI version
- API version from `info.version`
- SHA-256 checksum
- byte size
- path count
- operation count

`config.json` will reference the local GA and beta specification files. The API index will be generated from the local beta snapshot, and the action-batches table will be generated from the local GA snapshot. The existing read-only demo bearer token in `config.json` will remain unchanged.

## Atomic release flow

The scheduled or manually dispatched workflow will:

1. Check out `main` with full history.
2. Resolve the current GA and beta upstream commit SHAs.
3. Download both specifications into a temporary staging directory using bounded retries and timeouts.
4. Validate both specifications and build the provenance manifest.
5. Copy the validated snapshots into their repository paths.
6. Install locked generator dependencies with `npm ci` on a supported Node.js runtime.
7. Generate the API index from the local beta specification.
8. Generate the action-batches table from the local GA specification.
9. Validate `config.json`, local content references, generated outputs, and deterministic regeneration.
10. Create one commit containing both specifications, the manifest, configuration, and every generated artifact.
11. Fetch the newest `origin/main` and rebase the release commit onto it.
12. Re-run the fast local-reference and generated-output checks after rebasing.
13. Push that single release commit to `main`.
14. Invoke PubHub synchronization only after the push succeeds.

If no tracked release-package file changed, the workflow will exit successfully without committing or synchronizing PubHub.

A push made by the workflow's `GITHUB_TOKEN` does not create a second GitHub Actions run. The API release workflow therefore owns the PubHub call for its own commit. Human-authored pushes to `main` remain handled by the lightweight PubHub workflow.

## Concurrency and race handling

- Give the API release workflow a repository-wide release concurrency group and do not cancel an in-progress release.
- Generate from staged immutable inputs rather than mutable URLs.
- Fetch and rebase immediately before the release commit.
- If the rebase conflicts or the push loses a race, fail without calling PubHub.
- Permit a manual rerun after resolving the conflict or after an upstream release arrives late.
- Remove the separate direct-to-`main` generator workflows so independent jobs can no longer race.

## Validation gates

The workflow must fail before modifying `main` when any of these checks fail:

- either download does not return HTTP 200 after bounded retries
- either file is invalid JSON
- the document is not OpenAPI 3.x
- `info.version` or `paths` is absent
- there are no operations with operation IDs
- path or operation counts fall below conservative minimums derived from current specifications
- the beta snapshot contains no beta release-stage operations
- the GA snapshot contains beta release-stage operations
- a required local file referenced by `config.json` is missing
- a generator exits unsuccessfully or omits an expected output
- a second generation pass changes tracked generated output
- rebasing or pushing the atomic commit fails

The validation tooling will expose small, testable commands rather than embedding all logic directly in workflow YAML.

## PubHub synchronization

The API release workflow and lightweight documentation workflow will call one shared synchronization script or reusable workflow interface. It will:

- use the existing PubHub project ID and token secrets
- enforce connection and overall timeouts
- retry transient network and server failures
- fail on non-success HTTP status codes
- avoid printing credentials or unrestricted response bodies
- report the Git commit SHA submitted for synchronization

The API release workflow will depend on successful validation, commit, and push steps, ensuring PubHub is never called for a failed release. The PubHub portal remains the only production publication approval step.

## Ordinary documentation changes

Changes to guides, markdown, images, or other non-specification documentation will not download specifications or run generators. A push to `main` will:

1. validate `config.json` syntax and required local references
2. synchronize the exact merged commit with PubHub
3. leave publication approval to the PubHub portal

This keeps everyday documentation work fast while retaining automatic preview synchronization.

## Testing strategy

Automated tests will cover:

- valid GA and beta specification acceptance
- malformed JSON rejection
- missing OpenAPI metadata rejection
- minimum path and operation count enforcement
- GA/beta release-stage constraints
- deterministic manifest contents apart from explicitly excluded volatile data
- generator behavior with explicit local specification paths
- failure when regeneration leaves a diff
- workflow trigger separation between scheduled API releases and ordinary pushes
- job dependencies that prevent PubHub synchronization after validation, commit, or push failures

Workflow YAML, shell scripts, JavaScript, JSON, and generated artifacts will also receive syntax checks. Network-dependent behavior will be tested through explicit command boundaries so validation logic can run against local fixtures.

## Internal documentation

Create `docs/ReleaseWorkflow.md` and link it from the repository `README.md`. It will document:

- release cadence and triggers
- upstream GA and beta sources
- local snapshot and manifest layout
- validation and generation sequence
- the atomic commit and synchronization behavior
- ordinary documentation behavior
- manual rerun procedure
- failure diagnosis and recovery
- PubHub preview and manual publication responsibilities

The document is repository-internal and will not be added to `config.json` or the public PubHub navigation.

## Operational outcome

Each API release visible to PubHub corresponds to one Git commit containing the exact GA and beta specifications and all artifacts derived from them. Additional guides synchronize independently without invoking the expensive release pipeline. No placeholder edit to `test.md` is required.
