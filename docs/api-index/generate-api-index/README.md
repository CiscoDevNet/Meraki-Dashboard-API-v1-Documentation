# Meraki API Index Generator

Created by Cory Guynn, 2024 /w some help from GPT-4

## Overview

This script automates the generation of the Cisco Meraki API documentation directly from the OpenAPI specification. It fetches the latest API spec and parses it to extract and organize API paths, operations, parameters, and response schemas into a human-readable format.

### Outputs:

- **meraki-api-index.csv:** A CSV file for detailed analysis and import into spreadsheet applications.
- **meraki-api-index.md:** A Markdown file for easy viewing and navigation on platforms that support Markdown.
- **meraki-api-index.html:** An HTML page featuring a filterable table of API operations for easy searching and browsing, enhanced with dynamic filtering and responsive design.

### Features:

- Dynamic HTML table with real-time filtering capability across multiple columns for efficient searching.
- Clear filters button to reset all filters at once and refresh the table view, making navigation intuitive.
- Automatically generated links and formatted code snippets for improved clarity and direct access to the Cisco Meraki developer hub.
- Responsive design ensuring accessibility and usability across different devices and screen sizes.
- Supporting CSS and JavaScript files for styling and functionality are automatically placed in the user's current directory or a separate "output" folder if running in this project folder.

## Usage

1. Run the script using Node.js to fetch the latest API spec and generate the documentation files. This process compiles the OpenAPI specification into accessible formats for various uses.
2. Open the HTML file in a web browser to view the filterable API operation table. This file, along with its supporting CSS and JavaScript files, provides a user-friendly interface for exploring the API operations.
3. Use the CSV file for detailed offline analysis or import into tools like Excel for further data manipulation and examination.
4. The Markdown file serves documentation purposes on platforms like GitHub, offering a markdown-rendered view of the API operations for easy reading.

## Prerequisites

- Node.js installed on the machine running the script.
- Required Node.js modules: `fs`, `node-fetch`, `json2csv`, and `path` for file system operations, web requests, CSV generation, and path manipulations, respectively.

### Running the Script

Execute the script in a terminal or command prompt with Node.js:

```bash
node generate-api-index.js
