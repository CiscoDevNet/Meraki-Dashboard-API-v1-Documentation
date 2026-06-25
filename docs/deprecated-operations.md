# Deprecated operations

Listed by deprecation date (newest first).

## 2026 June

### getNetworkSyslogServers

[getNetworkSyslogServers](https://developer.cisco.com/meraki/api-v1/get-network-syslog-servers/) is deprecated in favor of [getOrganizationDevicesSyslogServersByNetwork](https://developer.cisco.com/meraki/api-v1/get-organization-devices-syslog-servers-by-network/) or [getOrganizationDevicesSyslogServersRolesByNetwork](https://developer.cisco.com/meraki/api-v1/get-organization-devices-syslog-servers-roles-by-network/), based on your use case.

#### Replacement operations

##### Use case: reading syslog server configuration for one or more networks

[getOrganizationDevicesSyslogServersByNetwork](https://developer.cisco.com/meraki/api-v1/get-organization-devices-syslog-servers-by-network/) returns syslog server configuration for networks in an organization. Pass the `networkIds[]` query parameter to limit results to specific networks (for example, a single network ID when migrating from `getNetworkSyslogServers`).

This operation is paginated and supports reading syslog configuration for many networks in fewer API calls than issuing one network-scoped request per network.

##### Use case: discovering valid syslog role values before configuring servers

When migrating write workflows, use [getOrganizationDevicesSyslogServersRolesByNetwork](https://developer.cisco.com/meraki/api-v1/get-organization-devices-syslog-servers-roles-by-network/) to list the role `name` and `value` pairs available for each network. The replacement update operation expects role `value` strings (for example, `wirelessEventLog`), not the human-readable titles returned by the deprecated read and update operations (for example, `Wireless event log`).

#### Migration notes

- **OAuth scope:** `dashboard:general:telemetry:read` → `dashboard:general:config:read`
- **Response shape:** the deprecated operation returns `{ "servers": [ ... ] }`. The replacement returns a paginated collection: `{ "items": [ { "network": { "id": "..." }, "servers": [ ... ] } ], "meta": { ... } }`.
- **Server attributes:** replacement responses include `transportProtocol` and `encryption` settings in addition to `host`, `port`, and `roles`.
- **Roles:** replacement responses return per-product-type role values in camelCase (for example, `applianceUrlLog`, `wirelessEventLog`) instead of the deprecated operation's rolled-up human-readable titles (for example, `URLs`, `Wireless event log`).

---

### updateNetworkSyslogServers

[updateNetworkSyslogServers](https://developer.cisco.com/meraki/api-v1/update-network-syslog-servers/) is deprecated in favor of [updateNetworkDevicesSyslogServers](https://developer.cisco.com/meraki/api-v1/update-network-devices-syslog-servers/).

#### Replacement operations

##### Use case: updating syslog server configuration for a network

[updateNetworkDevicesSyslogServers](https://developer.cisco.com/meraki/api-v1/update-network-devices-syslog-servers/) updates syslog servers for a network. It supports the same core inputs (`host`, `port`, `roles`) and adds optional `transportProtocol` and `encryption` settings for encrypted syslog.

This operation supports action batches via the standard Meraki action batch mechanism.

##### Use case: determining which role strings are valid for a network

Before calling the replacement update operation, query [getOrganizationDevicesSyslogServersRolesByNetwork](https://developer.cisco.com/meraki/api-v1/get-organization-devices-syslog-servers-roles-by-network/) and use each role object's `value` property in the update request body.

#### Migration notes

- **OAuth scope:** `dashboard:general:telemetry:write` → `dashboard:general:config:write`
- **Request body:** the `servers` array structure is similar, but `roles` must use camelCase enum values (for example, `["wirelessEventLog", "applianceUrlLog"]`) rather than human-readable titles (for example, `["Wireless event log", "URLs"]`).
- **Response shape:** the deprecated operation returns `{ "servers": [ ... ] }`. The replacement returns `{ "network": { "id": "..." }, "servers": [ ... ] }` with camelCase role values and optional `transportProtocol` / `encryption` fields.
- **Role specificity:** the replacement API models roles per product type (for example, separate wireless and appliance URL log roles). The deprecated API rolled some non-event-log roles into generic titles; callers should map to the appropriate per-product-type role values for their network.

#### Example migration

**Before (deprecated):**

```http
PUT /networks/{networkId}/syslogServers
```

```json
{
  "servers": [
    {
      "host": "1.2.3.4",
      "port": 514,
      "roles": ["Wireless event log", "URLs"]
    }
  ]
}
```

**After (replacement):**

```http
PUT /networks/{networkId}/devices/syslog/servers
```

```json
{
  "servers": [
    {
      "host": "1.2.3.4",
      "port": 514,
      "roles": ["wirelessEventLog", "applianceUrlLog"],
      "transportProtocol": "UDP"
    }
  ]
}
```

To resolve role values for a network programmatically:

```http
GET /organizations/{organizationId}/devices/syslog/servers/roles/byNetwork?networkIds[]={networkId}
```

## 2026 May

### createOrganizationPolicyObject (Request body parameter deprecation)
[createOrganizationPolicyObject](https://developer.cisco.com/meraki/api-v1/create-organization-policy-object/)
`ipAndMask` which is part of the API request body parameter `type` is deprecated and will be removed in a future release. Use `cidr` instead.


## 2024 October

### getNetworkDevices

[getNetworkDevices](https://developer.cisco.com/meraki/api-v1/get-network-devices/) is deprecated in favor of the following operations, based on your use case:

#### Replacement operations

##### Use case: gathering device serial numbers, names, notes, models, MACs, and other hardware metadata, including network assignments

[getOrganizationDevices](https://developer.cisco.com/meraki/api-v1/get-organization-devices/) provides all this information, and offers more query parameter options for filtering the result, including filtering on networkIds.

##### Use case: Polling device uplink and/or management addresses

[getOrganizationDevicesUplinksAddressesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-uplinks-addresses-by-device/) lists the current uplink addresses for devices in an organization.

### getOrganizationDevicesStatuses

[getOrganizationDevicesStatuses](https://developer.cisco.com/meraki/api-v1/get-organization-devices-statuses/) is deprecated in favor of the following operations, based on your use case:

#### Replacement operations

##### Use case: continuous monitoring of device up/down/alerting/dormant status and/or status history

Most of the time, most devices in a network should be in an online status. The operation [getOrganizationDevicesAvailabilitiesChangeHistory](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities-change-history/) provides the most efficient means of gathering status information over time. Thus, by monitoring the change history, you can assert device status by comparing the changes provided by this operation with a one-time snapshot of the statuses provided in [getOrganizationDevicesAvailabilities](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities/). This is substantially more efficient than polling device statuses on an interval, because an empty response in the change history means were no status changes during that time for any device in an entire organization.

##### Use case: one-time poll of device up/down/alerting/dormant status

[getOrganizationDevicesAvailabilities](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities/) provides status information for devices in a more performant manner than the deprecated statuses operation.

##### Use case: Polling device power module status

[getOrganizationDevicesPowerModulesStatusesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-power-modules-statuses-by-device/) lists the most recent status information for power modules in rackmount MX and MS devices that support them.

##### Use case: Polling device uplink and/or management addresses

[getOrganizationDevicesUplinksAddressesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-uplinks-addresses-by-device/) lists the current uplink addresses for devices in an organization.

##### Use case: Polling device provisioning status

[getOrganizationDevicesProvisioningStatuses](https://developer.cisco.com/meraki/api-v1/get-organization-devices-provisioning-statuses/) provides the provisioning status for each device.

## 2024 May

### getNetworkHealthAlerts

[getNetworkHealthAlerts](https://developer.cisco.com/meraki/api-v1/get-network-health-alerts) is deprecated in favor of [getOrganizationAssuranceAlerts](https://developer.cisco.com/meraki/api-v1/get-organization-assurance-alerts) which offers more extensive filtering capabilities

## 2024 March

### Camera analytics

The following operations are deprecated in favor of the newer [boundaries](https://developer.cisco.com/meraki/api-v1/search/?q=boundaries) operations.

* [getDeviceCameraAnalyticsLive](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-live/)
* [getDeviceCameraAnalyticsOverview](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-overview/)
* [getDeviceCameraAnalyticsRecent](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-recent/)
* [getDeviceCameraAnalyticsZones](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-zones/)
* [getDeviceCameraAnalyticsZoneHistory](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-zone-history/)

## 2023 August

### claimIntoOrganization

[claimIntoOrganization](https://developer.cisco.com/meraki/api-v1/claim-into-organization) is deprecated in favor of [claimIntoOrganizationInventory](https://developer.cisco.com/meraki/api-v1/claim-into-organization-inventory), which offers full feature parity.
