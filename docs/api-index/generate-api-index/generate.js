/**
 * Meraki API Index Generator
 * 
 * Created by Cory Guynn, 2024
 * /w some help from GPT4
 *
 * This script automates the generation of the Cisco Meraki API documentation directly from the OpenAPI specification.
 * It fetches the latest API spec and parses it to extract and organize API paths, operations, parameters, and
 * response schemas into a human-readable format.
 *
 * Outputs:
 * - meraki-api-index.csv: A CSV file for detailed analysis and import into spreadsheet applications.
 * - meraki-api-index.md: A Markdown file for easy viewing and navigation on platforms that support Markdown.
 * - meraki-api-index.html: An HTML page featuring a filterable table of API operations for easy searching and browsing.
 *
 * Features:
 * - Dynamic HTML table with real-time filtering capability across multiple columns.
 * - Clear filters button to reset all filters at once and refresh the table view.
 * - Automatically generated links and formatted code snippets for improved clarity.
 * 
 * Usage:
 * 1. Run the script using Node.js to fetch the latest API spec and generate the documentation files.
 * 2. Open the HTML file in a web browser to view the filterable API operation table.
 * 3. Use the CSV file for detailed offline analysis or import into tools like Excel.
 * 4. The Markdown file can be used for documentation purposes on platforms like GitHub.
 *
 * Prerequisites:
 * - Node.js installed on the machine running the script.
 * - Required Node.js modules: fs, node-fetch, json2csv.
 *
 */


const fs = require('fs');
const path = require('path');
const fetch = require('node-fetch');
const { parse } = require('json2csv');

// Constants
const DEFAULT_API_SPEC_URL = 'https://raw.githubusercontent.com/meraki/openapi/v1-beta/openapi/spec3.json';

const CSV_FILENAME = 'meraki-api-index.csv';
const MD_FILENAME = 'meraki-api-index.md';
const HTML_FILENAME = 'meraki-api-index.html';

// Helper Functions

// Determine if input is a URL
const isUrl = (input) => {
    try {
        new URL(input);
        return true;
    } catch (e) {
        return false;
    }
};

// Dynamically fetch or read the OpenAPI specification
async function fetchOpenAPISpec(customSpecPath) {
    if (customSpecPath && isUrl(customSpecPath)) {
        // Fetch the spec from a URL
        const response = await fetch(customSpecPath);
        return response.json();
    } else if (customSpecPath && fs.existsSync(customSpecPath)) {
        // Read the spec from a local file
        const spec = fs.readFileSync(customSpecPath, 'utf8');
        return JSON.parse(spec);
    } else {
        // Use the default URL
        const response = await fetch(DEFAULT_API_SPEC_URL);
        return response.json();
    }
}

// function toKebabCase(str) {
//     return str.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
// }

function toKebabCase(str) {
    return str
        .replace(/([a-z])([A-Z])/g, '$1-$2') // Handle camelCase
        .replace(/([0-9]+)/g, '-$1-') // Handle numbers
        .toLowerCase();
}

// Parse CLI args for operationId filtering
function parseOperationIdArgs(args) {
    const result = new Set();
    let filePath;

    for (let i = 0; i < args.length; i++) {
        const arg = args[i];
        if (arg === '--ops' && args[i + 1]) {
            args[i + 1].split(/[\s,]+/).filter(Boolean).forEach(op => result.add(op.trim().toLowerCase()));
            i++;
        } else if (arg === '--ops-file' && args[i + 1]) {
            filePath = args[i + 1];
            i++;
        }
    }

    if (filePath && fs.existsSync(filePath)) {
        const fileOps = fs.readFileSync(filePath, 'utf8').split(/[\s,]+/).filter(Boolean);
        fileOps.forEach(op => result.add(op.trim().toLowerCase()));
    }

    return {
        operationIdsFilter: result.size > 0 ? result : null,
        remainingArgs: args
    };
}

