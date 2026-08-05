# Reliable API Documentation Release Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic Wednesday API-release pipeline that commits local GA/beta specifications and all generated artifacts atomically, while ordinary documentation pushes perform only lightweight validation and PubHub synchronization.

**Architecture:** Testable Node.js release utilities validate and describe immutable local specifications. A scheduled workflow resolves upstream SHAs, downloads both snapshots, generates every derived artifact from local files, verifies determinism, rebases one release commit, pushes it, and then calls a shared hardened PubHub synchronization script. A separate lightweight push workflow validates local references and calls the same synchronization script without regenerating API content.

**Tech Stack:** GitHub Actions, Node.js 24 built-in test runner, POSIX shell, `git`, `curl`, JSON/OpenAPI 3.x.

## Global Constraints

- Schedule API releases every Wednesday at 20:00 UTC and support manual dispatch.
- Push one atomic release commit directly to `main`; do not create a release PR.
- Keep PubHub as the human preview and production-publication approval gate.
- Do not regenerate specifications or API artifacts for ordinary guide, markdown, or image changes.
- Keep the existing read-only demo API key in `config.json` unchanged.
- Store both full specification files in Git; file size is accepted.
- Generate the API index from beta and the action-batches table from GA.
- Do not add the internal release document to public PubHub navigation.
- Never call PubHub after a failed validation, generation, rebase, or push.
- Preserve the user's untracked `config-tmp.json`.

---

### Task 1: Specification inspection, manifest, and config-reference utilities

**Files:**
- Create: `scripts/release/release-tools.mjs`
- Create: `scripts/release/release-tools.test.mjs`

**Interfaces:**
- Produces: `inspectSpec(spec, channel) -> SpecMetadata`
- Produces: `createManifest({ ga, beta }) -> Manifest`
- Produces: `validateConfigReferences(configPath, repositoryRoot) -> string[]`
- Produces CLI commands: `validate-spec`, `write-manifest`, and `validate-config`

- [ ] **Step 1: Write failing tests for GA/beta validation**

Use `node:test` and construct small in-memory OpenAPI documents. Assert that `inspectSpec` accepts valid GA/beta inputs and rejects malformed channel content, absent metadata, too-small documents, GA beta operations, and beta documents without beta operations. Export minimums as constants so tests can build documents exactly at the boundary.

```js
test('rejects beta specs without beta operations', () => {
  const spec = makeSpec({ paths: MINIMUMS.beta.paths, betaOperations: 0 });
  assert.throws(() => inspectSpec(spec, 'beta'), /beta operation/i);
});
```

- [ ] **Step 2: Run the tests and verify the expected module-not-found failure**

Run: `node --test scripts/release/release-tools.test.mjs`

Expected: FAIL because `release-tools.mjs` does not exist.

- [ ] **Step 3: Implement `inspectSpec` minimally**

Count only OpenAPI HTTP methods under `paths`. Require OpenAPI 3.x, a non-empty `info.version`, conservative minimums (`ga`: 500 paths/800 operations; `beta`: 900 paths/1200 operations), an `operationId` for each counted operation, zero beta-stage operations in GA, and at least one beta-stage operation in beta.

- [ ] **Step 4: Run the tests and verify validation passes**

Run: `node --test scripts/release/release-tools.test.mjs`

Expected: PASS for the validation tests.

- [ ] **Step 5: Write failing manifest determinism tests**

Assert fixed key ordering and that the manifest includes repository, branch, commit SHA, OpenAPI/API versions, SHA-256, bytes, paths, and operations without a timestamp.

- [ ] **Step 6: Implement deterministic manifest creation and CLI output**

`write-manifest` accepts `--ga`, `--ga-sha`, `--beta`, `--beta-sha`, and `--output`, reads exact file bytes, validates both documents, hashes them, and writes formatted JSON with a trailing newline.

- [ ] **Step 7: Write failing local-reference tests**

