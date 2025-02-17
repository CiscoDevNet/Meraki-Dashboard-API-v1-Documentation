## OAuth scopes
OAuth scopes in OAuth 2.0 are used to define and limit the access rights granted to an access token. 

When an integration requests authorization from an administrator, it  must include a list of scopes that the integration seeks access to.  The Meraki Dashboard presents these scopes to the admin during the authorization process, allowing them to approve or deny the request.

Using scopes, OAuth 2.0 offers a flexible and granular method for controlling access to resources. This enables the administrator to make informed decisions regarding the level of access granted to integrations. This mechanism supports the principle of least privilege, enhancing security and privacy.

Meraki provides the following two scopes:
1. **`config`**: This scope grants access to configuration features that influence the operation of the network and the overall network experience. The config scope dictates the end-user network experience and the functioning of Meraki devices, such as VPNs, VLANs, access controls, policies, SSIDs, and sensor names. Note that the `config` scope excludes admin-facing telemetry configurations, which are managed using telemetry scopes.

2. **`telemetry`**: This scope grants access to telemetry data and configurations that do not impact the end-user network experience. They include features like event logs, syslog, bandwidth utilization, client counts, and camera snapshots.

Note: The Meraki scopes can have either "read-only" or "write" permission levels.


| Category              | Read                           | Write                          |
|-----------------------|--------------------------------|--------------------------------|
| **Dashboard**         | dashboard:iam:config:read     | dashboard:iam:config:write     |
|                       | dashboard:iam:telemetry:read  | dashboard:iam:telemetry:write  |
|                       | dashboard:general:config:read | dashboard:general:config:write |
|                       | dashboard:general:telemetry:read | dashboard:general:telemetry:write |
|                       | dashboard:licensing:config:read | dashboard:licensing:config:write |
|                       | dashboard:licensing:telemetry:read | dashboard:licensing:telemetry:write |
| **Network**           | sdwan:config:read             | sdwan:config:write             |
|                       | switch:config:read            | switch:config:write            |
|                       | wireless:config:read          | wireless:config:write          |
|                       | sdwan:telemetry:read          | sdwan:telemetry:write          |
|                       | switch:telemetry:read         | switch:telemetry:write         |
|                       | wireless:telemetry:read       | wireless:telemetry:write       |
| **IoT**               | camera:config:read            | camera:config:write            |
|                       | sensor:config:read            | sensor:config:write            |
|                       | camera:telemetry:read         | camera:telemetry:write         |
|                       | sensor:telemetry:read         | sensor:telemetry:write         |
| **Endpoint Management (SM)** | sm:telemetry:read      | sm:telemetry:write             |
|                       | sm:config:read                | sm:config:write                |


