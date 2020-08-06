The [Meraki OpenAPI spec](https://github.com/meraki/openapi), is THE SOURCE OF TRUTH, defining the publicly supported state of the Dashboard API.

Once a major API version is released, we will make only backwards-compatible (minor) changes to it. 

These changes include:

* Adding new API resources
* Adding new optional request parameters to existing API methods
* Adding new properties to existing API responses
* Changing the order of properties in existing API responses


### V1 Release Schedule

|   |Week 1   |Week 2   |Week 3   |Week 4   |
|---|---|---|---|---|
|Month 1   |1.0.0   |   |   |   |
|  |1.0.0-beta   |1.0.0-beta.1   |1.0.0-beta.2   |1.0.0-beta.3   |
|Month 2   |1.1.0   |   |   |   |
|  |1.1.0-beta   |1.1.0-beta.1   |1.1.0-beta.2   |1.1.0-beta.3   |
|Month 3    |1.2.0   |   |   |   |
|  |1.2.0-beta   |1.2.0-beta.1   |1.2.0-beta.2   |1.2.0-beta.3   |

Any API changes will be described in detail via the [Changelog](https://developer.cisco.com/meraki/whats-new/)

## V0 Deprecation & Sunset

Now that v1 is the new default version, we will be retiring v0 over time. 

There are two phases to this process:

- A "Deprecation" response header informing you that this is no longer the preferred version. It will remain operational and supported, yet we encourage you to migrate to the newest version.


- A "Sunset" response header informing you when this version is no longer supported and may become unresponsive.


### Key Dates

> Deprecation:  **August 5th, 2020**

> Sunset:       **February 5th, 2022**



