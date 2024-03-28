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
    if (isUrl(customSpecPath)) {
        // Fetch the spec from a URL
        const response = await fetch(customSpecPath);
        return response.json();
    } else if (fs.existsSync(customSpecPath)) {
        // Read the spec from a local file
        const spec = fs.readFileSync(customSpecPath, 'utf8');
        return JSON.parse(spec);
    } else {
        // Use the default URL
        const response = await fetch(DEFAULT_API_SPEC_URL);
        return response.json();
    }
}

function toKebabCase(str) {
    return str.replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
}

// Parses the Swagger paths from the specification into reportable formats.
function parseSwaggerPaths(spec) {
    let csvReport = [];
    let markdownReport = [];
    Object.keys(spec.paths).forEach(path => {
        Object.keys(spec.paths[path]).forEach(method => {
            const operation = spec.paths[path][method];
            const operationId = operation.operationId;
            let releaseStage = operation[`x-release-stage`] || "GA";
            if (operation.deprecated) {
                releaseStage = "deprecated"
            }
            const summary = operation.summary;
            const apiDocsUrl = `https://developer.cisco.com/meraki/api/${toKebabCase(operationId)}/`;
            const methodPath = `${method.toUpperCase()} ${path}`;
            const summaryText = releaseStage !== "GA" ? `${summary} (${releaseStage.toUpperCase()})` : summary;
            const summaryLink = `[${summaryText}](${apiDocsUrl})`;
            const responseParams = extractResponseSchemas(operation.responses);
            const pathParams = operation.parameters ? operation.parameters.map(p => p.name).join(", ") : '';
            const requestBodyParams = extractRequestBodyProperties(operation.requestBody);
            const tags = operation.tags.join(", ");
            const pythonOperation = `${operation.tags[0]}.${operationId}`;

            const tagsArray = tags.split(', ');
            const boldFirstTag = `<b>${tagsArray.shift()}</b>`; // Make the first tag bold
            const formattedTags = tagsArray.length > 0 ? `, ${tagsArray.join(', ')}` : '';
            const formattedTagsWithBoldFirst = `${boldFirstTag}${formattedTags}`;


            csvReport.push({
                releaseStage, operationId, summary, apiDocsUrl, method, path, pathParams, requestBodyParams, responseParams, tags, pythonOperation
            });

            markdownReport.push({
                Operation: `${methodPath} <br /> ${summaryLink}<br><label style="font-size:small; padding-left:20px;"><i>${formattedTagsWithBoldFirst}</i></label><div style="padding:5px"> >  \`${operationId}\` </div> `,
                "Request Parameters": ` \`${requestBodyParams}\` `,
                "Path Parameters": ` \`${pathParams}\` `,
                "Response Parameters": ` \`${responseParams}\` `
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

function markdownToHtmlTable(data, fields) {
    // Header with combined titles and filter inputs
    let headerHtml = `<thead><tr>${fields.map(field => `
        <th>
            <p style="margin:5px 0px">${field}</p>
            <input type="text" onkeyup="filterTable(this, ${fields.indexOf(field)})" placeholder="Filter...">
        </th>
    `).join('')}</tr></thead>`;

    // Body rows
    let bodyHtml = `<tbody>${data.map(row => `
        <tr>${fields.map(field => {
        let cellData = row[field] || '';
        cellData = cellData.replace(/`([^`]+)`/g, '<code>$1</code>')
            .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
        return `<td>${cellData}</td>`;
    }).join('')}</tr>
    `).join('')}</tbody>`;

    // Full table
    return `<div class="table-container"><table class="scrollable-table">${headerHtml}${bodyHtml}</table></div>`;
}



async function generateData() {
    // Capture custom spec path or URL from CLI arguments
    const customSpecPath = process.argv[2];

    const targetDirectory = setupTargetDirectoryAndCopyFiles(); // Set up directory and copy supporting files

    try {
        // Pass the custom or default spec URL/path to fetchOpenAPISpec
        const spec = await fetchOpenAPISpec(customSpecPath || DEFAULT_API_SPEC_URL);
        const { markdownReport, csvReport } = parseSwaggerPaths(spec);
        const apiVersion = spec.info.version;
        const fields = ["Operation", "Path Parameters", "Request Parameters", "Response Parameters"];

        // Define filenames with paths
        const csvFilePath = path.join(targetDirectory, CSV_FILENAME);
        const mdFilePath = path.join(targetDirectory, MD_FILENAME);
        const htmlFilePath = path.join(targetDirectory, HTML_FILENAME);

        // Write CSV File
        const csvContent = parse(csvReport, { fields: Object.keys(csvReport[0]) });
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
               <div style="padding-left:10px">
                <p>
                    <button class="clear-filters" onclick="clearFilters()">Clear Filters</button> <a style="padding-left:30px" href="${CSV_FILENAME}" class="export" >Download CSV </a> <a style="padding-left:30px" href="https://github.com/meraki/openapi" class="export" >OpenAPI Specification</a></div>
                </p>
               </div>
           
                ${markdownToHtmlTable(markdownReport, fields)}

                
                <p style="padding-left:30px"><i> API v${apiVersion}</i></p>
           
            
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