Create temporary `config.json` fixtures and assert local `content`, `$remoteModule`, `overview.markdownPath`, and `sampleCode.folder` values must exist while `http(s)` content is ignored.

- [ ] **Step 8: Implement config-reference traversal and CLI**

The `validate-config` command parses JSON, reports all missing paths together, and exits non-zero on syntax or reference errors.

- [ ] **Step 9: Run the complete utility suite**

Run: `node --test scripts/release/release-tools.test.mjs`

Expected: all tests PASS with no warnings.

### Task 2: Make the API-index generator safe for explicit local inputs

**Files:**
- Modify: `docs/api-index/generate-api-index/generate.js:58-73,294-405`
- Modify: `docs/api-index/generate-api-index/package.json:6-8`
- Create: `docs/api-index/generate-api-index/generate.test.js`

**Interfaces:**
- Produces: `fetchOpenAPISpec(specPath) -> Promise<object>` that never silently falls back when an explicit path is invalid.
- Produces: `generateData(args) -> Promise<void>` and a CLI that exits non-zero on errors.

- [ ] **Step 1: Write failing tests for explicit local input and missing files**

Import the generator without executing it. Assert a temporary local spec loads successfully and an explicitly supplied missing path rejects with `Specification not found`.

- [ ] **Step 2: Run tests and confirm import side effects or missing exports fail**

Run: `cd docs/api-index/generate-api-index && node --test generate.test.js`

Expected: FAIL because the module runs immediately and does not export the required functions.

- [ ] **Step 3: Add a main guard, exports, and strict input handling**

Use `if (require.main === module)` for CLI execution. Check `response.ok` for URL inputs, attach a bounded request timeout, throw when an explicit local path is absent, and set `process.exitCode = 1` on CLI failure instead of swallowing the error.

- [ ] **Step 4: Replace the placeholder package test command**

Set `scripts.test` to `node --test generate.test.js` without changing locked runtime dependencies.

- [ ] **Step 5: Run generator tests**

Run: `cd docs/api-index/generate-api-index && npm test`

Expected: all tests PASS.

### Task 3: Download, generation, determinism, and PubHub command boundaries

**Files:**
- Create: `scripts/release/download-specs.sh`
- Create: `scripts/release/generate-release.sh`
- Create: `scripts/release/verify-release.sh`
- Create: `scripts/release/sync-pubhub.sh`
- Create: `scripts/release/script-contracts.test.mjs`

**Interfaces:**
- `download-specs.sh <repository-root>` writes `specs/ga/spec3.json`, `specs/beta/spec3.json`, and `specs/manifest.json`.
- `generate-release.sh <repository-root>` regenerates the API index and action-batches table from local snapshots.
- `verify-release.sh <repository-root> [--deterministic]` validates snapshots/config and optionally proves regeneration leaves the expected output bytes unchanged.
- `sync-pubhub.sh <project-id> <token> <commit-sha>` calls PubHub with bounded retries and sanitized output.

- [ ] **Step 1: Write failing script contract tests**

Read the scripts as text and spawn safe local portions. Require `set -euo pipefail`, exact local spec paths, `git ls-remote` SHA resolution, curl `--fail-with-body`, retry/connect/overall timeout flags, manifest generation, fixed generated-output copies, and absence of `test.md` mutation.

- [ ] **Step 2: Run and verify scripts are missing**

Run: `node --test scripts/release/script-contracts.test.mjs`

Expected: FAIL because the scripts do not exist.

- [ ] **Step 3: Implement `download-specs.sh`**

Resolve both refs in one `git ls-remote` call. Download raw files at the resolved commit SHAs into `mktemp -d`, validate them before copying to repository paths, and then invoke `write-manifest`. Install a trap that removes only the exact temporary directory.

- [ ] **Step 4: Implement `generate-release.sh`**

Run `generate.js` with `specs/beta/spec3.json`, copy only the five expected API-index files, and invoke the action-batches generator with `specs/ga/spec3.json` and the explicit output path.