// Parses the Swagger paths from the specification into reportable formats.
function parseSwaggerPaths(spec, operationIdsFilter) {
    let csvReport = [];
    let markdownReport = [];
    Object.keys(spec.paths).forEach(path => {
        Object.keys(spec.paths[path]).forEach(method => {
            const operation = spec.paths[path][method];
            const operationId = operation.operationId;
            if (!operationId) {
                return;
            }
            if (operationIdsFilter && !operationIdsFilter.has(operationId.toLowerCase())) {
                return;
            }
            let releaseStage = operation[`x-release-stage`] || "GA";
            if (operation.deprecated) {
                releaseStage = "deprecated"
            }
            const summary = operation.summary;
            const apiDocsUrl = `https://developer.cisco.com/meraki/api-v1/${toKebabCase(operationId)}/`;
            const methodPath = `${method.toUpperCase()} ${path}`;
            const summaryText = releaseStage !== "GA" ? `${summary} (${releaseStage.toUpperCase()})` : summary;
            const summaryLink = `[${summaryText}](${apiDocsUrl})`;
            const responseParams = extractResponseSchemas(operation.responses);
            const pathParams = operation.parameters ? operation.parameters.map(p => p.name).join(", ") : '';
            const requestBodyParams = extractRequestBodyProperties(operation.requestBody);
            const tagsArrayRaw = operation.tags || [];
            const tags = tagsArrayRaw.join(", ");
            const pythonOperation = tagsArrayRaw.length > 0 ? `${tagsArrayRaw[0]}.${operationId}` : operationId;

            const tagsArray = tags.split(', ').filter(Boolean);
            const boldFirstTag = tagsArray.length > 0 ? `<b>${tagsArray.shift()}</b>` : '';
            const formattedTags = tagsArray.length > 0 ? `, ${tagsArray.join(', ')}` : '';
            const formattedTagsWithBoldFirst = `${boldFirstTag}${formattedTags}`;

            // Extract OAuth scopes
            const oauthScopes = operation.security
                ?.find(sec => sec.oauth2)?.oauth2
                ?.join(', ') || '';

            csvReport.push({
                releaseStage, operationId, summary, apiDocsUrl, method, path, 
                pathParams, requestBodyParams, responseParams, tags, 
                pythonOperation, oauthScopes  // Added oauthScopes
            });

            markdownReport.push({
                releaseStage,
                summary,
                apiDocsUrl,
                method,
                path,
                tags,
                pythonOperation,
                oauthScopes,
                operationId,
                Operation: `${methodPath} <br /> ${summaryLink}<br><label style="font-size:small; padding-left:20px;"><i>${formattedTagsWithBoldFirst}</i></label><div style="padding:5px"> >  \`${operationId}\` </div> `,
                "Request Parameters": ` \`${requestBodyParams}\` `,
                "Path Parameters": ` \`${pathParams}\` `,
                "Response Parameters": ` \`${responseParams}\` `,
                "OAuth Scopes": ` \`${oauthScopes}\` `  // Added OAuth Scopes column
            });
        });
    });
    return { markdownReport, csvReport };
}


function extractPropertiesFromSchema(schema, properties = []) {
    if (schema.type === 'object' && schema.properties) {
        Object.keys(schema.properties).forEach(key => {
            // Add the property name
            properties.push(key);
            // Recursively extract nested properties
            extractPropertiesFromSchema(schema.properties[key], properties);
        });
    } else if (schema.type === 'array' && schema.items) {
        extractPropertiesFromSchema(schema.items, properties);
    }
    return properties;
}

// Extracts all response schema property names
function extractResponseSchemas(responses) {
    let propertiesSet = new Set();
    Object.values(responses).forEach(response => {
        if (response.content && response.content['application/json'] && response.content['application/json'].schema) {
            extractPropertiesFromSchema(response.content['application/json'].schema).forEach(prop => {
                propertiesSet.add(prop);
            });
        }
    });
    return Array.from(propertiesSet).sort().join(", ");
}

// Extracts request body schema property names function to handle nested properties.
function extractRequestBodyProperties(requestBody) {
    let propertiesSet = new Set();
    if (requestBody && requestBody.content && requestBody.content['application/json'] && requestBody.content['application/json'].schema) {
        let schema = requestBody.content['application/json'].schema;
        // Use the recursive function to extract properties
        extractPropertiesFromSchema(schema).forEach(prop => {
            propertiesSet.add(prop);
        });
    }
    return Array.from(propertiesSet).sort().join(", ");
}


