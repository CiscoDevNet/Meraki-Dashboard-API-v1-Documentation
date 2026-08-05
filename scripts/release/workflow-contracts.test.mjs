import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const repositoryRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const workflowDirectory = path.join(repositoryRoot, '.github/workflows');

function workflow(name) {
  return readFileSync(path.join(workflowDirectory, name), 'utf8');
}

function ordered(contents, values) {
  let previous = -1;
  for (const value of values) {
    const current = contents.indexOf(value);
    assert.ok(current > previous, `Expected ${value} after the previous release step`);
    previous = current;
  }
}

test('only one workflow owns scheduled API generation', () => {
  assert.equal(existsSync(path.join(workflowDirectory, 'generate_api_index.yml')), false);
  assert.equal(existsSync(path.join(workflowDirectory, 'generate_action_batches_table.yml')), false);

  const contents = workflow('release_api_docs.yml');
  assert.match(contents, /cron: ['"]0 20 \* \* 3['"]/);
  assert.match(contents, /workflow_dispatch:/);
  assert.doesNotMatch(contents, /^\s+push:/m);
  assert.match(contents, /contents: write/);
  assert.match(contents, /group: pubhub-main/);
  assert.match(contents, /cancel-in-progress: false/);
  assert.match(contents, /actions\/checkout@v5/);
  assert.match(contents, /actions\/setup-node@v5/);
  assert.match(contents, /node-version: ['"]24['"]/);
  assert.match(contents, /npm ci/);
});

test('release workflow pushes one verified commit before synchronizing PubHub', () => {
  const contents = workflow('release_api_docs.yml');
  ordered(contents, [
    'download-specs.sh',
    'generate-release.sh',
    'verify-release.sh',
    'git commit',
    'git pull --rebase origin main',
    'git push origin HEAD:main',
    'sync-pubhub.sh',
  ]);
  assert.match(contents, /if: steps\.release\.outputs\.changed == 'true'/);
  assert.doesNotMatch(contents, /\[skip ci\]/);
  assert.doesNotMatch(contents, /test\.md/);
});

test('ordinary main pushes only validate local references and synchronize PubHub', () => {
  const contents = workflow('pubhub.yml');
  assert.match(contents, /^\s+push:/m);
  assert.match(contents, /branches:/);
  assert.match(contents, /- main/);
  assert.match(contents, /contents: read/);
  assert.match(contents, /group: pubhub-main/);
  assert.match(contents, /validate-config/);
  assert.match(contents, /sync-pubhub\.sh/);
  assert.doesNotMatch(contents, /download-specs\.sh/);
  assert.doesNotMatch(contents, /generate-release\.sh/);
  assert.doesNotMatch(contents, /fjogeleit/);
  assert.doesNotMatch(contents, /outputs\.response/);
});

test('a queued ordinary push skips PubHub when a newer main commit exists', () => {
  const contents = workflow('pubhub.yml');
  ordered(contents, [
    'git fetch origin main',
    'git rev-parse origin/main',
    'validate-config',
    'sync-pubhub.sh',
  ]);
  assert.match(contents, /id: latest/);
  assert.match(contents, /if: steps\.latest\.outputs\.current == 'true'/g);
});
