# Meraki Dashboard API Python Library

The Meraki Dashboard API Python library provides all current Meraki [Dashboard API](https://developer.cisco.com/docs/meraki-api-v1) calls to interface with the Cisco Meraki cloud-managed platform. The library is supported on Python 3.6 or above, and you can install it via [PyPI](https://pypi.org/project/meraki/):

    pip install meraki

## Features

While you can make direct HTTP requests to dashboard API in any programming language or REST API client, using a client library can make it easier for you to focus on your specific use case, without the overhead of having to write functions to handle the dashboard API calls. The Python library can also take care of error handling, logging, retries, and other convenient processes and options for you automatically.

* Support for all API endpoints, as it uses the [OpenAPI specification](https://api.meraki.com/api/v1/openapiSpec) to generate source code
* Log all API requests made to a local file as well as on-screen console
* Automatic retries upon 429 rate limit errors, using the [`Retry-After` field](https://developer.cisco.com/docs/meraki-api-v1/#!rate-limit) within response headers
* Get all (or a specified number of) pages of data with built-in pagination control
* Tweak settings such as maximum retries, certificate path, suppress logging, and other options
* Simulate POST/PUT/DELETE calls to preview first, so that network configuration does not get changed
* Includes the legacy module's (version 0.34 and prior) functions for backward compatibility

## Setup

1. Enable API access in your Meraki dashboard organization and obtain an API key ([instructions](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API))

2. Keep your API key safe and secure, as it is similar to a password for your dashboard. If publishing your Python code to a wider audience, please research secure handling of API keys.

3. Install the latest version of [Python 3](ttps://wiki.python.org/moin/BeginnersGuide/NonProgrammers)

4. Use _pip_ (or an alternative such as _easy_install_) to install the library:
    * `pip install meraki`
    * If you have both Python3 and Python2 installed, you may need to use `pip3 install meraki`
    * If _meraki_ was previously installed, you can upgrade with `pip install --upgrade meraki` or `pip3 install --upgrade meraki`
    * You can specify the version of the library, for example `pip install meraki==0.100.2` for v0 or `pip install meraki==1.0.0b1` for v1

## Usage
1. Export your API key as an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), for example:

    ```shell
    export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
    ```

2. Alternatively, define your API key as a variable in your source code; this method is not recommended due to its inherent insecurity.

3. Single line of code to import and use the library goes at the top of your script:

    ```python
    import meraki
    ```

4. Instantiate the client (API consumer class), optionally specifying any of the parameters available to set:

    ```python
    dashboard = meraki.DashboardAPI()
    ```

5. Make dashboard API calls in your source code, using the format _client.scope.operation_, where _client_ is the name you defined in the previous step (**dashboard** above), _scope_ is the corresponding scope that represents the first tag from the OpenAPI spec, and _operation_ is the operation of the API endpoint. For example, to make a call to get the list of organizations accessible by the API key defined in step 1, use this function call:

    ```python
    my_orgs = dashboard.organizations.getOrganizations()
    ```

6. If you were using this module versions 0.34 and prior, that file's functions are included in the _legacy.py_ file, and you can adapt your existing scripts by replacing their `from meraki import meraki` line to `import meraki`

For a full working script that demos this library, please see and run the **org_wide_clients_v1.py** file included (in **examples** folder). That code collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET endpoints are called, and the data is written to local CSV output files.