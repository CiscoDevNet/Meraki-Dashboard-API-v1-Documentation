const assert = require('node:assert/strict');
const { mkdtempSync, readFileSync, writeFileSync } = require('node:fs');
const { tmpdir } = require('node:os');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const { fetchOpenAPISpec, generateData, toMarkdownTable } = require('./generate.js');

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

test('wraps every Markdown data row without trailing whitespace', () => {
  const table = toMarkdownTable([
    { Operation: 'GET /one', Scope: '' },
    { Operation: 'POST /two', Scope: 'write' },
  ], ['Operation', 'Scope']);

  assert.equal(table, [
    '| Operation | Scope |',
    '| --- | --- |',
    '| GET /one |  |',
    '| POST /two | write |',
  ].join('\n'));
  for (const line of table.split('\n')) assert.doesNotMatch(line, /\s+$/);
});

test('full CSV download resolves beside the PubHub-hosted script asset', async () => {
  const directory = mkdtempSync(path.join(tmpdir(), 'api-index-download-'));
  const specPath = path.join(directory, 'spec.json');
  writeFileSync(specPath, JSON.stringify({
    openapi: '3.0.1',
    info: { version: 'test' },
    paths: {},
  }));

  const originalDirectory = process.cwd();
  try {
    process.chdir(directory);
    await generateData([specPath]);
  } finally {
    process.chdir(originalDirectory);
  }

  const html = readFileSync(path.join(directory, 'meraki-api-index.html'), 'utf8');
  const script = readFileSync(path.join(directory, 'api-index-html.script.js'), 'utf8');
  const handler = html.match(/<button[^>]+onclick="([^"]+)"[^>]*>Download full CSV<\/button>/)?.[1];
  assert.ok(handler, 'generated HTML must include a full CSV download handler');

  const pageUrl = 'https://developer.cisco.com/meraki/api-v1/api-index/';
  const scriptUrl = 'https://pubhub.devnetcloud.com/media/Meraki-Dashboard-API-v1-Documentation/docs/docs/api-index/api-index-html.script.js';
  let navigatedTo;
  const location = {
    assign(value) {
      navigatedTo = new URL(value, pageUrl).href;
    },
    get href() {
      return pageUrl;
    },
    set href(value) {
      navigatedTo = new URL(value, pageUrl).href;
    },
  };
  const context = {
    document: {
      addEventListener() {},
      currentScript: { src: scriptUrl },
    },
    URL,
    window: { location },
  };

  vm.runInNewContext(script, context);
  vm.runInNewContext(handler, context);

  assert.equal(
    navigatedTo,
    'https://pubhub.devnetcloud.com/media/Meraki-Dashboard-API-v1-Documentation/docs/docs/api-index/meraki-api-index.csv',
  );
});
