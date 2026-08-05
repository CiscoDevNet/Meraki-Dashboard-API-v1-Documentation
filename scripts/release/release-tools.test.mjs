import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';
import test from 'node:test';

import {
  MINIMUMS,
  createManifest,
  inspectSpec,
  validateConfigReferences,
} from './release-tools.mjs';

const HTTP_METHODS = ['get', 'post', 'put', 'delete', 'patch', 'head', 'options', 'trace'];

function makeSpec(channel, { betaOperations, missingOperationId = false } = {}) {
  const minimum = MINIMUMS[channel];
  const paths = {};
  let operationIndex = 0;

  for (let pathIndex = 0; pathIndex < minimum.paths; pathIndex += 1) {
    const operationsForPath = {};
    for (const method of HTTP_METHODS) {
      if (operationIndex >= minimum.operations) break;
      operationsForPath[method] = {
        operationId: `operation${operationIndex}`,
        responses: { 200: { description: 'ok' } },
      };
      operationIndex += 1;
    }
    paths[`/resource/${pathIndex}`] = operationsForPath;
  }

  const requestedBetaOperations = betaOperations ?? (channel === 'beta' ? 1 : 0);
  let marked = 0;
  for (const pathItem of Object.values(paths)) {
    for (const method of HTTP_METHODS) {
      if (marked >= requestedBetaOperations) break;
      if (pathItem[method]) {
        pathItem[method]['x-release-stage'] = 'beta';
        marked += 1;
      }
    }
    if (marked >= requestedBetaOperations) break;
  }

  if (missingOperationId) delete paths['/resource/0'].get.operationId;

  return {
    openapi: '3.0.1',
    info: { title: 'Fixture', version: channel === 'ga' ? '1.2.3' : '1.2.3-beta.1' },
    paths,
  };
}

test('accepts a valid GA specification at the safety boundary', () => {
  const result = inspectSpec(makeSpec('ga'), 'ga');
  assert.equal(result.paths, MINIMUMS.ga.paths);
  assert.equal(result.operations, MINIMUMS.ga.operations);
  assert.equal(result.betaOperations, 0);
});

test('accepts a valid beta specification with beta operations', () => {
  const result = inspectSpec(makeSpec('beta'), 'beta');
  assert.equal(result.paths, MINIMUMS.beta.paths);
  assert.equal(result.operations, MINIMUMS.beta.operations);
  assert.equal(result.betaOperations, 1);
});

test('rejects specifications that are not OpenAPI 3.x', () => {
  const spec = makeSpec('ga');
  spec.openapi = '2.0';
  assert.throws(() => inspectSpec(spec, 'ga'), /OpenAPI 3/i);
});

test('rejects specifications without an API version', () => {
  const spec = makeSpec('ga');
  delete spec.info.version;
  assert.throws(() => inspectSpec(spec, 'ga'), /info\.version/i);
});

test('rejects unexpectedly small specifications', () => {
  const spec = makeSpec('ga');
  delete spec.paths['/resource/0'];
  assert.throws(() => inspectSpec(spec, 'ga'), /at least 500 paths/i);
});

test('rejects operations without operationId', () => {
  assert.throws(() => inspectSpec(makeSpec('ga', { missingOperationId: true }), 'ga'), /operationId/i);
});

test('rejects beta-stage operations in GA', () => {
  assert.throws(() => inspectSpec(makeSpec('ga', { betaOperations: 1 }), 'ga'), /GA.*beta/i);
});

test('rejects beta specs without beta operations', () => {
  assert.throws(() => inspectSpec(makeSpec('beta', { betaOperations: 0 }), 'beta'), /beta operation/i);
});

test('creates a deterministic provenance manifest without volatile fields', () => {
  const manifestInput = {
    ga: {
      metadata: inspectSpec(makeSpec('ga'), 'ga'),
      commitSha: 'a'.repeat(40),
      sha256: '1'.repeat(64),
      bytes: 100,
    },
    beta: {
      metadata: inspectSpec(makeSpec('beta'), 'beta'),
      commitSha: 'b'.repeat(40),
      sha256: '2'.repeat(64),
      bytes: 200,
    },
  };

  const first = createManifest(manifestInput);
  const second = createManifest(manifestInput);

  assert.deepEqual(first, second);
  assert.deepEqual(Object.keys(first), ['schemaVersion', 'ga', 'beta']);
  assert.equal(first.ga.repository, 'meraki/openapi');
  assert.equal(first.ga.branch, 'master');
  assert.equal(first.beta.branch, 'v1-beta');
  assert.equal(first.ga.commitSha, 'a'.repeat(40));
  assert.equal(first.beta.sha256, '2'.repeat(64));
  assert.equal(first.generatedAt, undefined);
});

test('validates local config content and module references while ignoring URLs', () => {
  const root = mkdtempSync(path.join(tmpdir(), 'release-config-'));
  mkdirSync(path.join(root, 'docs'));
  mkdirSync(path.join(root, 'config'));
  mkdirSync(path.join(root, 'snippets'));
  writeFileSync(path.join(root, 'docs', 'guide.md'), '# Guide\n');
  writeFileSync(path.join(root, 'config', 'group.js'), 'module.exports = {};\n');
  writeFileSync(path.join(root, 'config', 'overview.md'), '# Overview\n');

  const configPath = path.join(root, 'config.json');
  writeFileSync(configPath, JSON.stringify({
    items: [
      {
        title: 'Local',
        content: 'docs/guide.md',
        config: {
          overview: { markdownPath: 'config/overview.md' },
          groupBy: { $remoteModule: 'config/group.js' },
          sampleCode: { python: { folder: 'snippets' } },
        },
      },
      { title: 'Remote', content: 'https://example.com/spec.json' },
    ],
  }));

  assert.deepEqual(validateConfigReferences(configPath, root), []);
});

test('reports every missing local config reference together', () => {
  const root = mkdtempSync(path.join(tmpdir(), 'release-config-missing-'));
  const configPath = path.join(root, 'config.json');
  writeFileSync(configPath, JSON.stringify({
    items: [{
      content: 'docs/missing.md',
      config: {
        groupBy: { $remoteModule: 'config/missing.js' },
        sampleCode: { python: { folder: 'snippets/missing' } },
      },
    }],
  }));

  assert.deepEqual(validateConfigReferences(configPath, root), [
    'config/missing.js',
    'docs/missing.md',
    'snippets/missing',
  ]);
});