- [ ] **Step 5: Implement `verify-release.sh`**

Run both spec validations, config-reference validation, and manifest regeneration to a temporary file followed by `cmp`. With `--deterministic`, copy the expected generated outputs to a temporary directory, run generation, and compare every output byte-for-byte with its saved copy.

- [ ] **Step 6: Implement hardened PubHub synchronization**

Use the existing endpoint and secrets, `curl --fail-with-body --retry 4 --retry-all-errors --connect-timeout 15 --max-time 90`, write the response to a temporary file, print only a success line with the commit SHA, and never print the token.

- [ ] **Step 7: Run script contract tests and shell syntax checks**

Run: `node --test scripts/release/script-contracts.test.mjs && for f in scripts/release/*.sh; do sh -n "$f"; done`

Expected: all tests and syntax checks PASS.

### Task 4: Commit the initial immutable specification package

**Files:**
- Create: `specs/ga/spec3.json`
- Create: `specs/beta/spec3.json`
- Create: `specs/manifest.json`
- Modify: `config.json:144,188`
- Modify generated: `docs/api-index/meraki-api-index.csv`
- Modify generated: `docs/api-index/meraki-api-index.md`
- Modify generated: `docs/api-index/meraki-api-index.html`
- Modify generated: `docs/api-index/api-index-html.script.js`
- Modify generated: `docs/api-index/api-index-html.styles.css`
- Modify generated: `docs/ActionBatchesResources.md`

**Interfaces:**
- `config.json` GA content becomes `specs/ga/spec3.json`.
- `config.json` beta content becomes `specs/beta/spec3.json`.

- [ ] **Step 1: Run config validation before changing URLs and confirm it does not yet prove local snapshots**

Run: `node scripts/release/release-tools.mjs validate-config config.json .`

Expected: PASS but the release contract test still FAILS because GA/beta OAS content uses mutable URLs.

- [ ] **Step 2: Download the current upstream snapshots through the new command**

Run: `scripts/release/download-specs.sh "$PWD"`

Expected: both specs and a valid deterministic manifest are written.

- [ ] **Step 3: Change only the two Meraki API-reference content URLs**

Keep SecureConnect remote and leave both demo bearer token values unchanged.

- [ ] **Step 4: Install locked dependencies and regenerate all artifacts**

Run: `cd docs/api-index/generate-api-index && npm ci`

Run: `scripts/release/generate-release.sh "$PWD"`

Expected: generation succeeds using only local GA/beta inputs.

- [ ] **Step 5: Verify deterministic release content**

Run: `scripts/release/verify-release.sh "$PWD"`

Run generation a second time and require no additional diff.

### Task 5: Replace racing workflows with the atomic scheduled release

**Files:**
- Delete: `.github/workflows/generate_api_index.yml`
- Delete: `.github/workflows/generate_action_batches_table.yml`
- Create: `.github/workflows/release_api_docs.yml`
- Modify: `.github/workflows/pubhub.yml`
- Create: `scripts/release/workflow-contracts.test.mjs`

**Interfaces:**
- Scheduled release trigger: cron `0 20 * * 3` and `workflow_dispatch`.
- Ordinary push trigger: `push` to `main` only.
- Both workflows use concurrency group `pubhub-main` with `cancel-in-progress: false`.

- [ ] **Step 1: Write failing workflow contract tests**

Assert the old generator workflows are absent; release workflow has schedule/manual triggers, `contents: write`, Node 24, `npm ci`, download/generate/verify/commit/rebase/push ordering, and PubHub only after successful push; ordinary workflow has no spec download or generator command and invokes config validation before PubHub.

- [ ] **Step 2: Run tests and confirm old workflows violate the contract**

Run: `node --test scripts/release/workflow-contracts.test.mjs`

Expected: FAIL on the existing independent push workflows.

- [ ] **Step 3: Implement `release_api_docs.yml`**

