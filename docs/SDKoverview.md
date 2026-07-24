# AI Toolkit & SDKs

The Meraki Dashboard API provides AI tooling and SDKs built from the OpenAPI specification to simplify development for both AI-driven agentic workflows and traditional programmatic automation. These tools eliminate boilerplate API integration code and provide higher-level abstractions for common tasks. The SDKs are open source and community supported.

## AI & Agentic Automation

**Meraki MCP Server** connects AI agents and coding assistants like Claude, Cursor, and VS Code directly to the Meraki Dashboard API through the Model Context Protocol (MCP) standard. It enables natural language queries and agentic network automation without writing custom API integration code. Use it to build agents that generate reports, troubleshoot connectivity issues, audit configurations, and answer questions about your network using conversational prompts.

## Programmatic Development

**Python Library** is the preferred SDK for deterministic automation and scripting with the Meraki Dashboard API. It provides access to all API endpoints with built-in features like automatic retry on rate limit errors, pagination support, request logging, and simulation mode for testing changes before applying them. Use it for reliable automation scripts, integration workflows, and infrastructure management tasks where you need predictable, repeatable behavior.

**Go SDK** is a community-supported library that provides Go language bindings for the Meraki Dashboard API. It follows similar patterns to the Python library and is ideal for teams building infrastructure tooling in Go. [View on GitHub](https://github.com/meraki/dashboard-api-go)

**Postman Collection** provides pre-built API request templates for exploring, testing, and learning the Meraki Dashboard API through the Postman interface. It's particularly useful for manual testing, API exploration, and understanding request/response structures before writing code. [Learn more](https://developer.cisco.com/meraki/build/meraki-postman-collection-getting-started/introduction/#dashboard-api-and-postman)
