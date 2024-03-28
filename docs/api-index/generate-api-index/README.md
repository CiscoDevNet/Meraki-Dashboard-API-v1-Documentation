# Meraki API Index Generator

Created by Cory Guynn, 2024

## Overview

This tool automates the creation of Cisco Meraki [API Index](https://developer.cisco.com/meraki/api/api-index/) documentation from an OpenAPI specification. It fetches the most recent API release and organizes it into human-readable formats.

## Outputs:

- **meraki-api-index.csv**: A CSV file for spreadsheet applications.
- **meraki-api-index.md**: A Markdown file for GitHub and other platforms.
- **meraki-api-index.html**: A filterable HTML page of API operations.

## Features:

- Real-time filtering of API operations in an HTML table.
- Links to the Meraki developer hub.
- CSV file for easy data science


## Usage

1. Run `generate.js` with Node.js to create the files.
2. Open `meraki-api-index.html` in a browser to view the API table.
3. Utilize `meraki-api-index.csv` for offline analysis in Excel or similar.
4. Employ `meraki-api-index.md` for online viewing on platforms like GitHub.

## Prerequisites:

- Node.js installed on your machine.
- Modules: `fs`, `node-fetch`, `json2csv`, `path`.

## Running the Script:

In your terminal or command prompt with Node.js:

```bash
node generate.js
```

To use a local or custom spec:

```
node generate.js /path/to/local/spec.json
node generate.js https://customspec.com/spec.json
```

### Output Directory:
Running in its directory, outputs go to `output`.
Running elsewhere, outputs stay in the current directory.

## License:
MIT License