Use `actions/checkout@v5`, `actions/setup-node@v5`, full history, explicit `main`, Node 24, `npm ci`, the release scripts, and one commit named `Update API documentation from OpenAPI`. Write a `changed` step output; skip commit/push/PubHub when clean. After committing, `git pull --rebase origin main`, run fast validation plus `git diff --exit-code`, push, and call PubHub.

- [ ] **Step 4: Replace `pubhub.yml` with lightweight validation and sync**

Checkout the pushed commit, set up Node 24, validate config references, and call the shared PubHub script. Give it `contents: read`; remove the mutable third-party HTTP action and response echo.

- [ ] **Step 5: Remove both obsolete generator workflows**

Delete them only after the scheduled workflow includes both generators.

- [ ] **Step 6: Run workflow contract and syntax tests**

Run: `node --test scripts/release/workflow-contracts.test.mjs`

Run: `ruby -e 'require "yaml"; Dir[".github/workflows/*.yml"].each { |f| YAML.load_file(f); puts f }'`

Expected: contract tests PASS and all workflow files parse.

### Task 6: Document the internal CI/CD pipeline

**Files:**
- Create: `docs/ReleaseWorkflow.md`
- Modify: `README.md:14-16`

**Interfaces:**
- README links repository maintainers to `docs/ReleaseWorkflow.md`.
- The new file is not referenced by `config.json`.

- [ ] **Step 1: Add a failing documentation contract assertion**

Extend `workflow-contracts.test.mjs` to require the internal document, README link, Wednesday cadence, manual rerun, ordinary-doc path, recovery steps, and explicit PubHub human approval.

- [ ] **Step 2: Run the contract test and verify failure**

Run: `node --test scripts/release/workflow-contracts.test.mjs`

Expected: FAIL because the documentation is absent.

- [ ] **Step 3: Write the internal release workflow documentation and README link**

Document operator-facing triggers, files, checks, exact rerun UI steps, likely failure stages, recovery without `test.md`, and the PubHub portal responsibility. Do not add the page to public navigation.

- [ ] **Step 4: Run documentation contract tests**

Run: `node --test scripts/release/workflow-contracts.test.mjs`

Expected: PASS.

### Task 7: Full verification and handoff

**Files:**
- Verify all modified and created files from Tasks 1-6.

**Interfaces:**
- Produces a repository state ready for review and push; no external workflow dispatch or PubHub sync is performed locally.

- [ ] **Step 1: Run all Node tests**

Run: `node --test scripts/release/*.test.mjs`

Run: `cd docs/api-index/generate-api-index && npm test`

Expected: all tests PASS with zero failures.

- [ ] **Step 2: Run deterministic release verification**

Run: `scripts/release/verify-release.sh "$PWD" --deterministic`

Expected: validation succeeds and generated release files remain unchanged.

- [ ] **Step 3: Run syntax and repository checks**

Run: `jq empty config.json specs/manifest.json specs/ga/spec3.json specs/beta/spec3.json`

Run: `for f in scripts/release/*.sh; do sh -n "$f"; done`

Run: `ruby -e 'require "yaml"; Dir[".github/workflows/*.yml"].each { |f| YAML.load_file(f) }'`

Run: `git diff --check`

Expected: every command exits 0.

- [ ] **Step 4: Review the final diff and generated scope**

Run: `git status --short && git diff --stat && git diff -- .github/workflows scripts/release config.json README.md docs/ReleaseWorkflow.md`

Confirm `config-tmp.json` remains untracked and unchanged, the demo key remains present, no public navigation entry was added, and no unrelated file was modified.

- [ ] **Step 5: Commit the implementation**

Stage only the intended implementation, snapshots, and generated files. Commit with:

```bash
git commit -m "ci: make API documentation releases atomic"
```

- [ ] **Step 6: Report deployment behavior and residual verification**

State that local verification cannot prove the real PubHub secret/endpoint or GitHub scheduled execution. Recommend manually dispatching `release_api_docs.yml` once after push and confirming project 2864 shows the commit before approving publication.
