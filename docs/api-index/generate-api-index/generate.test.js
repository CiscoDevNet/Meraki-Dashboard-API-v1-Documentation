const assert = require('node:assert/strict');
const { mkdtempSync, writeFileSync } = require('node:fs');
const { tmpdir } = require('node:os');
const path = require('node:path');
const test = require('node:test');

const { fetchOpenAPISpec, generateData } = require('./generate.js');

test('exports an import-safe generator API', () => {
  assert.equal(typeof fetchOpenAPISpec, 'function');
  assert.equal(typeof generateData, 'function');
});

test('loads an explicitly supplied local specification', async () => {
  const directory = mkdtempSync(path.join(tmpdir(), 'api-index-spec-'));
  const specPath = path.join(directory, 'spec.json');
  writeFileSync(specPath, JSON.stringify({ openapi: '3.0.1', info: { version: 'test' }, paths: {} }));

  const spec = await fetchOpenAPISpec(specPath);
  assert.equal(spec.info.version, 'test');
});

test('rejects an explicitly supplied missing local specification', async () => {
  await assert.rejects(
    fetchOpenAPISpec('/definitely/missing/spec.json'),
    /Specification not found/,
  );
});

test('rejects unsuccessful HTTP responses before parsing JSON', async () => {
  const fakeFetch = async () => ({ ok: false, status: 503, statusText: 'Unavailable' });
  await assert.rejects(
    fetchOpenAPISpec('https://example.com/spec.json', fakeFetch),
    /503 Unavailable/,
  );
});
