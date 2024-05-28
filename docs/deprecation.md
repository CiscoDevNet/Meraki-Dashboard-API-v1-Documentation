# Deprecation

## Overview

As necessary, Meraki may deprecate API versions or operations over time. After an announced deprecation period, the versions or operations marked as deprecated will be sunset.

This means that Meraki may offer newer, more performant alternatives over time to satisfy developer use cases currently met in whole or in part by existing operations and/or versions. When this happens, Meraki will:

1. Mark the deprecated operation or version as deprecated in the OAS.
2. Provide documented alternatives to the operation or version.

We encourage developers to take advantage of the improvements and migrate their applications to the latest offerings. In any case, it is the developer's responsibility to migrate their applications to non-deprecated offerings prior to the sunset date for that offering.

## Definitions

### Version vs. revision

An API version, also known as a _major_ version, identifies a grouped set of API resources and operations. At Meraki, we use simple integers for versions, e.g. "v1". Today, these are released infrequently, and Meraki only has "v1".

An API revision, also known as a _minor_ version, identifies non-breaking improvements to an API, such as the addition of new attributes or capabilities to extend existing operations within a major version. In most if not all cases, changes between revisions within a single version are additive and otherwise transparent to clients built on older revisions of that version. Today, Meraki names a new revision every month, summarizing all the changes that have been released since the last named revision. A Meraki API revision name takes the format of "1.50.0", where "1" is the version, "50" is the ID of the "minor version", and "0" is the patch version. Note that the terms 'major' and 'minor' versions are commonly used in the industry in the context of semantic versioning; for our purposes, this guide will refer to major versions as versions and minor versions as revisions.

### Deprecation vs. sunsetting

Deprecating is the act of marking a whole API version, or a specific API operation within a version, as deprecated, and informing the community about the intention to sunset it at some point in the future. During the deprecation period, backwards compatibility can be expected until the operation or version is sunset. However, maintaining compatibility does not ensure the deprecated operation's suitability or reliability for any uses beyond its intended purpose.

Sunsetting is the act of removing support for a single API operation or a whole version, after the deprecation period has elapsed. An operation or version is sunset after the deprecation period has elapsed.

## Deprecated operations

### Device operations

#### claimIntoOrganization

[claimIntoOrganization](https://developer.cisco.com/meraki/api-v1/claim-into-organization) is deprecated in favor of [claimIntoOrganizationInventory](https://developer.cisco.com/meraki/api-v1/claim-into-organization-inventory), which offers full feature parity.

#### getOrganizationDevicesStatuses

[getOrganizationDevicesStatuses](https://developer.cisco.com/meraki/api-v1/get-organization-devices-statuses/) is deprecated in favor of the following operations, based on your use case:

##### Use case: continuous monitoring of device up/down/alerting/dormant status and/or status history

Most of the time, most devices in a network should be in an online status. The operation [getOrganizationDevicesAvailabilitiesChangeHistory](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities-change-history/) provides the most efficient means of gathering status information over time. Thus, by monitoring the change history, you can assert device status by comparing the changes provided by this operation with a one-time snapshot of the statuses provided in [getOrganizationDevicesAvailabilities](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities/). This is substantially more efficient than polling device statuses on an interval, because an empty response in the change history means were no status changes during that time for any device in an entire organization.

##### Use case: one-time poll of device up/down/alerting/dormant status

[getOrganizationDevicesAvailabilities](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities/) provides status information for devices in a more performant manner than the deprecated statuses operation.

##### Use case: Polling device power module status

[getOrganizationDevicesPowerModulesStatusesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-power-modules-statuses-by-device/) lists the most recent status information for power modules in rackmount MX and MS devices that support them.

##### Use case: Polling device uplink and/or management addresses

[getOrganizationDevicesUplinksAddressesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-uplinks-addresses-by-device/) lists the current uplink addresses for devices in an organization.

### Camera operations

#### Analytics

The following operations are deprecated in favor of the newer [boundaries](https://developer.cisco.com/meraki/api-v1/search/?q=boundaries) operations.

* [getDeviceCameraAnalyticsLive](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-live/)
* [getDeviceCameraAnalyticsOverview](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-overview/)
* [getDeviceCameraAnalyticsRecent](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-recent/)
* [getDeviceCameraAnalyticsZones](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-zones/)
* [getDeviceCameraAnalyticsZoneHistory](https://developer.cisco.com/meraki/api-v1/get-device-camera-analytics-zone-history/)

### Monitoring operations

#### Alerts

##### getNetworkHealthAlerts

[getNetworkHealthAlerts](https://developer.cisco.com/meraki/api-v1/get-network-health-alerts) is deprecated in favor of [getOrganizationAssuranceAlerts](https://developer.cisco.com/meraki/api-v1/get-organization-assurance-alerts) which offers more extensive filtering capabilities
