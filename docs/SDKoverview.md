The SDKs are built from the Meraki API [OpenAPI specification](https://api.meraki.com/api/v0/openapiSpec) with the aim of simplifying API development. These libraries are open-source and community-supported.

While you can make direct HTTP requests to dashboard API in any programming language or REST API client, using an SDK or client library can make it easier for you to focus on your specific use case, without the overhead of having to write functions to handle the dashboard API calls. The library can also take care of error handling, logging, retries, and other convenient processes and options for you automatically.

### Python Library
The [Python library](pythonLibrary.md) is the recommended option for Meraki administrators who are working with dashboard API and network programmability. This library is available from the [GitHub repository](https://github.com/meraki/dashboard-api-python/) and the [Python Package Index](https://pypi.org/project/meraki/) (PyPI). If using the Python library for dashboard API v1, ensure that a version of the package beginning with **_1._** is installed, such as:

`pip install meraki==1.0.0`