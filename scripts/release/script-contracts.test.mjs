import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));

function script(name) {
  return readFileSync(path.join(scriptDirectory, name), 'utf8');
}

test('download script resolves immutable refs and uses bounded reliable downloads', () => {
  const contents = script('download-specs.sh');
  assert.match(contents, /set -euo pipefail/);
  assert.match(contents, /git ls-remote/);
  assert.match(contents, /refs\/heads\/master/);
  assert.match(contents, /refs\/heads\/v1-beta/);
  assert.match(contents, /--fail-with-body/);
  assert.match(contents, /--retry 4/);
  assert.match(contents, /--retry-all-errors/);
  assert.match(contents, /--connect-timeout 15/);
  assert.match(contents, /--max-time 120/);
  assert.match(contents, /write-manifest/);
  assert.doesNotMatch(contents, /test\.md/);
});

test('generation script uses only the committed beta and GA snapshots', () => {
  const contents = script('generate-release.sh');
  assert.match(contents, /set -euo pipefail/);
  assert.match(contents, /specs\/beta\/spec3\.json/);
  assert.match(contents, /specs\/ga\/spec3\.json/);
  assert.match(contents, /meraki-api-index\.csv/);
  assert.match(contents, /ActionBatchesResources\.md/);
  assert.doesNotMatch(contents, /raw\.githubusercontent\.com/);
});

test('verification script checks manifest bytes and deterministic generation', () => {
  const contents = script('verify-release.sh');
  assert.match(contents, /validate-spec.*ga/);
  assert.match(contents, /validate-spec.*beta/);
  assert.match(contents, /validate-config/);
  assert.match(contents, /write-manifest/);
  assert.match(contents, /cmp/);
  assert.match(contents, /--deterministic/);
  assert.match(contents, /generate-release\.sh/);
});

test('PubHub script has bounded retries and never prints the token or response body', () => {
  const contents = script('sync-pubhub.sh');
  assert.match(contents, /set -euo pipefail/);
  assert.match(contents, /--fail-with-body/);
  assert.match(contents, /--retry 4/);
  assert.match(contents, /--retry-all-errors/);
  assert.match(contents, /--connect-timeout 15/);
  assert.match(contents, /--max-time 90/);
  assert.match(contents, /Authorization: Token/);
  assert.match(contents, /commit/);
  assert.doesNotMatch(contents, /cat .*response/);
});