// Converts data to a Markdown table.
function toMarkdownTable(data, fields) {
    const header = fields.join(' | ');
    const separator = fields.map(() => '---').join(' | ');
    const body = data.map(row => fields.map(field => row[field] || '').join(' | ')).join('\n');
    return `| ${header} |\n| ${separator} |\n| ${body} |`;
}

function markdownToHtmlTable(data, fields, apiVersion, totalCount) {
    // Header with combined titles and filter inputs
    let headerHtml = `<thead><tr><th style="width:32px; text-align:left;">
            <button class="icon-btn" title="Clear filters" onclick="clearAllFilters()">✕</button>
        </th>${fields.map(field => {
        const idx = fields.indexOf(field);
        if (field === "Operation") {
            return `
        <th>
            <div style="display:flex; align-items:center; justify-content:space-between; gap:6px;">
                <p style="margin:0;">${field}</p>
            </div>
            <div style="display:flex; gap:6px; align-items:center; margin-top:4px;">
                <input type="text" onkeyup="filterTable(this, ${idx})" placeholder="Filter...">
                <button class="icon-btn" id="opFilterToggle" title="Advanced operation filter" onclick="toggleOpFilterPanel()">▼</button>
            </div>
            <div id="opFilterPanel" style="display:none; margin-top:6px;">
                <label for="opFilterInput"><b>Filter multiple operations</b> (comma/space/newline)</label><br/>
                <textarea id="opFilterInput" rows="3" style="width:100%; max-width:480px;" placeholder="getOrganizations, getOrganizationNetworks, getOrganizationDevices, ..."></textarea>
                <div style="margin-top:6px; display:flex; gap:8px; flex-wrap:wrap; align-items:center;">
                    <button class="apply-op-filter" onclick="applyOpFilter()">Apply</button>
                    <button class="icon-btn" title="Clear operation filter" onclick="clearOpFilter()">✕</button>
                </div>
            </div>
        </th>`;
        }
        return `
        <th>
            <p style="margin:5px 0px">${field}</p>
            <input type="text" onkeyup="filterTable(this, ${idx})" placeholder="Filter...">
        </th>`;
    }).join('')}</tr></thead>`;

    // Body rows
    let bodyHtml = `<tbody>${data.map(row => {
        const attrs = [
            ['operation-id', row.operationId || ''],
            ['release-stage', row.releaseStage || ''],
            ['summary', row.summary || ''],
            ['api-docs-url', row.apiDocsUrl || ''],
            ['method', row.method || ''],
            ['path', row.path || ''],
            ['path-params', row["Path Parameters"] ? row["Path Parameters"].replace(/`/g, '') : ''],
            ['request-body-params', row["Request Parameters"] ? row["Request Parameters"].replace(/`/g, '') : ''],
            ['response-params', row["Response Parameters"] ? row["Response Parameters"].replace(/`/g, '') : ''],
            ['tags', row.tags || ''],
            ['python-operation', row.pythonOperation || ''],
            ['oauth-scopes', row.oauthScopes || '']
        ].map(([k, v]) => `data-${k}="${(v || '').replace(/"/g, '&quot;')}"`).join(' ');
        return `
        <tr ${attrs}><td></td>${fields.map(field => {
        let cellData = row[field] || '';
        cellData = cellData.replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        return `<td>${cellData}</td>`;
    }).join('')}</tr>`;
    }).join('')}</tbody>`;

    // Full table
    return `<div class="table-container"><table class="scrollable-table">${headerHtml}${bodyHtml}</table></div>`;
}



async function generateData() {
    // Capture custom spec path or URL from CLI arguments
    const rawArgs = process.argv.slice(2);
    const customSpecPath = rawArgs[0] && !rawArgs[0].startsWith('--') ? rawArgs.shift() : undefined;
    const { operationIdsFilter } = parseOperationIdArgs(rawArgs);

    const targetDirectory = setupTargetDirectoryAndCopyFiles(); // Set up directory and copy supporting files

    try {
        // Pass the custom or default spec URL/path to fetchOpenAPISpec
        const spec = await fetchOpenAPISpec(customSpecPath || DEFAULT_API_SPEC_URL);
        const { markdownReport, csvReport } = parseSwaggerPaths(spec, operationIdsFilter);
        const totalCount = csvReport.length;
        const methodCounts = csvReport.reduce((acc, row) => {
            const m = (row.method || '').toUpperCase();
            if (m) acc[m] = (acc[m] || 0) + 1;
            return acc;
        }, {});
        const apiVersion = spec.info.version;
        const fields = ["Operation", "Path Parameters", "Request Parameters", "Response Parameters", "OAuth Scopes"];

        // Define filenames with paths
        const csvFilePath = path.join(targetDirectory, CSV_FILENAME);
        const mdFilePath = path.join(targetDirectory, MD_FILENAME);
        const htmlFilePath = path.join(targetDirectory, HTML_FILENAME);

        // Write CSV File
        const csvFields = csvReport.length > 0
            ? Object.keys(csvReport[0])
            : ["releaseStage", "operationId", "summary", "apiDocsUrl", "method", "path", "pathParams", "requestBodyParams", "responseParams", "tags", "pythonOperation", "oauthScopes"];
        const csvContent = parse(csvReport, { fields: csvFields });
        fs.writeFileSync(csvFilePath, csvContent);
        console.log(`CSV file has been generated successfully: ${csvFilePath}`);

        // Write Markdown File
        const markdownTable = toMarkdownTable(markdownReport, fields);
        const markdownContent = `## Meraki API Specification - Version ${apiVersion}\n\n[Download CSV](${CSV_FILENAME})\n\n${markdownTable}`;
        fs.writeFileSync(mdFilePath, markdownContent);
        console.log(`Markdown file has been generated successfully: ${mdFilePath}`);

        // Write HTML File
        const htmlContent = `
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API Index</title>
            <link rel="stylesheet" type="text/css" href="api-index-html.styles.css" /> 
            <script src="api-index-html.script.js"></script>
        </head>
        <body>     
            
        
               <!-- <h1>API Index</h1> -->
               <div style="padding:10px; display:flex; flex-wrap:wrap; gap:12px; align-items:center; border-bottom:1px solid #ccc;">
                    <div style="display:flex; gap:12px; align-items:center; flex:1 1 auto; flex-wrap:wrap;">
                        <span><b>API v${apiVersion}</b></span>
                        <span id="totalCount">Total operations: ${totalCount}</span>
                        <span id="methodCounts" style="opacity:0.75; font-size: 0.9em;">GET: ${methodCounts.GET || 0} | POST: ${methodCounts.POST || 0} | PUT: ${methodCounts.PUT || 0} | DELETE: ${methodCounts.DELETE || 0}</span>
                    </div>
                    <div style="display:flex; gap:8px; align-items:center; justify-content:flex-end; flex:1 1 auto;">
                        <button class="toolbar-btn" onclick="exportFilteredCsv()">Download filtered CSV</button>
                        <button class="toolbar-btn" onclick="window.location.href='${CSV_FILENAME}'">Download full CSV</button>
                        <button class="toolbar-btn" onclick="window.location.href='https://github.com/meraki/openapi'">OpenAPI Specification</button>
                    </div>
               </div>
               ${markdownToHtmlTable(markdownReport, fields, apiVersion, totalCount)}

        </body>
        </html>
    `;
        fs.writeFileSync(htmlFilePath, htmlContent);
        console.log(`HTML file has been generated successfully: ${htmlFilePath}`);
    } catch (error) {
        console.error('An error occurred:', error);
    }
}
function setupTargetDirectoryAndCopyFiles() {
    const currentDirectory = process.cwd();
    const scriptDirectory = __dirname;

    let targetDirectory = currentDirectory;
    // Check if the script is run in its own directory
    if (currentDirectory === scriptDirectory) {
        // Define the output directory
        const outputDirectory = path.join(currentDirectory, 'output');
        // Check if the "output" directory exists, if not, create it
        if (!fs.existsSync(outputDirectory)) {
            fs.mkdirSync(outputDirectory);
        }
        targetDirectory = outputDirectory;
    }

    // Define the paths for the supporting files
    const supportingFiles = [
        'api-index-html.script.js',
        'api-index-html.styles.css',
    ];

    // Copy supporting files to the target directory
    supportingFiles.forEach(file => {
        const sourcePath = path.join(scriptDirectory, 'src', file);
        const destinationPath = path.join(targetDirectory, file);
        fs.copyFileSync(sourcePath, destinationPath);
    });

    // Return the target directory for further use
    return targetDirectory;
}

generateData();
