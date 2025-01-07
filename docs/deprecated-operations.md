# Deprecated operations

Listed by deprecation date (newest first).

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
