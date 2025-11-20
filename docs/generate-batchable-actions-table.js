#!/usr/bin/env node

/**
 * Script to generate a markdown table of Meraki batchable actions
 * from the OpenAPI spec.
 * 
 * Usage:
 *   node generate-batchable-actions-table.js [spec-url-or-path] [output-file]
 * 
 * Examples:
 *   node generate-batchable-actions-table.js
 *   node generate-batchable-actions-table.js https://raw.githubusercontent.com/meraki/openapi/master/openapi/spec3.json
 *   node generate-batchable-actions-table.js ./spec3.json
 *   node generate-batchable-actions-table.js ./spec3.json custom-output.md
 */

const fs = require('fs');
const https = require('https');
const http = require('http');
const { URL } = require('url');

const DEFAULT_SPEC_URL = 'https://raw.githubusercontent.com/meraki/openapi/master/openapi/spec3.json';
const DEFAULT_OUTPUT_FILE = 'ActionBatchesResources.md';

/**
 * Fetch JSON from URL
 */
function fetchJson(url) {
  return new Promise((resolve, reject) => {
    const parsedUrl = new URL(url);
    const client = parsedUrl.protocol === 'https:' ? https : http;
    
    client.get(url, (res) => {
      if (res.statusCode !== 200) {
        reject(new Error(`Failed to fetch: ${res.statusCode} ${res.statusMessage}`));
        return;
      }
      
      let data = '';
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (err) {
          reject(new Error(`Failed to parse JSON: ${err.message}`));
        }
      });
    }).on('error', reject);
  });
}

/**
 * Read JSON from file
 */
function readJsonFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(content);
  } catch (err) {
    throw new Error(`Failed to read file ${filePath}: ${err.message}`);
  }
}

/**
 * Escape markdown special characters in table cells
 */
function escapeMarkdown(text) {
  if (!text) return '';
  return String(text)
    .replace(/\|/g, '\\|')
    .replace(/\n/g, ' ');
}

/**
 * Generate markdown table from batchable actions
 */
function generateMarkdownTable(actions) {
  if (!Array.isArray(actions) || actions.length === 0) {
    return 'No batchable actions found.';
  }

  // Table header
  let table = '| Group | Summary | Resource | Operation |\n';
  table += '|-------|---------|----------|-----------|\n';

  // Table rows
  for (const action of actions) {
    const group = escapeMarkdown(action.group || '');
    const summary = escapeMarkdown(action.summary || '');
    const resource = escapeMarkdown(action.resource || '');
    const operation = escapeMarkdown(action.operation || '');
    
    table += `| ${group} | ${summary} | ${resource} | ${operation} |\n`;
  }

  return table;
}

/**
 * Main function
 */
async function main() {
  const specPath = process.argv[2] || DEFAULT_SPEC_URL;
  const outputFile = process.argv[3] || DEFAULT_OUTPUT_FILE;
  
  let spec;
  
  try {
    // Check if it's a file path or URL
    if (specPath.startsWith('http://') || specPath.startsWith('https://')) {
      console.error(`Fetching spec from: ${specPath}`);
      spec = await fetchJson(specPath);
    } else {
      console.error(`Reading spec from: ${specPath}`);
      spec = readJsonFile(specPath);
    }
    
    // Extract batchable actions
    const batchableActions = spec['x-batchable-actions'];
    
    if (!batchableActions) {
      console.error('Error: "x-batchable-actions" not found in spec');
      process.exit(1);
    }
    
    // Generate markdown table
    const table = generateMarkdownTable(batchableActions);
    
    // Write to file
    fs.writeFileSync(outputFile, table, 'utf8');
    console.error(`✓ Generated ${batchableActions.length} batchable actions`);
    console.error(`✓ Written to: ${outputFile}`);
    
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
}

// Run the script
if (require.main === module) {
  main();
}

module.exports = { generateMarkdownTable, fetchJson, readJsonFile };

