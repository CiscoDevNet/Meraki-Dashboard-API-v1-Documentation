#!/usr/bin/env node

import { createHash } from 'node:crypto';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const HTTP_METHODS = new Set(['get', 'post', 'put', 'delete', 'patch', 'head', 'options', 'trace']);

export const MINIMUMS = Object.freeze({
  ga: Object.freeze({ paths: 500, operations: 800 }),
  beta: Object.freeze({ paths: 900, operations: 1200 }),
});

function requireChannel(channel) {
  if (!Object.hasOwn(MINIMUMS, channel)) {
    throw new Error(`Unknown specification channel: ${channel}`);
  }
}

export function inspectSpec(spec, channel) {
  requireChannel(channel);
  if (!spec || typeof spec !== 'object' || Array.isArray(spec)) {
    throw new Error('Specification must be a JSON object');
  }
  if (typeof spec.openapi !== 'string' || !spec.openapi.startsWith('3.')) {
    throw new Error('Specification must use OpenAPI 3.x');
  }
  if (typeof spec.info?.version !== 'string' || spec.info.version.trim() === '') {
    throw new Error('Specification must define a non-empty info.version');
  }
  if (!spec.paths || typeof spec.paths !== 'object' || Array.isArray(spec.paths)) {
    throw new Error('Specification must define a paths object');
  }

  const pathEntries = Object.entries(spec.paths);
  const minimum = MINIMUMS[channel];
  if (pathEntries.length < minimum.paths) {
    throw new Error(`${channel} specification must contain at least ${minimum.paths} paths; found ${pathEntries.length}`);
  }

  let operations = 0;
  let betaOperations = 0;
  const missingOperationIds = [];

  for (const [apiPath, pathItem] of pathEntries) {
    if (!pathItem || typeof pathItem !== 'object') continue;
    for (const [method, operation] of Object.entries(pathItem)) {
      if (!HTTP_METHODS.has(method.toLowerCase())) continue;
      operations += 1;
      if (!operation || typeof operation.operationId !== 'string' || operation.operationId.trim() === '') {
        missingOperationIds.push(`${method.toUpperCase()} ${apiPath}`);
      }
      if (String(operation?.['x-release-stage'] ?? '').toLowerCase() === 'beta') {
        betaOperations += 1;
      }
    }
  }

  if (operations < minimum.operations) {
    throw new Error(`${channel} specification must contain at least ${minimum.operations} operations; found ${operations}`);
  }
  if (missingOperationIds.length > 0) {
    throw new Error(`Every operation must define operationId; missing: ${missingOperationIds.slice(0, 5).join(', ')}`);
  }
  if (channel === 'ga' && betaOperations > 0) {
    throw new Error(`GA specification contains ${betaOperations} beta-stage operations`);
  }
  if (channel === 'beta' && betaOperations === 0) {
    throw new Error('Beta specification must contain at least one beta operation');
  }

  return {
    openapi: spec.openapi,
    apiVersion: spec.info.version,
    paths: pathEntries.length,
    operations,
    betaOperations,
  };
}

function manifestEntry(channel, input) {
  const branch = channel === 'ga' ? 'master' : 'v1-beta';
  return {
    repository: 'meraki/openapi',
    branch,
    commitSha: input.commitSha,
    openapi: input.metadata.openapi,
    apiVersion: input.metadata.apiVersion,
    sha256: input.sha256,
    bytes: input.bytes,
    paths: input.metadata.paths,
    operations: input.metadata.operations,
    betaOperations: input.metadata.betaOperations,
  };
}

export function createManifest({ ga, beta }) {
  return {
    schemaVersion: 1,
    ga: manifestEntry('ga', ga),
    beta: manifestEntry('beta', beta),
  };
}

function isRemoteReference(value) {
  return /^https?:\/\//i.test(value);
}

function collectConfigReferences(value, key, references) {
  if (Array.isArray(value)) {
    for (const item of value) collectConfigReferences(item, key, references);
    return;
  }
  if (!value || typeof value !== 'object') return;

  for (const [childKey, childValue] of Object.entries(value)) {
    if (
      typeof childValue === 'string'
      && ['content', '$remoteModule', 'markdownPath', 'folder'].includes(childKey)
      && !isRemoteReference(childValue)
    ) {
      references.add(childValue);
    }
    collectConfigReferences(childValue, childKey, references);
  }
}

export function validateConfigReferences(configPath, repositoryRoot) {
  const config = JSON.parse(readFileSync(configPath, 'utf8'));
  const references = new Set();
  collectConfigReferences(config, undefined, references);

  const missing = [];
  for (const reference of references) {
    const resolved = path.resolve(repositoryRoot, reference);
    const relative = path.relative(path.resolve(repositoryRoot), resolved);
    if (relative.startsWith('..') || path.isAbsolute(relative) || !existsSync(resolved)) {
      missing.push(reference);
    }
  }
  return missing.sort();
}

function parseArguments(args) {
  const options = {};
  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (!argument.startsWith('--') || !args[index + 1]) {
      throw new Error(`Expected --name value argument, received: ${argument}`);
    }
    options[argument.slice(2)] = args[index + 1];
    index += 1;
  }
  return options;
}

function readSpecRecord(filePath, channel, commitSha) {
  const bytes = readFileSync(filePath);
  const spec = JSON.parse(bytes.toString('utf8'));
  return {
    metadata: inspectSpec(spec, channel),
    commitSha,
    sha256: createHash('sha256').update(bytes).digest('hex'),
    bytes: bytes.length,
  };
}

async function runCli(argv) {
  const [command, ...args] = argv;
  if (command === 'validate-spec') {
    const [channel, filePath] = args;
    if (!channel || !filePath) throw new Error('Usage: validate-spec <ga|beta> <file>');
    const spec = JSON.parse(readFileSync(filePath, 'utf8'));
    const metadata = inspectSpec(spec, channel);
    process.stdout.write(`${channel} specification valid: ${metadata.apiVersion}, ${metadata.paths} paths, ${metadata.operations} operations\n`);
    return;
  }

  if (command === 'write-manifest') {
    const options = parseArguments(args);
    for (const required of ['ga', 'ga-sha', 'beta', 'beta-sha', 'output']) {
      if (!options[required]) throw new Error(`write-manifest requires --${required}`);
    }
    const manifest = createManifest({
      ga: readSpecRecord(options.ga, 'ga', options['ga-sha']),
      beta: readSpecRecord(options.beta, 'beta', options['beta-sha']),
    });
    writeFileSync(options.output, `${JSON.stringify(manifest, null, 2)}\n`);
    process.stdout.write(`Wrote release manifest: ${options.output}\n`);
    return;
  }

  if (command === 'validate-config') {
    const [configPath, repositoryRoot = '.'] = args;
    if (!configPath) throw new Error('Usage: validate-config <config.json> [repository-root]');
    const missing = validateConfigReferences(configPath, repositoryRoot);
    if (missing.length > 0) {
      throw new Error(`Missing local config references:\n${missing.map((item) => `- ${item}`).join('\n')}`);
    }
    process.stdout.write(`Config references valid: ${configPath}\n`);
    return;
  }

  throw new Error('Usage: release-tools.mjs <validate-spec|write-manifest|validate-config> ...');
}

const isMain = process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href;
if (isMain) {
  runCli(process.argv.slice(2)).catch((error) => {
    process.stderr.write(`Error: ${error.message}\n`);
    process.exitCode = 1;
  });
}
