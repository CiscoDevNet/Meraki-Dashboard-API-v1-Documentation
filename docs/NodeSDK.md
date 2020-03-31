# Getting started

The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.

> Date: 04 March, 2020
>
> [What's New](https://meraki.io/whats-new/)

---

[API Documentation](https://meraki.io/api)

[Community Support](https://meraki.io/community)

[Meraki Homepage](https://www.meraki.com)


## How to Build

The generated SDK relies on [Node Package Manager](https://www.npmjs.com/) (NPM) being available to resolve dependencies. If you don't already have NPM installed, please go ahead and follow instructions to install NPM from [here](https://nodejs.org/en/download/).
The SDK also requires Node to be installed. If Node isn't already installed, please install it from [here](https://nodejs.org/en/download/)
> NPM is installed by default when Node is installed

To check if node and npm have been successfully installed, write the following commands in command prompt:

* `node --version`
* `npm -version`

![Version Check](https://apidocs.io/illustration/nodejs?step=versionCheck&workspaceFolder=Meraki-Node)

Now use npm to resolve all dependencies by running the following command in the root directory (of the SDK folder):

```bash
npm install
```

![Resolve Dependencies](https://apidocs.io/illustration/nodejs?step=resolveDependency1&workspaceFolder=Meraki-Node)

![Resolve Dependencies](https://apidocs.io/illustration/nodejs?step=resolveDependency2)

This will install all dependencies in the `node_modules` folder.

Once dependencies are resolved, you will need to move the folder `Meraki ` in to your `node_modules` folder.

## How to Use

The following section explains how to use the library in a new project.

### 1. Open Project Folder
Open an IDE/Text Editor for JavaScript like Sublime Text. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

Click on `File` and select `Open Folder`.

![Open Folder](https://apidocs.io/illustration/nodejs?step=openFolder)

Select the folder of your SDK and click on `Select Folder` to open it up in Sublime Text. The folder will become visible in the bar on the left.

![Open Project](https://apidocs.io/illustration/nodejs?step=openProject&workspaceFolder=Meraki-Node)

### 2. Creating a Test File

Now right click on the folder name and select the `New File` option to create a new test file. Save it as `index.js` Now import the generated NodeJS library using the following lines of code:

```js
var lib = require('lib');
```

Save changes.

![Create new file](https://apidocs.io/illustration/nodejs?step=createNewFile&workspaceFolder=Meraki-Node)

![Save new file](https://apidocs.io/illustration/nodejs?step=saveNewFile&workspaceFolder=Meraki-Node)

### 3. Running The Test File

To run the `index.js` file, open up the command prompt and navigate to the Path where the SDK folder resides. Type the following command to run the file:

```
node index.js
```

![Run file](https://apidocs.io/illustration/nodejs?step=runProject&workspaceFolder=Meraki-Node)


## How to Test

These tests use Mocha framework for testing, coupled with Chai for assertions. These dependencies need to be installed for tests to run.
Tests can be run in a number of ways:

### Method 1 (Run all tests)

1. Navigate to the root directory of the SDK folder from command prompt.
2. Type `mocha --recursive` to run all the tests.

### Method 2 (Run all tests)

1. Navigate to the `../test/Controllers/` directory from command prompt.
2. Type `mocha *` to run all the tests.

### Method 3 (Run specific controller's tests)

1. Navigate to the `../test/Controllers/` directory from command prompt.
2. Type `mocha  Meraki Dashboard APIController`  to run all the tests in that controller file.

> To increase mocha's default timeout, you can change the `TEST_TIMEOUT` parameter's value in `TestBootstrap.js`.

![Run Tests](https://apidocs.io/illustration/nodejs?step=runTests&controllerName=Meraki%20Dashboard%20APIController)

## Initialization

### Authentication
In order to setup authentication in the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| xCiscoMerakiAPIKey | TODO: add a description |



API client can be initialized as following:

```JavaScript
const lib = require('lib');

// Configuration parameters and credentials
lib.Configuration.xCiscoMerakiAPIKey = "xCiscoMerakiAPIKey";

```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [APIUsageController](#api_usage_controller)
* [ActionBatchesController](#action_batches_controller)
* [AdminsController](#admins_controller)
* [AlertSettingsController](#alert_settings_controller)
* [BluetoothClientsController](#bluetooth_clients_controller)
* [BluetoothSettingsController](#bluetooth_settings_controller)
* [CameraQualityRetentionProfilesController](#camera_quality_retention_profiles_controller)
* [CamerasController](#cameras_controller)
* [ChangeLogController](#change_log_controller)
* [ClientsController](#clients_controller)
* [ConfigTemplatesController](#config_templates_controller)
* [ConnectivityMonitoringDestinationsController](#connectivity_monitoring_destinations_controller)
* [ContentFilteringCategoriesController](#content_filtering_categories_controller)
* [ContentFilteringRulesController](#content_filtering_rules_controller)
* [DashboardBrandingPoliciesController](#dashboard_branding_policies_controller)
* [DevicesController](#devices_controller)
* [EventsController](#events_controller)
* [FirewalledServicesController](#firewalled_services_controller)
* [FloorplansController](#floorplans_controller)
* [GroupPoliciesController](#group_policies_controller)
* [HTTPServersController](#http_servers_controller)
* [IntrusionSettingsController](#intrusion_settings_controller)
* [LicensesController](#licenses_controller)
* [LinkAggregationsController](#link_aggregations_controller)
* [MGDHCPSettingsController](#mgdhcp_settings_controller)
* [MGLANSettingsController](#mglan_settings_controller)
* [MGConnectivityMonitoringDestinationsController](#mg_connectivity_monitoring_destinations_controller)
* [MGPortForwardingRulesController](#mg_port_forwarding_rules_controller)
* [MGSubnetPoolSettingsController](#mg_subnet_pool_settings_controller)
* [MGUplinkSettingsController](#mg_uplink_settings_controller)
* [MRL3FirewallController](#mrl3_firewall_controller)
* [MVSenseController](#mv_sense_controller)
* [MX11NATRulesController](#mx11_nat_rules_controller)
* [MX1ManyNATRulesController](#mx1_many_nat_rules_controller)
* [MXL3FirewallController](#mxl3_firewall_controller)
* [MXL7ApplicationCategoriesController](#mxl7_application_categories_controller)
* [MXL7FirewallController](#mxl7_firewall_controller)
* [MXVLANPortsController](#mxvlan_ports_controller)
* [MXVPNFirewallController](#mxvpn_firewall_controller)
* [MXCellularFirewallController](#mx_cellular_firewall_controller)
* [MXInboundFirewallController](#mx_inbound_firewall_controller)
* [MXPortForwardingRulesController](#mx_port_forwarding_rules_controller)
* [MXStaticRoutesController](#mx_static_routes_controller)
* [MXWarmSpareSettingsController](#mx_warm_spare_settings_controller)
* [MalwareSettingsController](#malware_settings_controller)
* [ManagementInterfaceSettingsController](#management_interface_settings_controller)
* [MerakiAuthUsersController](#meraki_auth_users_controller)
* [MonitoredMediaServersController](#monitored_media_servers_controller)
* [NamedTagScopeController](#named_tag_scope_controller)
* [NetflowSettingsController](#netflow_settings_controller)
* [NetworksController](#networks_controller)
* [OpenAPISpecController](#open_api_spec_controller)
* [OrganizationsController](#organizations_controller)
* [PIIController](#pii_controller)
* [RadioSettingsController](#radio_settings_controller)
* [SAMLRolesController](#saml_roles_controller)
* [SMController](#sm_controller)
* [SNMPSettingsController](#snmp_settings_controller)
* [SsidsController](#ssids_controller)
* [SecurityEventsController](#security_events_controller)
* [SplashLoginAttemptsController](#splash_login_attempts_controller)
* [SplashSettingsController](#splash_settings_controller)
* [SwitchAclsController](#switch_acls_controller)
* [SwitchPortSchedulesController](#switch_port_schedules_controller)
* [SwitchPortsController](#switch_ports_controller)
* [SwitchProfilesController](#switch_profiles_controller)
* [SwitchSettingsController](#switch_settings_controller)
* [SwitchStacksController](#switch_stacks_controller)
* [SyslogServersController](#syslog_servers_controller)
* [TrafficAnalysisSettingsController](#traffic_analysis_settings_controller)
* [TrafficShapingController](#traffic_shaping_controller)
* [UplinkSettingsController](#uplink_settings_controller)
* [VlansController](#vlans_controller)
* [WebhookLogsController](#webhook_logs_controller)
* [WirelessHealthController](#wireless_health_controller)
* [WirelessSettingsController](#wireless_settings_controller)

## <a name="api_usage_controller"></a>![Class: ](https://apidocs.io/img/class.png ".APIUsageController") APIUsageController

### Get singleton instance

The singleton instance of the ``` APIUsageController ``` class can be accessed from the API Client.

```javascript
var controller = lib.APIUsageController;
```

### <a name="get_organization_api_requests"></a>![Method: ](https://apidocs.io/img/method.png ".APIUsageController.getOrganizationApiRequests") getOrganizationApiRequests

> List the API requests made by an organization


```javascript
function getOrganizationApiRequests(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| adminId |  ``` Optional ```  | Filter the results by the ID of the admin who made the API requests |
| path |  ``` Optional ```  | Filter the results by the path of the API requests |
| method |  ``` Optional ```  | Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE') |
| responseCode |  ``` Optional ```  | Filter the results by the response code of the API requests |
| sourceIp |  ``` Optional ```  | Filter the results by the IP address of the originating API request |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 13.9902985300824;
        input['perPage'] = 13;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['adminId'] = 'adminId';
        input['path'] = 'path';
        input['method'] = 'method';
        input['responseCode'] = 13;
        input['sourceIp'] = 'sourceIp';

    controller.getOrganizationApiRequests(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_api_requests_overview"></a>![Method: ](https://apidocs.io/img/method.png ".APIUsageController.getOrganizationApiRequestsOverview") getOrganizationApiRequestsOverview

> Return an aggregated overview of API requests data


```javascript
function getOrganizationApiRequestsOverview(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 227.267125303516;

    controller.getOrganizationApiRequestsOverview(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="action_batches_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ActionBatchesController") ActionBatchesController

### Get singleton instance

The singleton instance of the ``` ActionBatchesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ActionBatchesController;
```

### <a name="create_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.createOrganizationActionBatch") createOrganizationActionBatch

> Create an action batch


```javascript
function createOrganizationActionBatch(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationActionBatch |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationActionBatch'] = new CreateOrganizationActionBatchModel({"key":"value"});

    controller.createOrganizationActionBatch(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_action_batches"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.getOrganizationActionBatches") getOrganizationActionBatches

> Return the list of action batches in the organization


```javascript
function getOrganizationActionBatches(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationActionBatches(organizationId, function(error, response, context) {

    
    });
```



### <a name="get_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.getOrganizationActionBatch") getOrganizationActionBatch

> Return an action batch


```javascript
function getOrganizationActionBatch(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['actionBatchId'] = 'actionBatchId';

    controller.getOrganizationActionBatch(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.deleteOrganizationActionBatch") deleteOrganizationActionBatch

> Delete an action batch


```javascript
function deleteOrganizationActionBatch(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['actionBatchId'] = 'actionBatchId';

    controller.deleteOrganizationActionBatch(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_action_batch"></a>![Method: ](https://apidocs.io/img/method.png ".ActionBatchesController.updateOrganizationActionBatch") updateOrganizationActionBatch

> Update an action batch


```javascript
function updateOrganizationActionBatch(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| actionBatchId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationActionBatch |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['actionBatchId'] = 'actionBatchId';
        input['updateOrganizationActionBatch'] = new UpdateOrganizationActionBatchModel({"key":"value"});

    controller.updateOrganizationActionBatch(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="admins_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AdminsController") AdminsController

### Get singleton instance

The singleton instance of the ``` AdminsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.AdminsController;
```

### <a name="get_organization_admins"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.getOrganizationAdmins") getOrganizationAdmins

> List the dashboard administrators in this organization


```javascript
function getOrganizationAdmins(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationAdmins(organizationId, function(error, response, context) {

    
    });
```



### <a name="create_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.createOrganizationAdmin") createOrganizationAdmin

> Create a new dashboard administrator


```javascript
function createOrganizationAdmin(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationAdmin |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationAdmin'] = new CreateOrganizationAdminModel({"key":"value"});

    controller.createOrganizationAdmin(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.updateOrganizationAdmin") updateOrganizationAdmin

> Update an administrator


```javascript
function updateOrganizationAdmin(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationAdmin |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['id'] = 'id';
        input['updateOrganizationAdmin'] = new UpdateOrganizationAdminModel({"key":"value"});

    controller.updateOrganizationAdmin(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization_admin"></a>![Method: ](https://apidocs.io/img/method.png ".AdminsController.deleteOrganizationAdmin") deleteOrganizationAdmin

> Revoke all access for a dashboard administrator within this organization


```javascript
function deleteOrganizationAdmin(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['id'] = 'id';

    controller.deleteOrganizationAdmin(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="alert_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AlertSettingsController") AlertSettingsController

### Get singleton instance

The singleton instance of the ``` AlertSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.AlertSettingsController;
```

### <a name="get_network_alert_settings"></a>![Method: ](https://apidocs.io/img/method.png ".AlertSettingsController.getNetworkAlertSettings") getNetworkAlertSettings

> Return the alert configuration for this network


```javascript
function getNetworkAlertSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkAlertSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_alert_settings"></a>![Method: ](https://apidocs.io/img/method.png ".AlertSettingsController.updateNetworkAlertSettings") updateNetworkAlertSettings

> Update the alert configuration for this network


```javascript
function updateNetworkAlertSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkAlertSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkAlertSettings'] = new UpdateNetworkAlertSettingsModel({"key":"value"});

    controller.updateNetworkAlertSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="bluetooth_clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BluetoothClientsController") BluetoothClientsController

### Get singleton instance

The singleton instance of the ``` BluetoothClientsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.BluetoothClientsController;
```

### <a name="get_network_bluetooth_clients"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothClientsController.getNetworkBluetoothClients") getNetworkBluetoothClients

> List the Bluetooth clients seen by APs in this network


```javascript
function getNetworkBluetoothClients(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 7 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['timespan'] = 227.267125303516;
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['includeConnectivityHistory'] = true;

    controller.getNetworkBluetoothClients(input, function(error, response, context) {

    
    });
```



### <a name="get_network_bluetooth_client"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothClientsController.getNetworkBluetoothClient") getNetworkBluetoothClient

> Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.


```javascript
function getNetworkBluetoothClient(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bluetoothClientId |  ``` Required ```  | TODO: Add a parameter description |
| includeConnectivityHistory |  ``` Optional ```  | Include the connectivity history for this client |
| connectivityHistoryTimespan |  ``` Optional ```  | The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['bluetoothClientId'] = 'bluetoothClientId';
        input['includeConnectivityHistory'] = true;
        input['connectivityHistoryTimespan'] = 227;

    controller.getNetworkBluetoothClient(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="bluetooth_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".BluetoothSettingsController") BluetoothSettingsController

### Get singleton instance

The singleton instance of the ``` BluetoothSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.BluetoothSettingsController;
```

### <a name="get_device_wireless_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothSettingsController.getDeviceWirelessBluetoothSettings") getDeviceWirelessBluetoothSettings

> Return the bluetooth settings for a wireless device


```javascript
function getDeviceWirelessBluetoothSettings(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceWirelessBluetoothSettings(serial, function(error, response, context) {

    
    });
```



### <a name="update_device_wireless_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothSettingsController.updateDeviceWirelessBluetoothSettings") updateDeviceWirelessBluetoothSettings

> Update the bluetooth settings for a wireless device


```javascript
function updateDeviceWirelessBluetoothSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceWirelessBluetoothSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['updateDeviceWirelessBluetoothSettings'] = new UpdateDeviceWirelessBluetoothSettingsModel({"key":"value"});

    controller.updateDeviceWirelessBluetoothSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_network_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothSettingsController.getNetworkBluetoothSettings") getNetworkBluetoothSettings

> Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.


```javascript
function getNetworkBluetoothSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkBluetoothSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_bluetooth_settings"></a>![Method: ](https://apidocs.io/img/method.png ".BluetoothSettingsController.updateNetworkBluetoothSettings") updateNetworkBluetoothSettings

> Update the Bluetooth settings for a network. See the docs page for <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a>.


```javascript
function updateNetworkBluetoothSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkBluetoothSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkBluetoothSettings'] = new UpdateNetworkBluetoothSettingsModel({"key":"value"});

    controller.updateNetworkBluetoothSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="camera_quality_retention_profiles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CameraQualityRetentionProfilesController") CameraQualityRetentionProfilesController

### Get singleton instance

The singleton instance of the ``` CameraQualityRetentionProfilesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.CameraQualityRetentionProfilesController;
```

### <a name="get_network_camera_quality_retention_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.getNetworkCameraQualityRetentionProfiles") getNetworkCameraQualityRetentionProfiles

> List the quality retention profiles for this network


```javascript
function getNetworkCameraQualityRetentionProfiles(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCameraQualityRetentionProfiles(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.createNetworkCameraQualityRetentionProfile") createNetworkCameraQualityRetentionProfile

> Creates new quality retention profile for this network.


```javascript
function createNetworkCameraQualityRetentionProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkCameraQualityRetentionProfile |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkCameraQualityRetentionProfile'] = new CreateNetworkCameraQualityRetentionProfileModel({"key":"value"});

    controller.createNetworkCameraQualityRetentionProfile(input, function(error, response, context) {

    
    });
```



### <a name="get_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.getNetworkCameraQualityRetentionProfile") getNetworkCameraQualityRetentionProfile

> Retrieve a single quality retention profile


```javascript
function getNetworkCameraQualityRetentionProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qualityRetentionProfileId'] = 'qualityRetentionProfileId';

    controller.getNetworkCameraQualityRetentionProfile(input, function(error, response, context) {

    
    });
```



### <a name="update_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.updateNetworkCameraQualityRetentionProfile") updateNetworkCameraQualityRetentionProfile

> Update an existing quality retention profile for this network.


```javascript
function updateNetworkCameraQualityRetentionProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCameraQualityRetentionProfile |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qualityRetentionProfileId'] = 'qualityRetentionProfileId';
        input['updateNetworkCameraQualityRetentionProfile'] = new UpdateNetworkCameraQualityRetentionProfileModel({"key":"value"});

    controller.updateNetworkCameraQualityRetentionProfile(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_camera_quality_retention_profile"></a>![Method: ](https://apidocs.io/img/method.png ".CameraQualityRetentionProfilesController.deleteNetworkCameraQualityRetentionProfile") deleteNetworkCameraQualityRetentionProfile

> Delete an existing quality retention profile for this network.


```javascript
function deleteNetworkCameraQualityRetentionProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qualityRetentionProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qualityRetentionProfileId'] = 'qualityRetentionProfileId';

    controller.deleteNetworkCameraQualityRetentionProfile(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="cameras_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CamerasController") CamerasController

### Get singleton instance

The singleton instance of the ``` CamerasController ``` class can be accessed from the API Client.

```javascript
var controller = lib.CamerasController;
```

### <a name="get_device_camera_quality_and_retention_settings"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.getDeviceCameraQualityAndRetentionSettings") getDeviceCameraQualityAndRetentionSettings

> Returns quality and retention settings for the given camera


```javascript
function getDeviceCameraQualityAndRetentionSettings(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceCameraQualityAndRetentionSettings(serial, function(error, response, context) {

    
    });
```



### <a name="update_device_camera_quality_and_retention_settings"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.updateDeviceCameraQualityAndRetentionSettings") updateDeviceCameraQualityAndRetentionSettings

> Update quality and retention settings for the given camera


```javascript
function updateDeviceCameraQualityAndRetentionSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCameraQualityAndRetentionSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['updateDeviceCameraQualityAndRetentionSettings'] = new UpdateDeviceCameraQualityAndRetentionSettingsModel({"key":"value"});

    controller.updateDeviceCameraQualityAndRetentionSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_network_camera_schedules"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.getNetworkCameraSchedules") getNetworkCameraSchedules

> Returns a list of all camera recording schedules.


```javascript
function getNetworkCameraSchedules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCameraSchedules(networkId, function(error, response, context) {

    
    });
```



### <a name="generate_network_camera_snapshot"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.generateNetworkCameraSnapshot") generateNetworkCameraSnapshot

> Generate a snapshot of what the camera sees at the specified time and return a link to that image.


```javascript
function generateNetworkCameraSnapshot(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| generateNetworkCameraSnapshot |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['generateNetworkCameraSnapshot'] = new GenerateNetworkCameraSnapshotModel({"key":"value"});

    controller.generateNetworkCameraSnapshot(input, function(error, response, context) {

    
    });
```



### <a name="get_network_camera_video_link"></a>![Method: ](https://apidocs.io/img/method.png ".CamerasController.getNetworkCameraVideoLink") getNetworkCameraVideoLink

> Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.


```javascript
function getNetworkCameraVideoLink(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| timestamp |  ``` Optional ```  | [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['timestamp'] = 'timestamp';

    controller.getNetworkCameraVideoLink(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="change_log_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ChangeLogController") ChangeLogController

### Get singleton instance

The singleton instance of the ``` ChangeLogController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ChangeLogController;
```

### <a name="get_organization_configuration_changes"></a>![Method: ](https://apidocs.io/img/method.png ".ChangeLogController.getOrganizationConfigurationChanges") getOrganizationConfigurationChanges

> View the Change Log for your organization


```javascript
function getOrganizationConfigurationChanges(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 365 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| networkId |  ``` Optional ```  | Filters on the given network |
| adminId |  ``` Optional ```  | Filters on the given Admin |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 227.267125303516;
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['networkId'] = 'networkId';
        input['adminId'] = 'adminId';

    controller.getOrganizationConfigurationChanges(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="clients_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ClientsController") ClientsController

### Get singleton instance

The singleton instance of the ``` ClientsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ClientsController;
```

### <a name="get_device_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getDeviceClients") getDeviceClients

> List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.


```javascript
function getDeviceClients(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['timespan'] = 227.267125303516;

    controller.getDeviceClients(input, function(error, response, context) {

    
    });
```



### <a name="get_network_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClients") getNetworkClients

> List the clients that have used this network in the timespan


```javascript
function getNetworkClients(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['timespan'] = 227.267125303516;
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkClients(input, function(error, response, context) {

    
    });
```



### <a name="provision_network_clients"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.provisionNetworkClients") provisionNetworkClients

> Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.


```javascript
function provisionNetworkClients(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| provisionNetworkClients |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['provisionNetworkClients'] = new ProvisionNetworkClientsModel({"key":"value"});

    controller.provisionNetworkClients(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClient") getNetworkClient

> Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClient(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';

    controller.getNetworkClient(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_events"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientEvents") getNetworkClientEvents

> Return the events associated with this client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientEvents(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkClientEvents(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_latency_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientLatencyHistory") getNetworkClientLatencyHistory

> Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.


```javascript
function getNetworkClientLatencyHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 227.267125303516;
        input['resolution'] = 227;

    controller.getNetworkClientLatencyHistory(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientPolicy") getNetworkClientPolicy

> Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';

    controller.getNetworkClientPolicy(input, function(error, response, context) {

    
    });
```



### <a name="update_network_client_policy"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.updateNetworkClientPolicy") updateNetworkClientPolicy

> Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function updateNetworkClientPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientPolicy |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['updateNetworkClientPolicy'] = new UpdateNetworkClientPolicyModel({"key":"value"});

    controller.updateNetworkClientPolicy(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientSplashAuthorizationStatus") getNetworkClientSplashAuthorizationStatus

> Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientSplashAuthorizationStatus(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';

    controller.getNetworkClientSplashAuthorizationStatus(input, function(error, response, context) {

    
    });
```



### <a name="update_network_client_splash_authorization_status"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.updateNetworkClientSplashAuthorizationStatus") updateNetworkClientSplashAuthorizationStatus

> Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function updateNetworkClientSplashAuthorizationStatus(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkClientSplashAuthorizationStatus |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['updateNetworkClientSplashAuthorizationStatus'] = new UpdateNetworkClientSplashAuthorizationStatusModel({"key":"value"});

    controller.updateNetworkClientSplashAuthorizationStatus(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_traffic_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientTrafficHistory") getNetworkClientTrafficHistory

> Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientTrafficHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkClientTrafficHistory(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_usage_history"></a>![Method: ](https://apidocs.io/img/method.png ".ClientsController.getNetworkClientUsageHistory") getNetworkClientUsageHistory

> Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientUsageHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';

    controller.getNetworkClientUsageHistory(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="config_templates_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConfigTemplatesController") ConfigTemplatesController

### Get singleton instance

The singleton instance of the ``` ConfigTemplatesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ConfigTemplatesController;
```

### <a name="get_organization_config_templates"></a>![Method: ](https://apidocs.io/img/method.png ".ConfigTemplatesController.getOrganizationConfigTemplates") getOrganizationConfigTemplates

> List the configuration templates for this organization


```javascript
function getOrganizationConfigTemplates(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationConfigTemplates(organizationId, function(error, response, context) {

    
    });
```



### <a name="delete_organization_config_template"></a>![Method: ](https://apidocs.io/img/method.png ".ConfigTemplatesController.deleteOrganizationConfigTemplate") deleteOrganizationConfigTemplate

> Remove a configuration template


```javascript
function deleteOrganizationConfigTemplate(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['configTemplateId'] = 'configTemplateId';

    controller.deleteOrganizationConfigTemplate(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="connectivity_monitoring_destinations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ConnectivityMonitoringDestinationsController") ConnectivityMonitoringDestinationsController

### Get singleton instance

The singleton instance of the ``` ConnectivityMonitoringDestinationsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ConnectivityMonitoringDestinationsController;
```

### <a name="get_network_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".ConnectivityMonitoringDestinationsController.getNetworkConnectivityMonitoringDestinations") getNetworkConnectivityMonitoringDestinations

> Return the connectivity testing destinations for an MX network


```javascript
function getNetworkConnectivityMonitoringDestinations(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkConnectivityMonitoringDestinations(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".ConnectivityMonitoringDestinationsController.updateNetworkConnectivityMonitoringDestinations") updateNetworkConnectivityMonitoringDestinations

> Update the connectivity testing destinations for an MX network


```javascript
function updateNetworkConnectivityMonitoringDestinations(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkConnectivityMonitoringDestinations |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkConnectivityMonitoringDestinations'] = new UpdateNetworkConnectivityMonitoringDestinationsModel({"key":"value"});

    controller.updateNetworkConnectivityMonitoringDestinations(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="content_filtering_categories_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ContentFilteringCategoriesController") ContentFilteringCategoriesController

### Get singleton instance

The singleton instance of the ``` ContentFilteringCategoriesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ContentFilteringCategoriesController;
```

### <a name="get_network_content_filtering_categories"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringCategoriesController.getNetworkContentFilteringCategories") getNetworkContentFilteringCategories

> List all available content filtering categories for an MX network


```javascript
function getNetworkContentFilteringCategories(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkContentFilteringCategories(networkId, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="content_filtering_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ContentFilteringRulesController") ContentFilteringRulesController

### Get singleton instance

The singleton instance of the ``` ContentFilteringRulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ContentFilteringRulesController;
```

### <a name="get_network_content_filtering"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringRulesController.getNetworkContentFiltering") getNetworkContentFiltering

> Return the content filtering settings for an MX network


```javascript
function getNetworkContentFiltering(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkContentFiltering(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_content_filtering"></a>![Method: ](https://apidocs.io/img/method.png ".ContentFilteringRulesController.updateNetworkContentFiltering") updateNetworkContentFiltering

> Update the content filtering settings for an MX network


```javascript
function updateNetworkContentFiltering(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkContentFiltering |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkContentFiltering'] = new UpdateNetworkContentFilteringModel({"key":"value"});

    controller.updateNetworkContentFiltering(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="dashboard_branding_policies_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DashboardBrandingPoliciesController") DashboardBrandingPoliciesController

### Get singleton instance

The singleton instance of the ``` DashboardBrandingPoliciesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.DashboardBrandingPoliciesController;
```

### <a name="get_organization_branding_policies"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.getOrganizationBrandingPolicies") getOrganizationBrandingPolicies

> List the branding policies of an organization


```javascript
function getOrganizationBrandingPolicies(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationBrandingPolicies(organizationId, function(error, response, context) {

    
    });
```



### <a name="create_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.createOrganizationBrandingPolicy") createOrganizationBrandingPolicy

> Add a new branding policy to an organization


```javascript
function createOrganizationBrandingPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationBrandingPolicy |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationBrandingPolicy'] = new CreateOrganizationBrandingPolicyModel({"key":"value"});

    controller.createOrganizationBrandingPolicy(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_branding_policies_priorities"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.getOrganizationBrandingPoliciesPriorities") getOrganizationBrandingPoliciesPriorities

> Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).


```javascript
function getOrganizationBrandingPoliciesPriorities(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationBrandingPoliciesPriorities(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization_branding_policies_priorities"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.updateOrganizationBrandingPoliciesPriorities") updateOrganizationBrandingPoliciesPriorities

> Update the priority ordering of an organization's branding policies.


```javascript
function updateOrganizationBrandingPoliciesPriorities(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationBrandingPoliciesPriorities |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganizationBrandingPoliciesPriorities'] = new UpdateOrganizationBrandingPoliciesPrioritiesModel({"key":"value"});

    controller.updateOrganizationBrandingPoliciesPriorities(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.getOrganizationBrandingPolicy") getOrganizationBrandingPolicy

> Return a branding policy


```javascript
function getOrganizationBrandingPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['brandingPolicyId'] = 'brandingPolicyId';

    controller.getOrganizationBrandingPolicy(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.updateOrganizationBrandingPolicy") updateOrganizationBrandingPolicy

> Update a branding policy


```javascript
function updateOrganizationBrandingPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationBrandingPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['brandingPolicyId'] = 'brandingPolicyId';
        input['updateOrganizationBrandingPolicy'] = new UpdateOrganizationBrandingPolicyModel({"key":"value"});

    controller.updateOrganizationBrandingPolicy(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization_branding_policy"></a>![Method: ](https://apidocs.io/img/method.png ".DashboardBrandingPoliciesController.deleteOrganizationBrandingPolicy") deleteOrganizationBrandingPolicy

> Delete a branding policy


```javascript
function deleteOrganizationBrandingPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| brandingPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['brandingPolicyId'] = 'brandingPolicyId';

    controller.deleteOrganizationBrandingPolicy(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="devices_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DevicesController") DevicesController

### Get singleton instance

The singleton instance of the ``` DevicesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.DevicesController;
```

### <a name="cycle_device_switch_ports"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.cycleDeviceSwitchPorts") cycleDeviceSwitchPorts

> Cycle a set of switch ports


```javascript
function cycleDeviceSwitchPorts(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| cycleDeviceSwitchPorts |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['cycleDeviceSwitchPorts'] = new CycleDeviceSwitchPortsModel({"key":"value"});

    controller.cycleDeviceSwitchPorts(input, function(error, response, context) {

    
    });
```



### <a name="get_network_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDevices") getNetworkDevices

> List the devices in a network


```javascript
function getNetworkDevices(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkDevices(networkId, function(error, response, context) {

    
    });
```



### <a name="claim_network_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.claimNetworkDevices") claimNetworkDevices

> Claim devices into a network


```javascript
function claimNetworkDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| claimNetworkDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['claimNetworkDevices'] = new ClaimNetworkDevicesModel({"key":"value"});

    controller.claimNetworkDevices(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDevice") getNetworkDevice

> Return a single device


```javascript
function getNetworkDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDevice(input, function(error, response, context) {

    
    });
```



### <a name="update_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.updateNetworkDevice") updateNetworkDevice

> Update the attributes of a device


```javascript
function updateNetworkDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDevice |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['updateNetworkDevice'] = new UpdateNetworkDeviceModel({"key":"value"});

    controller.updateNetworkDevice(input, function(error, response, context) {

    
    });
```



### <a name="blink_network_device_leds"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.blinkNetworkDeviceLeds") blinkNetworkDeviceLeds

> Blink the LEDs on a device


```javascript
function blinkNetworkDeviceLeds(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| blinkNetworkDeviceLeds |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['blinkNetworkDeviceLeds'] = new BlinkNetworkDeviceLedsModel({"key":"value"});

    controller.blinkNetworkDeviceLeds(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_lldp_cdp"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDeviceLldpCdp") getNetworkDeviceLldpCdp

> List LLDP and CDP information for a device


```javascript
function getNetworkDeviceLldpCdp(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| timespan |  ``` Optional ```  | The timespan for which LLDP and CDP information will be fetched. Must be in seconds and less than or equal to a month (2592000 seconds). LLDP and CDP information is sent to the Meraki dashboard every 10 minutes. In instances where this LLDP and CDP information matches an existing entry in the Meraki dashboard, the data is updated once every two hours. Meraki recommends querying LLDP and CDP information at an interval slightly greater than two hours, to ensure that unchanged CDP / LLDP information can be queried consistently. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['timespan'] = 227;

    controller.getNetworkDeviceLldpCdp(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_loss_and_latency_history"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDeviceLossAndLatencyHistory") getNetworkDeviceLossAndLatencyHistory

> Get the uplink loss percentage and latency in milliseconds for a wired network device.


```javascript
function getNetworkDeviceLossAndLatencyHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| ip |  ``` Required ```  | The destination IP used to obtain the requested stats. This is required. |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. |
| uplink |  ``` Optional ```  | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['ip'] = 'ip';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 227.267125303516;
        input['resolution'] = 227;
        input['uplink'] = Object.keys(uplink)[0];

    controller.getNetworkDeviceLossAndLatencyHistory(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_performance"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDevicePerformance") getNetworkDevicePerformance

> Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.


```javascript
function getNetworkDevicePerformance(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDevicePerformance(input, function(error, response, context) {

    
    });
```



### <a name="reboot_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.rebootNetworkDevice") rebootNetworkDevice

> Reboot a device


```javascript
function rebootNetworkDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.rebootNetworkDevice(input, function(error, response, context) {

    
    });
```



### <a name="remove_network_device"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.removeNetworkDevice") removeNetworkDevice

> Remove a single device


```javascript
function removeNetworkDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.removeNetworkDevice(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getNetworkDeviceUplink") getNetworkDeviceUplink

> Return the uplink information for a device.


```javascript
function getNetworkDeviceUplink(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDeviceUplink(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_devices"></a>![Method: ](https://apidocs.io/img/method.png ".DevicesController.getOrganizationDevices") getOrganizationDevices

> List the devices in an organization


```javascript
function getOrganizationDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| configurationUpdatedAfter |  ``` Optional ```  | Filter results by whether or not the device's configuration has been updated after the given timestamp |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['configurationUpdatedAfter'] = 'configurationUpdatedAfter';

    controller.getOrganizationDevices(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EventsController") EventsController

### Get singleton instance

The singleton instance of the ``` EventsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.EventsController;
```

### <a name="get_network_events"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.getNetworkEvents") getNetworkEvents

> List the events for the network


```javascript
function getNetworkEvents(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| productType |  ``` Optional ```  | The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway |
| includedEventTypes |  ``` Optional ```  ``` Collection ```  | A list of event types. The returned events will be filtered to only include events with these types. |
| excludedEventTypes |  ``` Optional ```  ``` Collection ```  | A list of event types. The returned events will be filtered to exclude events with these types. |
| deviceMac |  ``` Optional ```  | The MAC address of the Meraki device which the list of events will be filtered with |
| deviceSerial |  ``` Optional ```  | The serial of the Meraki device which the list of events will be filtered with |
| deviceName |  ``` Optional ```  | The name of the Meraki device which the list of events will be filtered with |
| clientIp |  ``` Optional ```  | The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks. |
| clientMac |  ``` Optional ```  | The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks. |
| clientName |  ``` Optional ```  | The name, or partial name, of the client which the list of events will be filtered with |
| smDeviceMac |  ``` Optional ```  | The MAC address of the Systems Manager device which the list of events will be filtered with |
| smDeviceName |  ``` Optional ```  | The name of the Systems Manager device which the list of events will be filtered with |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['productType'] = 'productType';
        input['includedEventTypes'] = ['includedEventTypes'];
        input['excludedEventTypes'] = ['excludedEventTypes'];
        input['deviceMac'] = 'deviceMac';
        input['deviceSerial'] = 'deviceSerial';
        input['deviceName'] = 'deviceName';
        input['clientIp'] = 'clientIp';
        input['clientMac'] = 'clientMac';
        input['clientName'] = 'clientName';
        input['smDeviceMac'] = 'smDeviceMac';
        input['smDeviceName'] = 'smDeviceName';
        input['perPage'] = 227;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkEvents(input, function(error, response, context) {

    
    });
```



### <a name="get_network_events_event_types"></a>![Method: ](https://apidocs.io/img/method.png ".EventsController.getNetworkEventsEventTypes") getNetworkEventsEventTypes

> List the event type to human-readable description


```javascript
function getNetworkEventsEventTypes(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkEventsEventTypes(networkId, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="firewalled_services_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FirewalledServicesController") FirewalledServicesController

### Get singleton instance

The singleton instance of the ``` FirewalledServicesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.FirewalledServicesController;
```

### <a name="get_network_firewalled_services"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.getNetworkFirewalledServices") getNetworkFirewalledServices

> List the appliance services and their accessibility rules


```javascript
function getNetworkFirewalledServices(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkFirewalledServices(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_firewalled_service"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.getNetworkFirewalledService") getNetworkFirewalledService

> Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')


```javascript
function getNetworkFirewalledService(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| service |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['service'] = 'service';

    controller.getNetworkFirewalledService(input, function(error, response, context) {

    
    });
```



### <a name="update_network_firewalled_service"></a>![Method: ](https://apidocs.io/img/method.png ".FirewalledServicesController.updateNetworkFirewalledService") updateNetworkFirewalledService

> Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')


```javascript
function updateNetworkFirewalledService(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| service |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkFirewalledService |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['service'] = 'service';
        input['updateNetworkFirewalledService'] = new UpdateNetworkFirewalledServiceModel({"key":"value"});

    controller.updateNetworkFirewalledService(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="floorplans_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FloorplansController") FloorplansController

### Get singleton instance

The singleton instance of the ``` FloorplansController ``` class can be accessed from the API Client.

```javascript
var controller = lib.FloorplansController;
```

### <a name="get_network_floor_plans"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.getNetworkFloorPlans") getNetworkFloorPlans

> List the floor plans that belong to your network


```javascript
function getNetworkFloorPlans(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkFloorPlans(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.createNetworkFloorPlan") createNetworkFloorPlan

> Upload a floor plan


```javascript
function createNetworkFloorPlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkFloorPlan |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkFloorPlan'] = new CreateNetworkFloorPlanModel({"key":"value"});

    controller.createNetworkFloorPlan(input, function(error, response, context) {

    
    });
```



### <a name="get_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.getNetworkFloorPlan") getNetworkFloorPlan

> Find a floor plan by ID


```javascript
function getNetworkFloorPlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['floorPlanId'] = 'floorPlanId';

    controller.getNetworkFloorPlan(input, function(error, response, context) {

    
    });
```



### <a name="update_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.updateNetworkFloorPlan") updateNetworkFloorPlan

> Update a floor plan's geolocation and other meta data


```javascript
function updateNetworkFloorPlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkFloorPlan |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['floorPlanId'] = 'floorPlanId';
        input['updateNetworkFloorPlan'] = new UpdateNetworkFloorPlanModel({"key":"value"});

    controller.updateNetworkFloorPlan(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_floor_plan"></a>![Method: ](https://apidocs.io/img/method.png ".FloorplansController.deleteNetworkFloorPlan") deleteNetworkFloorPlan

> Destroy a floor plan


```javascript
function deleteNetworkFloorPlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| floorPlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['floorPlanId'] = 'floorPlanId';

    controller.deleteNetworkFloorPlan(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="group_policies_controller"></a>![Class: ](https://apidocs.io/img/class.png ".GroupPoliciesController") GroupPoliciesController

### Get singleton instance

The singleton instance of the ``` GroupPoliciesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.GroupPoliciesController;
```

### <a name="get_network_group_policies"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.getNetworkGroupPolicies") getNetworkGroupPolicies

> List the group policies in a network


```javascript
function getNetworkGroupPolicies(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkGroupPolicies(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.createNetworkGroupPolicy") createNetworkGroupPolicy

> Create a group policy


```javascript
function createNetworkGroupPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkGroupPolicy |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkGroupPolicy'] = new CreateNetworkGroupPolicyModel({"key":"value"});

    controller.createNetworkGroupPolicy(input, function(error, response, context) {

    
    });
```



### <a name="get_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.getNetworkGroupPolicy") getNetworkGroupPolicy

> Display a group policy


```javascript
function getNetworkGroupPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['groupPolicyId'] = 'groupPolicyId';

    controller.getNetworkGroupPolicy(input, function(error, response, context) {

    
    });
```



### <a name="update_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.updateNetworkGroupPolicy") updateNetworkGroupPolicy

> Update a group policy


```javascript
function updateNetworkGroupPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkGroupPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['groupPolicyId'] = 'groupPolicyId';
        input['updateNetworkGroupPolicy'] = new UpdateNetworkGroupPolicyModel({"key":"value"});

    controller.updateNetworkGroupPolicy(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_group_policy"></a>![Method: ](https://apidocs.io/img/method.png ".GroupPoliciesController.deleteNetworkGroupPolicy") deleteNetworkGroupPolicy

> Delete a group policy


```javascript
function deleteNetworkGroupPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| groupPolicyId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['groupPolicyId'] = 'groupPolicyId';

    controller.deleteNetworkGroupPolicy(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="http_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".HTTPServersController") HTTPServersController

### Get singleton instance

The singleton instance of the ``` HTTPServersController ``` class can be accessed from the API Client.

```javascript
var controller = lib.HTTPServersController;
```

### <a name="get_network_http_servers"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.getNetworkHttpServers") getNetworkHttpServers

> List the HTTP servers for a network


```javascript
function getNetworkHttpServers(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkHttpServers(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.createNetworkHttpServer") createNetworkHttpServer

> Add an HTTP server to a network


```javascript
function createNetworkHttpServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkHttpServer'] = new CreateNetworkHttpServerModel({"key":"value"});

    controller.createNetworkHttpServer(input, function(error, response, context) {

    
    });
```



### <a name="create_network_http_servers_webhook_test"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.createNetworkHttpServersWebhookTest") createNetworkHttpServersWebhookTest

> Send a test webhook for a network


```javascript
function createNetworkHttpServersWebhookTest(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkHttpServersWebhookTest |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkHttpServersWebhookTest'] = new CreateNetworkHttpServersWebhookTestModel({"key":"value"});

    controller.createNetworkHttpServersWebhookTest(input, function(error, response, context) {

    
    });
```



### <a name="get_network_http_servers_webhook_test"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.getNetworkHttpServersWebhookTest") getNetworkHttpServersWebhookTest

> Return the status of a webhook test for a network


```javascript
function getNetworkHttpServersWebhookTest(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['id'] = 'id';

    controller.getNetworkHttpServersWebhookTest(input, function(error, response, context) {

    
    });
```



### <a name="get_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.getNetworkHttpServer") getNetworkHttpServer

> Return an HTTP server for a network


```javascript
function getNetworkHttpServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['id'] = 'id';

    controller.getNetworkHttpServer(input, function(error, response, context) {

    
    });
```



### <a name="update_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.updateNetworkHttpServer") updateNetworkHttpServer

> Update an HTTP server


```javascript
function updateNetworkHttpServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkHttpServer |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['id'] = 'id';
        input['updateNetworkHttpServer'] = new UpdateNetworkHttpServerModel({"key":"value"});

    controller.updateNetworkHttpServer(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_http_server"></a>![Method: ](https://apidocs.io/img/method.png ".HTTPServersController.deleteNetworkHttpServer") deleteNetworkHttpServer

> Delete an HTTP server from a network


```javascript
function deleteNetworkHttpServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['id'] = 'id';

    controller.deleteNetworkHttpServer(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="intrusion_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".IntrusionSettingsController") IntrusionSettingsController

### Get singleton instance

The singleton instance of the ``` IntrusionSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.IntrusionSettingsController;
```

### <a name="get_network_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.getNetworkSecurityIntrusionSettings") getNetworkSecurityIntrusionSettings

> Returns all supported intrusion settings for an MX network


```javascript
function getNetworkSecurityIntrusionSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSecurityIntrusionSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.updateNetworkSecurityIntrusionSettings") updateNetworkSecurityIntrusionSettings

> Set the supported intrusion settings for an MX network


```javascript
function updateNetworkSecurityIntrusionSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSecurityIntrusionSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSecurityIntrusionSettings'] = new UpdateNetworkSecurityIntrusionSettingsModel({"key":"value"});

    controller.updateNetworkSecurityIntrusionSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.getOrganizationSecurityIntrusionSettings") getOrganizationSecurityIntrusionSettings

> Returns all supported intrusion settings for an organization


```javascript
function getOrganizationSecurityIntrusionSettings(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationSecurityIntrusionSettings(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization_security_intrusion_settings"></a>![Method: ](https://apidocs.io/img/method.png ".IntrusionSettingsController.updateOrganizationSecurityIntrusionSettings") updateOrganizationSecurityIntrusionSettings

> Sets supported intrusion settings for an organization


```javascript
function updateOrganizationSecurityIntrusionSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSecurityIntrusionSettings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganizationSecurityIntrusionSettings'] = new UpdateOrganizationSecurityIntrusionSettingsModel({"key":"value"});

    controller.updateOrganizationSecurityIntrusionSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="licenses_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LicensesController") LicensesController

### Get singleton instance

The singleton instance of the ``` LicensesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.LicensesController;
```

### <a name="get_organization_licenses"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.getOrganizationLicenses") getOrganizationLicenses

> List the licenses for an organization


```javascript
function getOrganizationLicenses(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| deviceSerial |  ``` Optional ```  | Filter the licenses to those assigned to a particular device |
| networkId |  ``` Optional ```  | Filter the licenses to those assigned in a particular network |
| state |  ``` Optional ```  | Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'unused', 'unusedActive' or 'recentlyQueued' |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['perPage'] = 63;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['deviceSerial'] = 'deviceSerial';
        input['networkId'] = 'networkId';
        input['state'] = Object.keys(state)[0];

    controller.getOrganizationLicenses(input, function(error, response, context) {

    
    });
```



### <a name="assign_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.assignOrganizationLicensesSeats") assignOrganizationLicensesSeats

> Assign SM seats to a network. This will increase the managed SM device limit of the network


```javascript
function assignOrganizationLicensesSeats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| assignOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['assignOrganizationLicensesSeats'] = new AssignOrganizationLicensesSeatsModel({"key":"value"});

    controller.assignOrganizationLicensesSeats(input, function(error, response, context) {

    
    });
```



### <a name="move_organization_licenses"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.moveOrganizationLicenses") moveOrganizationLicenses

> Move licenses to another organization. This will also move any devices that the licenses are assigned to


```javascript
function moveOrganizationLicenses(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| moveOrganizationLicenses |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['moveOrganizationLicenses'] = new MoveOrganizationLicensesModel({"key":"value"});

    controller.moveOrganizationLicenses(input, function(error, response, context) {

    
    });
```



### <a name="move_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.moveOrganizationLicensesSeats") moveOrganizationLicensesSeats

> Move SM seats to another organization


```javascript
function moveOrganizationLicensesSeats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| moveOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['moveOrganizationLicensesSeats'] = new MoveOrganizationLicensesSeatsModel({"key":"value"});

    controller.moveOrganizationLicensesSeats(input, function(error, response, context) {

    
    });
```



### <a name="renew_organization_licenses_seats"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.renewOrganizationLicensesSeats") renewOrganizationLicensesSeats

> Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license


```javascript
function renewOrganizationLicensesSeats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| renewOrganizationLicensesSeats |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['renewOrganizationLicensesSeats'] = new RenewOrganizationLicensesSeatsModel({"key":"value"});

    controller.renewOrganizationLicensesSeats(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_license"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.getOrganizationLicense") getOrganizationLicense

> Display a license


```javascript
function getOrganizationLicense(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| licenseId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['licenseId'] = 'licenseId';

    controller.getOrganizationLicense(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_license"></a>![Method: ](https://apidocs.io/img/method.png ".LicensesController.updateOrganizationLicense") updateOrganizationLicense

> Update a license


```javascript
function updateOrganizationLicense(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| licenseId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationLicense |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['licenseId'] = 'licenseId';
        input['updateOrganizationLicense'] = new UpdateOrganizationLicenseModel({"key":"value"});

    controller.updateOrganizationLicense(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="link_aggregations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LinkAggregationsController") LinkAggregationsController

### Get singleton instance

The singleton instance of the ``` LinkAggregationsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.LinkAggregationsController;
```

### <a name="get_network_switch_link_aggregations"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.getNetworkSwitchLinkAggregations") getNetworkSwitchLinkAggregations

> List link aggregation groups


```javascript
function getNetworkSwitchLinkAggregations(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchLinkAggregations(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.createNetworkSwitchLinkAggregation") createNetworkSwitchLinkAggregation

> Create a link aggregation group


```javascript
function createNetworkSwitchLinkAggregation(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchLinkAggregation |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSwitchLinkAggregation'] = new CreateNetworkSwitchLinkAggregationModel({"key":"value"});

    controller.createNetworkSwitchLinkAggregation(input, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.updateNetworkSwitchLinkAggregation") updateNetworkSwitchLinkAggregation

> Update a link aggregation group


```javascript
function updateNetworkSwitchLinkAggregation(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| linkAggregationId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchLinkAggregation |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['linkAggregationId'] = 'linkAggregationId';
        input['updateNetworkSwitchLinkAggregation'] = new UpdateNetworkSwitchLinkAggregationModel({"key":"value"});

    controller.updateNetworkSwitchLinkAggregation(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_switch_link_aggregation"></a>![Method: ](https://apidocs.io/img/method.png ".LinkAggregationsController.deleteNetworkSwitchLinkAggregation") deleteNetworkSwitchLinkAggregation

> Split a link aggregation group into separate ports


```javascript
function deleteNetworkSwitchLinkAggregation(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| linkAggregationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['linkAggregationId'] = 'linkAggregationId';

    controller.deleteNetworkSwitchLinkAggregation(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mgdhcp_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGDHCPSettingsController") MGDHCPSettingsController

### Get singleton instance

The singleton instance of the ``` MGDHCPSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGDHCPSettingsController;
```

### <a name="get_network_cellular_gateway_settings_dhcp"></a>![Method: ](https://apidocs.io/img/method.png ".MGDHCPSettingsController.getNetworkCellularGatewaySettingsDhcp") getNetworkCellularGatewaySettingsDhcp

> List common DHCP settings of MGs


```javascript
function getNetworkCellularGatewaySettingsDhcp(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCellularGatewaySettingsDhcp(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_cellular_gateway_settings_dhcp"></a>![Method: ](https://apidocs.io/img/method.png ".MGDHCPSettingsController.updateNetworkCellularGatewaySettingsDhcp") updateNetworkCellularGatewaySettingsDhcp

> Update common DHCP settings of MGs


```javascript
function updateNetworkCellularGatewaySettingsDhcp(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsDhcp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkCellularGatewaySettingsDhcp'] = new UpdateNetworkCellularGatewaySettingsDhcpModel({"key":"value"});

    controller.updateNetworkCellularGatewaySettingsDhcp(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mglan_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGLANSettingsController") MGLANSettingsController

### Get singleton instance

The singleton instance of the ``` MGLANSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGLANSettingsController;
```

### <a name="get_device_cellular_gateway_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MGLANSettingsController.getDeviceCellularGatewaySettings") getDeviceCellularGatewaySettings

> Show the LAN Settings of a MG


```javascript
function getDeviceCellularGatewaySettings(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceCellularGatewaySettings(serial, function(error, response, context) {

    
    });
```



### <a name="update_device_cellular_gateway_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MGLANSettingsController.updateDeviceCellularGatewaySettings") updateDeviceCellularGatewaySettings

> Update the LAN Settings for a single MG.


```javascript
function updateDeviceCellularGatewaySettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCellularGatewaySettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['updateDeviceCellularGatewaySettings'] = new UpdateDeviceCellularGatewaySettingsModel({"key":"value"});

    controller.updateDeviceCellularGatewaySettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mg_connectivity_monitoring_destinations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGConnectivityMonitoringDestinationsController") MGConnectivityMonitoringDestinationsController

### Get singleton instance

The singleton instance of the ``` MGConnectivityMonitoringDestinationsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGConnectivityMonitoringDestinationsController;
```

### <a name="get_network_cellular_gateway_settings_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".MGConnectivityMonitoringDestinationsController.getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations") getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations

> Return the connectivity testing destinations for an MG network


```javascript
function getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_cellular_gateway_settings_connectivity_monitoring_destinations"></a>![Method: ](https://apidocs.io/img/method.png ".MGConnectivityMonitoringDestinationsController.updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations") updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations

> Update the connectivity testing destinations for an MG network


```javascript
function updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations'] = new UpdateNetworkCellularGatewaySettingsConnectivityMonitoringDestinationsModel({"key":"value"});

    controller.updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mg_port_forwarding_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGPortForwardingRulesController") MGPortForwardingRulesController

### Get singleton instance

The singleton instance of the ``` MGPortForwardingRulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGPortForwardingRulesController;
```

### <a name="get_device_cellular_gateway_settings_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MGPortForwardingRulesController.getDeviceCellularGatewaySettingsPortForwardingRules") getDeviceCellularGatewaySettingsPortForwardingRules

> Returns the port forwarding rules for a single MG.


```javascript
function getDeviceCellularGatewaySettingsPortForwardingRules(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceCellularGatewaySettingsPortForwardingRules(serial, function(error, response, context) {

    
    });
```



### <a name="update_device_cellular_gateway_settings_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MGPortForwardingRulesController.updateDeviceCellularGatewaySettingsPortForwardingRules") updateDeviceCellularGatewaySettingsPortForwardingRules

> Updates the port forwarding rules for a single MG.


```javascript
function updateDeviceCellularGatewaySettingsPortForwardingRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceCellularGatewaySettingsPortForwardingRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['updateDeviceCellularGatewaySettingsPortForwardingRules'] = new UpdateDeviceCellularGatewaySettingsPortForwardingRulesModel({"key":"value"});

    controller.updateDeviceCellularGatewaySettingsPortForwardingRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mg_subnet_pool_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGSubnetPoolSettingsController") MGSubnetPoolSettingsController

### Get singleton instance

The singleton instance of the ``` MGSubnetPoolSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGSubnetPoolSettingsController;
```

### <a name="get_network_cellular_gateway_settings_subnet_pool"></a>![Method: ](https://apidocs.io/img/method.png ".MGSubnetPoolSettingsController.getNetworkCellularGatewaySettingsSubnetPool") getNetworkCellularGatewaySettingsSubnetPool

> Return the subnet pool and mask configured for MGs in the network.


```javascript
function getNetworkCellularGatewaySettingsSubnetPool(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCellularGatewaySettingsSubnetPool(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_cellular_gateway_settings_subnet_pool"></a>![Method: ](https://apidocs.io/img/method.png ".MGSubnetPoolSettingsController.updateNetworkCellularGatewaySettingsSubnetPool") updateNetworkCellularGatewaySettingsSubnetPool

> Update the subnet pool and mask configuration for MGs in the network.


```javascript
function updateNetworkCellularGatewaySettingsSubnetPool(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsSubnetPool |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkCellularGatewaySettingsSubnetPool'] = new UpdateNetworkCellularGatewaySettingsSubnetPoolModel({"key":"value"});

    controller.updateNetworkCellularGatewaySettingsSubnetPool(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mg_uplink_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MGUplinkSettingsController") MGUplinkSettingsController

### Get singleton instance

The singleton instance of the ``` MGUplinkSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MGUplinkSettingsController;
```

### <a name="get_network_cellular_gateway_settings_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".MGUplinkSettingsController.getNetworkCellularGatewaySettingsUplink") getNetworkCellularGatewaySettingsUplink

> Returns the uplink settings for your MG network.


```javascript
function getNetworkCellularGatewaySettingsUplink(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCellularGatewaySettingsUplink(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_cellular_gateway_settings_uplink"></a>![Method: ](https://apidocs.io/img/method.png ".MGUplinkSettingsController.updateNetworkCellularGatewaySettingsUplink") updateNetworkCellularGatewaySettingsUplink

> Updates the uplink settings for your MG network.


```javascript
function updateNetworkCellularGatewaySettingsUplink(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularGatewaySettingsUplink |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkCellularGatewaySettingsUplink'] = new UpdateNetworkCellularGatewaySettingsUplinkModel({"key":"value"});

    controller.updateNetworkCellularGatewaySettingsUplink(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mrl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MRL3FirewallController") MRL3FirewallController

### Get singleton instance

The singleton instance of the ``` MRL3FirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MRL3FirewallController;
```

### <a name="get_network_ssid_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.getNetworkSsidL3FirewallRules") getNetworkSsidL3FirewallRules

> Return the L3 firewall rules for an SSID on an MR network


```javascript
function getNetworkSsidL3FirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';

    controller.getNetworkSsidL3FirewallRules(input, function(error, response, context) {

    
    });
```



### <a name="update_network_ssid_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MRL3FirewallController.updateNetworkSsidL3FirewallRules") updateNetworkSsidL3FirewallRules

> Update the L3 firewall rules of an SSID on an MR network


```javascript
function updateNetworkSsidL3FirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsidL3FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';
        input['updateNetworkSsidL3FirewallRules'] = new UpdateNetworkSsidL3FirewallRulesModel({"key":"value"});

    controller.updateNetworkSsidL3FirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mv_sense_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MVSenseController") MVSenseController

### Get singleton instance

The singleton instance of the ``` MVSenseController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MVSenseController;
```

### <a name="get_device_camera_analytics_live"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.getDeviceCameraAnalyticsLive") getDeviceCameraAnalyticsLive

> Returns live state from camera of analytics zones


```javascript
function getDeviceCameraAnalyticsLive(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceCameraAnalyticsLive(serial, function(error, response, context) {

    
    });
```



### <a name="get_device_camera_analytics_overview"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.getDeviceCameraAnalyticsOverview") getDeviceCameraAnalyticsOverview

> Returns an overview of aggregate analytics data for a timespan


```javascript
function getDeviceCameraAnalyticsOverview(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour. |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 63.762407195178;
        input['objectType'] = Object.keys(objectType)[0];

    controller.getDeviceCameraAnalyticsOverview(input, function(error, response, context) {

    
    });
```



### <a name="get_device_camera_analytics_recent"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.getDeviceCameraAnalyticsRecent") getDeviceCameraAnalyticsRecent

> Returns most recent record for analytics zones


```javascript
function getDeviceCameraAnalyticsRecent(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['objectType'] = Object.keys(objectType)[0];

    controller.getDeviceCameraAnalyticsRecent(input, function(error, response, context) {

    
    });
```



### <a name="get_device_camera_analytics_zones"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.getDeviceCameraAnalyticsZones") getDeviceCameraAnalyticsZones

> Returns all configured analytic zones for this camera


```javascript
function getDeviceCameraAnalyticsZones(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceCameraAnalyticsZones(serial, function(error, response, context) {

    
    });
```



### <a name="get_device_camera_analytics_zone_history"></a>![Method: ](https://apidocs.io/img/method.png ".MVSenseController.getDeviceCameraAnalyticsZoneHistory") getDeviceCameraAnalyticsZoneHistory

> Return historical records for analytic zones


```javascript
function getDeviceCameraAnalyticsZoneHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| zoneId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 14 hours after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour. |
| resolution |  ``` Optional ```  | The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60. |
| objectType |  ``` Optional ```  | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['zoneId'] = 'zoneId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 63.762407195178;
        input['resolution'] = 63;
        input['objectType'] = Object.keys(objectType)[0];

    controller.getDeviceCameraAnalyticsZoneHistory(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx11_nat_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MX11NATRulesController") MX11NATRulesController

### Get singleton instance

The singleton instance of the ``` MX11NATRulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MX11NATRulesController;
```

### <a name="get_network_one_to_one_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX11NATRulesController.getNetworkOneToOneNatRules") getNetworkOneToOneNatRules

> Return the 1:1 NAT mapping rules for an MX network


```javascript
function getNetworkOneToOneNatRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkOneToOneNatRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_one_to_one_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX11NATRulesController.updateNetworkOneToOneNatRules") updateNetworkOneToOneNatRules

> Set the 1:1 NAT mapping rules for an MX network


```javascript
function updateNetworkOneToOneNatRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkOneToOneNatRules |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkOneToOneNatRules'] = new UpdateNetworkOneToOneNatRulesModel({"key":"value"});

    controller.updateNetworkOneToOneNatRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx1_many_nat_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MX1ManyNATRulesController") MX1ManyNATRulesController

### Get singleton instance

The singleton instance of the ``` MX1ManyNATRulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MX1ManyNATRulesController;
```

### <a name="get_network_one_to_many_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX1ManyNATRulesController.getNetworkOneToManyNatRules") getNetworkOneToManyNatRules

> Return the 1:Many NAT mapping rules for an MX network


```javascript
function getNetworkOneToManyNatRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkOneToManyNatRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_one_to_many_nat_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MX1ManyNATRulesController.updateNetworkOneToManyNatRules") updateNetworkOneToManyNatRules

> Set the 1:Many NAT mapping rules for an MX network


```javascript
function updateNetworkOneToManyNatRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkOneToManyNatRules |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkOneToManyNatRules'] = new UpdateNetworkOneToManyNatRulesModel({"key":"value"});

    controller.updateNetworkOneToManyNatRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mxl3_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL3FirewallController") MXL3FirewallController

### Get singleton instance

The singleton instance of the ``` MXL3FirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXL3FirewallController;
```

### <a name="get_network_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.getNetworkL3FirewallRules") getNetworkL3FirewallRules

> Return the L3 firewall rules for an MX network


```javascript
function getNetworkL3FirewallRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkL3FirewallRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_l3_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL3FirewallController.updateNetworkL3FirewallRules") updateNetworkL3FirewallRules

> Update the L3 firewall rules of an MX network


```javascript
function updateNetworkL3FirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkL3FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkL3FirewallRules'] = new UpdateNetworkL3FirewallRulesModel({"key":"value"});

    controller.updateNetworkL3FirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_application_categories_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7ApplicationCategoriesController") MXL7ApplicationCategoriesController

### Get singleton instance

The singleton instance of the ``` MXL7ApplicationCategoriesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXL7ApplicationCategoriesController;
```

### <a name="get_network_l7_firewall_rules_application_categories"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7ApplicationCategoriesController.getNetworkL7FirewallRulesApplicationCategories") getNetworkL7FirewallRulesApplicationCategories

> Return the L7 firewall application categories and their associated applications for an MX network


```javascript
function getNetworkL7FirewallRulesApplicationCategories(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkL7FirewallRulesApplicationCategories(networkId, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mxl7_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXL7FirewallController") MXL7FirewallController

### Get singleton instance

The singleton instance of the ``` MXL7FirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXL7FirewallController;
```

### <a name="get_network_l7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.getNetworkL7FirewallRules") getNetworkL7FirewallRules

> List the MX L7 firewall rules for an MX network


```javascript
function getNetworkL7FirewallRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkL7FirewallRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_l7_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXL7FirewallController.updateNetworkL7FirewallRules") updateNetworkL7FirewallRules

> Update the MX L7 firewall rules for an MX network


```javascript
function updateNetworkL7FirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkL7FirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkL7FirewallRules'] = new UpdateNetworkL7FirewallRulesModel({"key":"value"});

    controller.updateNetworkL7FirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mxvlan_ports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXVLANPortsController") MXVLANPortsController

### Get singleton instance

The singleton instance of the ``` MXVLANPortsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXVLANPortsController;
```

### <a name="get_network_appliance_ports"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.getNetworkAppliancePorts") getNetworkAppliancePorts

> List per-port VLAN settings for all ports of a MX.


```javascript
function getNetworkAppliancePorts(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkAppliancePorts(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_appliance_port"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.getNetworkAppliancePort") getNetworkAppliancePort

> Return per-port VLAN settings for a single MX port.


```javascript
function getNetworkAppliancePort(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appliancePortId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['appliancePortId'] = 'appliancePortId';

    controller.getNetworkAppliancePort(input, function(error, response, context) {

    
    });
```



### <a name="update_network_appliance_port"></a>![Method: ](https://apidocs.io/img/method.png ".MXVLANPortsController.updateNetworkAppliancePort") updateNetworkAppliancePort

> Update the per-port VLAN settings for a single MX port.


```javascript
function updateNetworkAppliancePort(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appliancePortId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkAppliancePort |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['appliancePortId'] = 'appliancePortId';
        input['updateNetworkAppliancePort'] = new UpdateNetworkAppliancePortModel({"key":"value"});

    controller.updateNetworkAppliancePort(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mxvpn_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXVPNFirewallController") MXVPNFirewallController

### Get singleton instance

The singleton instance of the ``` MXVPNFirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXVPNFirewallController;
```

### <a name="get_organization_vpn_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXVPNFirewallController.getOrganizationVpnFirewallRules") getOrganizationVpnFirewallRules

> Return the firewall rules for an organization's site-to-site VPN


```javascript
function getOrganizationVpnFirewallRules(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationVpnFirewallRules(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization_vpn_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXVPNFirewallController.updateOrganizationVpnFirewallRules") updateOrganizationVpnFirewallRules

> Update the firewall rules of an organization's site-to-site VPN


```javascript
function updateOrganizationVpnFirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationVpnFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganizationVpnFirewallRules'] = new UpdateOrganizationVpnFirewallRulesModel({"key":"value"});

    controller.updateOrganizationVpnFirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx_cellular_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXCellularFirewallController") MXCellularFirewallController

### Get singleton instance

The singleton instance of the ``` MXCellularFirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXCellularFirewallController;
```

### <a name="get_network_cellular_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXCellularFirewallController.getNetworkCellularFirewallRules") getNetworkCellularFirewallRules

> Return the cellular firewall rules for an MX network


```javascript
function getNetworkCellularFirewallRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkCellularFirewallRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_cellular_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXCellularFirewallController.updateNetworkCellularFirewallRules") updateNetworkCellularFirewallRules

> Update the cellular firewall rules of an MX network


```javascript
function updateNetworkCellularFirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkCellularFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkCellularFirewallRules'] = new UpdateNetworkCellularFirewallRulesModel({"key":"value"});

    controller.updateNetworkCellularFirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx_inbound_firewall_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXInboundFirewallController") MXInboundFirewallController

### Get singleton instance

The singleton instance of the ``` MXInboundFirewallController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXInboundFirewallController;
```

### <a name="get_network_appliance_firewall_inbound_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXInboundFirewallController.getNetworkApplianceFirewallInboundFirewallRules") getNetworkApplianceFirewallInboundFirewallRules

> Return the inbound firewall rules for an MX network


```javascript
function getNetworkApplianceFirewallInboundFirewallRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkApplianceFirewallInboundFirewallRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_appliance_firewall_inbound_firewall_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXInboundFirewallController.updateNetworkApplianceFirewallInboundFirewallRules") updateNetworkApplianceFirewallInboundFirewallRules

> Update the inbound firewall rules of an MX network


```javascript
function updateNetworkApplianceFirewallInboundFirewallRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkApplianceFirewallInboundFirewallRules |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkApplianceFirewallInboundFirewallRules'] = new UpdateNetworkApplianceFirewallInboundFirewallRulesModel({"key":"value"});

    controller.updateNetworkApplianceFirewallInboundFirewallRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx_port_forwarding_rules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXPortForwardingRulesController") MXPortForwardingRulesController

### Get singleton instance

The singleton instance of the ``` MXPortForwardingRulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXPortForwardingRulesController;
```

### <a name="get_network_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXPortForwardingRulesController.getNetworkPortForwardingRules") getNetworkPortForwardingRules

> Return the port forwarding rules for an MX network


```javascript
function getNetworkPortForwardingRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkPortForwardingRules(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_port_forwarding_rules"></a>![Method: ](https://apidocs.io/img/method.png ".MXPortForwardingRulesController.updateNetworkPortForwardingRules") updateNetworkPortForwardingRules

> Update the port forwarding rules for an MX network


```javascript
function updateNetworkPortForwardingRules(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkPortForwardingRules |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkPortForwardingRules'] = new UpdateNetworkPortForwardingRulesModel({"key":"value"});

    controller.updateNetworkPortForwardingRules(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx_static_routes_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXStaticRoutesController") MXStaticRoutesController

### Get singleton instance

The singleton instance of the ``` MXStaticRoutesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXStaticRoutesController;
```

### <a name="get_network_static_routes"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.getNetworkStaticRoutes") getNetworkStaticRoutes

> List the static routes for an MX or teleworker network


```javascript
function getNetworkStaticRoutes(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkStaticRoutes(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.createNetworkStaticRoute") createNetworkStaticRoute

> Add a static route for an MX or teleworker network


```javascript
function createNetworkStaticRoute(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkStaticRoute |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkStaticRoute'] = new CreateNetworkStaticRouteModel({"key":"value"});

    controller.createNetworkStaticRoute(input, function(error, response, context) {

    
    });
```



### <a name="get_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.getNetworkStaticRoute") getNetworkStaticRoute

> Return a static route for an MX or teleworker network


```javascript
function getNetworkStaticRoute(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| staticRouteId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['staticRouteId'] = 'staticRouteId';

    controller.getNetworkStaticRoute(input, function(error, response, context) {

    
    });
```



### <a name="update_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.updateNetworkStaticRoute") updateNetworkStaticRoute

> Update a static route for an MX or teleworker network


```javascript
function updateNetworkStaticRoute(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| staticRouteId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkStaticRoute |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['staticRouteId'] = 'staticRouteId';
        input['updateNetworkStaticRoute'] = new UpdateNetworkStaticRouteModel({"key":"value"});

    controller.updateNetworkStaticRoute(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_static_route"></a>![Method: ](https://apidocs.io/img/method.png ".MXStaticRoutesController.deleteNetworkStaticRoute") deleteNetworkStaticRoute

> Delete a static route from an MX or teleworker network


```javascript
function deleteNetworkStaticRoute(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| staticRouteId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['staticRouteId'] = 'staticRouteId';

    controller.deleteNetworkStaticRoute(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="mx_warm_spare_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MXWarmSpareSettingsController") MXWarmSpareSettingsController

### Get singleton instance

The singleton instance of the ``` MXWarmSpareSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MXWarmSpareSettingsController;
```

### <a name="swap_network_warmspare"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.swapNetworkWarmspare") swapNetworkWarmspare

> Swap MX primary and warm spare appliances


```javascript
function swapNetworkWarmspare(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.swapNetworkWarmspare(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_warm_spare_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.getNetworkWarmSpareSettings") getNetworkWarmSpareSettings

> Return MX warm spare settings


```javascript
function getNetworkWarmSpareSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkWarmSpareSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_warm_spare_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MXWarmSpareSettingsController.updateNetworkWarmSpareSettings") updateNetworkWarmSpareSettings

> Update MX warm spare settings


```javascript
function updateNetworkWarmSpareSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWarmSpareSettings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkWarmSpareSettings'] = new UpdateNetworkWarmSpareSettingsModel({"key":"value"});

    controller.updateNetworkWarmSpareSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="malware_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MalwareSettingsController") MalwareSettingsController

### Get singleton instance

The singleton instance of the ``` MalwareSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MalwareSettingsController;
```

### <a name="get_network_security_malware_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MalwareSettingsController.getNetworkSecurityMalwareSettings") getNetworkSecurityMalwareSettings

> Returns all supported malware settings for an MX network


```javascript
function getNetworkSecurityMalwareSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSecurityMalwareSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_security_malware_settings"></a>![Method: ](https://apidocs.io/img/method.png ".MalwareSettingsController.updateNetworkSecurityMalwareSettings") updateNetworkSecurityMalwareSettings

> Set the supported malware settings for an MX network


```javascript
function updateNetworkSecurityMalwareSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSecurityMalwareSettings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSecurityMalwareSettings'] = new UpdateNetworkSecurityMalwareSettingsModel({"key":"value"});

    controller.updateNetworkSecurityMalwareSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="management_interface_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ManagementInterfaceSettingsController") ManagementInterfaceSettingsController

### Get singleton instance

The singleton instance of the ``` ManagementInterfaceSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.ManagementInterfaceSettingsController;
```

### <a name="get_network_device_management_interface_settings"></a>![Method: ](https://apidocs.io/img/method.png ".ManagementInterfaceSettingsController.getNetworkDeviceManagementInterfaceSettings") getNetworkDeviceManagementInterfaceSettings

> Return the management interface settings for a device


```javascript
function getNetworkDeviceManagementInterfaceSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDeviceManagementInterfaceSettings(input, function(error, response, context) {

    
    });
```



### <a name="update_network_device_management_interface_settings"></a>![Method: ](https://apidocs.io/img/method.png ".ManagementInterfaceSettingsController.updateNetworkDeviceManagementInterfaceSettings") updateNetworkDeviceManagementInterfaceSettings

> Update the management interface settings for a device


```javascript
function updateNetworkDeviceManagementInterfaceSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDeviceManagementInterfaceSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['updateNetworkDeviceManagementInterfaceSettings'] = new UpdateNetworkDeviceManagementInterfaceSettingsModel({"key":"value"});

    controller.updateNetworkDeviceManagementInterfaceSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="meraki_auth_users_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MerakiAuthUsersController") MerakiAuthUsersController

### Get singleton instance

The singleton instance of the ``` MerakiAuthUsersController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MerakiAuthUsersController;
```

### <a name="get_network_meraki_auth_users"></a>![Method: ](https://apidocs.io/img/method.png ".MerakiAuthUsersController.getNetworkMerakiAuthUsers") getNetworkMerakiAuthUsers

> List the splash or RADIUS users configured under Meraki Authentication for a network


```javascript
function getNetworkMerakiAuthUsers(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkMerakiAuthUsers(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_meraki_auth_user"></a>![Method: ](https://apidocs.io/img/method.png ".MerakiAuthUsersController.getNetworkMerakiAuthUser") getNetworkMerakiAuthUser

> Return the Meraki Auth splash or RADIUS user


```javascript
function getNetworkMerakiAuthUser(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| merakiAuthUserId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['merakiAuthUserId'] = 'merakiAuthUserId';

    controller.getNetworkMerakiAuthUser(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="monitored_media_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MonitoredMediaServersController") MonitoredMediaServersController

### Get singleton instance

The singleton instance of the ``` MonitoredMediaServersController ``` class can be accessed from the API Client.

```javascript
var controller = lib.MonitoredMediaServersController;
```

### <a name="get_organization_insight_monitored_media_servers"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.getOrganizationInsightMonitoredMediaServers") getOrganizationInsightMonitoredMediaServers

> List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.


```javascript
function getOrganizationInsightMonitoredMediaServers(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationInsightMonitoredMediaServers(organizationId, function(error, response, context) {

    
    });
```



### <a name="create_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.createOrganizationInsightMonitoredMediaServer") createOrganizationInsightMonitoredMediaServer

> Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.


```javascript
function createOrganizationInsightMonitoredMediaServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationInsightMonitoredMediaServer |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationInsightMonitoredMediaServer'] = new CreateOrganizationInsightMonitoredMediaServerModel({"key":"value"});

    controller.createOrganizationInsightMonitoredMediaServer(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.getOrganizationInsightMonitoredMediaServer") getOrganizationInsightMonitoredMediaServer

> Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.


```javascript
function getOrganizationInsightMonitoredMediaServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['monitoredMediaServerId'] = 'monitoredMediaServerId';

    controller.getOrganizationInsightMonitoredMediaServer(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.updateOrganizationInsightMonitoredMediaServer") updateOrganizationInsightMonitoredMediaServer

> Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.


```javascript
function updateOrganizationInsightMonitoredMediaServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationInsightMonitoredMediaServer |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['monitoredMediaServerId'] = 'monitoredMediaServerId';
        input['updateOrganizationInsightMonitoredMediaServer'] = new UpdateOrganizationInsightMonitoredMediaServerModel({"key":"value"});

    controller.updateOrganizationInsightMonitoredMediaServer(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization_insight_monitored_media_server"></a>![Method: ](https://apidocs.io/img/method.png ".MonitoredMediaServersController.deleteOrganizationInsightMonitoredMediaServer") deleteOrganizationInsightMonitoredMediaServer

> Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.


```javascript
function deleteOrganizationInsightMonitoredMediaServer(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| monitoredMediaServerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['monitoredMediaServerId'] = 'monitoredMediaServerId';

    controller.deleteOrganizationInsightMonitoredMediaServer(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="named_tag_scope_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NamedTagScopeController") NamedTagScopeController

### Get singleton instance

The singleton instance of the ``` NamedTagScopeController ``` class can be accessed from the API Client.

```javascript
var controller = lib.NamedTagScopeController;
```

### <a name="get_network_sm_target_groups"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.getNetworkSmTargetGroups") getNetworkSmTargetGroups

> List the target groups in this network


```javascript
function getNetworkSmTargetGroups(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| withDetails |  ``` Optional ```  | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['withDetails'] = false;

    controller.getNetworkSmTargetGroups(input, function(error, response, context) {

    
    });
```



### <a name="create_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.createNetworkSmTargetGroup") createNetworkSmTargetGroup

> Add a target group


```javascript
function createNetworkSmTargetGroup(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmTargetGroup |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSmTargetGroup'] = new CreateNetworkSmTargetGroupModel({"key":"value"});

    controller.createNetworkSmTargetGroup(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.getNetworkSmTargetGroup") getNetworkSmTargetGroup

> Return a target group


```javascript
function getNetworkSmTargetGroup(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |
| withDetails |  ``` Optional ```  | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['targetGroupId'] = 'targetGroupId';
        input['withDetails'] = false;

    controller.getNetworkSmTargetGroup(input, function(error, response, context) {

    
    });
```



### <a name="update_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.updateNetworkSmTargetGroup") updateNetworkSmTargetGroup

> Update a target group


```javascript
function updateNetworkSmTargetGroup(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmTargetGroup |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['targetGroupId'] = 'targetGroupId';
        input['updateNetworkSmTargetGroup'] = new UpdateNetworkSmTargetGroupModel({"key":"value"});

    controller.updateNetworkSmTargetGroup(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_sm_target_group"></a>![Method: ](https://apidocs.io/img/method.png ".NamedTagScopeController.deleteNetworkSmTargetGroup") deleteNetworkSmTargetGroup

> Delete a target group from a network


```javascript
function deleteNetworkSmTargetGroup(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| targetGroupId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['targetGroupId'] = 'targetGroupId';

    controller.deleteNetworkSmTargetGroup(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="netflow_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NetflowSettingsController") NetflowSettingsController

### Get singleton instance

The singleton instance of the ``` NetflowSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.NetflowSettingsController;
```

### <a name="get_network_netflow_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetflowSettingsController.getNetwork_netflow_Settings") getNetwork_netflow_Settings

> Return the NetFlow traffic reporting settings for a network


```javascript
function getNetwork_netflow_Settings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetwork_netflow_Settings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_netflow_settings"></a>![Method: ](https://apidocs.io/img/method.png ".NetflowSettingsController.updateNetwork_netflow_Settings") updateNetwork_netflow_Settings

> Update the NetFlow traffic reporting settings for a network


```javascript
function updateNetwork_netflow_Settings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_netflow_Settings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetwork_netflow_Settings'] = new UpdateNetworkNetflowSettingsModel({"key":"value"});

    controller.updateNetwork_netflow_Settings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="networks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".NetworksController") NetworksController

### Get singleton instance

The singleton instance of the ``` NetworksController ``` class can be accessed from the API Client.

```javascript
var controller = lib.NetworksController;
```

### <a name="get_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getNetwork") getNetwork

> Return a network


```javascript
function getNetwork(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetwork(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.updateNetwork") updateNetwork

> Update a network


```javascript
function updateNetwork(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetwork'] = new UpdateNetworkModel({"key":"value"});

    controller.updateNetwork(input, function(error, response, context) {

    
    });
```



### <a name="delete_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.deleteNetwork") deleteNetwork

> Delete a network


```javascript
function deleteNetwork(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.deleteNetwork(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_access_policies"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getNetworkAccessPolicies") getNetworkAccessPolicies

> List the access policies for this network. Only valid for MS networks.


```javascript
function getNetworkAccessPolicies(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkAccessPolicies(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_air_marshal"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getNetworkAirMarshal") getNetworkAirMarshal

> List Air Marshal scan results from a network


```javascript
function getNetworkAirMarshal(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['timespan'] = 63.762407195178;

    controller.getNetworkAirMarshal(input, function(error, response, context) {

    
    });
```



### <a name="bind_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.bindNetwork") bindNetwork

> Bind a network to a template.


```javascript
function bindNetwork(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bindNetwork |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['bindNetwork'] = new BindNetworkModel({"key":"value"});

    controller.bindNetwork(input, function(error, response, context) {

    
    });
```



### <a name="get_network_site_to_site_vpn"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getNetworkSiteToSiteVpn") getNetworkSiteToSiteVpn

> Return the site-to-site VPN settings of a network. Only valid for MX networks.


```javascript
function getNetworkSiteToSiteVpn(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSiteToSiteVpn(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_site_to_site_vpn"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.updateNetworkSiteToSiteVpn") updateNetworkSiteToSiteVpn

> Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.


```javascript
function updateNetworkSiteToSiteVpn(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSiteToSiteVpn |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSiteToSiteVpn'] = new UpdateNetworkSiteToSiteVpnModel({"key":"value"});

    controller.updateNetworkSiteToSiteVpn(input, function(error, response, context) {

    
    });
```



### <a name="split_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.splitNetwork") splitNetwork

> Split a combined network into individual networks for each type of device


```javascript
function splitNetwork(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.splitNetwork(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_traffic"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getNetworkTraffic") getNetworkTraffic

>     The traffic analysis data for this network.
>     <a href="https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility">Traffic Analysis with Hostname Visibility</a> must be enabled on the network.
> 


```javascript
function getNetworkTraffic(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 30 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. |
| deviceType |  ``` Optional ```  | Filter the data by device type: combined (default), wireless, switch, appliance.
    When using combined, for each rule the data will come from the device type with the most usage. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['timespan'] = 63.762407195178;
        input['deviceType'] = 'deviceType';

    controller.getNetworkTraffic(input, function(error, response, context) {

    
    });
```



### <a name="unbind_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.unbindNetwork") unbindNetwork

> Unbind a network from a template.


```javascript
function unbindNetwork(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.unbindNetwork(networkId, function(error, response, context) {

    
    });
```



### <a name="get_organization_networks"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.getOrganizationNetworks") getOrganizationNetworks

> List the networks in an organization


```javascript
function getOrganizationNetworks(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Optional ```  | An optional parameter that is the ID of a config template. Will return all networks bound to that template. |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['configTemplateId'] = 'configTemplateId';

    controller.getOrganizationNetworks(input, function(error, response, context) {

    
    });
```



### <a name="create_organization_network"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.createOrganizationNetwork") createOrganizationNetwork

> Create a network


```javascript
function createOrganizationNetwork(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationNetwork |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationNetwork'] = new CreateOrganizationNetworkModel({"key":"value"});

    controller.createOrganizationNetwork(input, function(error, response, context) {

    
    });
```



### <a name="combine_organization_networks"></a>![Method: ](https://apidocs.io/img/method.png ".NetworksController.combineOrganizationNetworks") combineOrganizationNetworks

> Combine multiple networks into a single network


```javascript
function combineOrganizationNetworks(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| combineOrganizationNetworks |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['combineOrganizationNetworks'] = new CombineOrganizationNetworksModel({"key":"value"});

    controller.combineOrganizationNetworks(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="open_api_spec_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OpenAPISpecController") OpenAPISpecController

### Get singleton instance

The singleton instance of the ``` OpenAPISpecController ``` class can be accessed from the API Client.

```javascript
var controller = lib.OpenAPISpecController;
```

### <a name="get_organization_openapi_spec"></a>![Method: ](https://apidocs.io/img/method.png ".OpenAPISpecController.getOrganizationOpenapiSpec") getOrganizationOpenapiSpec

> Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON


```javascript
function getOrganizationOpenapiSpec(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationOpenapiSpec(organizationId, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="organizations_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OrganizationsController") OrganizationsController

### Get singleton instance

The singleton instance of the ``` OrganizationsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.OrganizationsController;
```

### <a name="get_organizations"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizations") getOrganizations

> List the organizations that the user has privileges on


```javascript
function getOrganizations(callback)
```

#### Example Usage

```javascript


    controller.getOrganizations(function(error, response, context) {

    
    });
```



### <a name="create_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.createOrganization") createOrganization

> Create a new organization


```javascript
function createOrganization(createOrganization, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| createOrganization |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var createOrganization = new CreateOrganizationModel({"key":"value"});

    controller.createOrganization(createOrganization, function(error, response, context) {

    
    });
```



### <a name="get_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganization") getOrganization

> Return an organization


```javascript
function getOrganization(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganization(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.updateOrganization") updateOrganization

> Update an organization


```javascript
function updateOrganization(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganization'] = new UpdateOrganizationModel({"key":"value"});

    controller.updateOrganization(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.deleteOrganization") deleteOrganization

> Delete an organization


```javascript
function deleteOrganization(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.deleteOrganization(organizationId, function(error, response, context) {

    
    });
```



### <a name="claim_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.claimOrganization") claimOrganization

> Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization's inventory.


```javascript
function claimOrganization(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| claimOrganization |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['claimOrganization'] = new ClaimOrganizationModel({"key":"value"});

    controller.claimOrganization(input, function(error, response, context) {

    
    });
```



### <a name="clone_organization"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.cloneOrganization") cloneOrganization

> Create a new organization by cloning the addressed organization


```javascript
function cloneOrganization(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| cloneOrganization |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['cloneOrganization'] = new CloneOrganizationModel({"key":"value"});

    controller.cloneOrganization(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_device_statuses"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizationDeviceStatuses") getOrganizationDeviceStatuses

> List the status of every Meraki device in the organization


```javascript
function getOrganizationDeviceStatuses(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationDeviceStatuses(organizationId, function(error, response, context) {

    
    });
```



### <a name="get_organization_inventory"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizationInventory") getOrganizationInventory

> Return the inventory for an organization


```javascript
function getOrganizationInventory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| includeLicenseInfo |  ``` Optional ```  | When this parameter is true, each entity in the response will include the license expiration date of the device (if any). Only applies to organizations that support per-device licensing. Defaults to false. |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['includeLicenseInfo'] = false;

    controller.getOrganizationInventory(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_license_state"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizationLicenseState") getOrganizationLicenseState

> Return an overview of the license state for an organization


```javascript
function getOrganizationLicenseState(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationLicenseState(organizationId, function(error, response, context) {

    
    });
```



### <a name="get_organization_third_party_vpn_peers"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizationThirdPartyVPNPeers") getOrganizationThirdPartyVPNPeers

> Return the third party VPN peers for an organization


```javascript
function getOrganizationThirdPartyVPNPeers(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationThirdPartyVPNPeers(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization_third_party_vpn_peers"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.updateOrganizationThirdPartyVPNPeers") updateOrganizationThirdPartyVPNPeers

> Update the third party VPN peers for an organization


```javascript
function updateOrganizationThirdPartyVPNPeers(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationThirdPartyVPNPeers |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganizationThirdPartyVPNPeers'] = new UpdateOrganizationThirdPartyVPNPeersModel({"key":"value"});

    controller.updateOrganizationThirdPartyVPNPeers(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_uplinks_loss_and_latency"></a>![Method: ](https://apidocs.io/img/method.png ".OrganizationsController.getOrganizationUplinksLossAndLatency") getOrganizationUplinksLossAndLatency

> Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago


```javascript
function getOrganizationUplinksLossAndLatency(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes. |
| uplink |  ``` Optional ```  | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks. |
| ip |  ``` Optional ```  | Optional filter for a specific destination IP. Default will return all destination IPs. |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 63.762407195178;
        input['uplink'] = Object.keys(uplink)[0];
        input['ip'] = 'ip';

    controller.getOrganizationUplinksLossAndLatency(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="pii_controller"></a>![Class: ](https://apidocs.io/img/class.png ".PIIController") PIIController

### Get singleton instance

The singleton instance of the ``` PIIController ``` class can be accessed from the API Client.

```javascript
var controller = lib.PIIController;
```

### <a name="get_network_pii_pii_keys"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.getNetworkPiiPiiKeys") getNetworkPiiPiiKeys

> List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/piiKeys
> ```


```javascript
function getNetworkPiiPiiKeys(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['username'] = 'username';
        input['email'] = 'email';
        input['mac'] = 'mac';
        input['serial'] = 'serial';
        input['imei'] = 'imei';
        input['bluetoothMac'] = 'bluetoothMac';

    controller.getNetworkPiiPiiKeys(input, function(error, response, context) {

    
    });
```



### <a name="get_network_pii_requests"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.getNetworkPiiRequests") getNetworkPiiRequests

> List the PII requests for this network or organization
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests
> ```


```javascript
function getNetworkPiiRequests(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkPiiRequests(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.createNetworkPiiRequest") createNetworkPiiRequest

> Submit a new delete or restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests
> ```


```javascript
function createNetworkPiiRequest(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkPiiRequest |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkPiiRequest'] = new CreateNetworkPiiRequestModel({"key":"value"});

    controller.createNetworkPiiRequest(input, function(error, response, context) {

    
    });
```



### <a name="get_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.getNetworkPiiRequest") getNetworkPiiRequest

> Return a PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{requestId}
> ```


```javascript
function getNetworkPiiRequest(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| requestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['requestId'] = 'requestId';

    controller.getNetworkPiiRequest(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_pii_request"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.deleteNetworkPiiRequest") deleteNetworkPiiRequest

> Delete a restrict processing PII request
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/requests/{requestId}
> ```


```javascript
function deleteNetworkPiiRequest(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| requestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['requestId'] = 'requestId';

    controller.deleteNetworkPiiRequest(input, function(error, response, context) {

    
    });
```



### <a name="get_network_pii_sm_devices_for_key"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.getNetworkPiiSmDevicesForKey") getNetworkPiiSmDevicesForKey

> Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/smDevicesForKey
> ```


```javascript
function getNetworkPiiSmDevicesForKey(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['username'] = 'username';
        input['email'] = 'email';
        input['mac'] = 'mac';
        input['serial'] = 'serial';
        input['imei'] = 'imei';
        input['bluetoothMac'] = 'bluetoothMac';

    controller.getNetworkPiiSmDevicesForKey(input, function(error, response, context) {

    
    });
```



### <a name="get_network_pii_sm_owners_for_key"></a>![Method: ](https://apidocs.io/img/method.png ".PIIController.getNetworkPiiSmOwnersForKey") getNetworkPiiSmOwnersForKey

> Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.
> 
> ## ALTERNATE PATH
> 
> ```
> /organizations/{organizationId}/pii/smOwnersForKey
> ```


```javascript
function getNetworkPiiSmOwnersForKey(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| username |  ``` Optional ```  | The username of a Systems Manager user |
| email |  ``` Optional ```  | The email of a network user account or a Systems Manager device |
| mac |  ``` Optional ```  | The MAC of a network client device or a Systems Manager device |
| serial |  ``` Optional ```  | The serial of a Systems Manager device |
| imei |  ``` Optional ```  | The IMEI of a Systems Manager device |
| bluetoothMac |  ``` Optional ```  | The MAC of a Bluetooth client |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['username'] = 'username';
        input['email'] = 'email';
        input['mac'] = 'mac';
        input['serial'] = 'serial';
        input['imei'] = 'imei';
        input['bluetoothMac'] = 'bluetoothMac';

    controller.getNetworkPiiSmOwnersForKey(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="radio_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RadioSettingsController") RadioSettingsController

### Get singleton instance

The singleton instance of the ``` RadioSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.RadioSettingsController;
```

### <a name="get_network_device_wireless_radio_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.getNetworkDeviceWirelessRadioSettings") getNetworkDeviceWirelessRadioSettings

> Return the radio settings of a device


```javascript
function getNetworkDeviceWirelessRadioSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDeviceWirelessRadioSettings(input, function(error, response, context) {

    
    });
```



### <a name="update_network_device_wireless_radio_settings"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.updateNetworkDeviceWirelessRadioSettings") updateNetworkDeviceWirelessRadioSettings

> Update the radio settings of a device


```javascript
function updateNetworkDeviceWirelessRadioSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkDeviceWirelessRadioSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['updateNetworkDeviceWirelessRadioSettings'] = new UpdateNetworkDeviceWirelessRadioSettingsModel({"key":"value"});

    controller.updateNetworkDeviceWirelessRadioSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_network_wireless_rf_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.getNetworkWirelessRfProfiles") getNetworkWirelessRfProfiles

> List the non-basic RF profiles for this network


```javascript
function getNetworkWirelessRfProfiles(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| includeTemplateProfiles |  ``` Optional ```  | If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template
    should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['includeTemplateProfiles'] = false;

    controller.getNetworkWirelessRfProfiles(input, function(error, response, context) {

    
    });
```



### <a name="create_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.createNetworkWirelessRfProfile") createNetworkWirelessRfProfile

> Creates new RF profile for this network


```javascript
function createNetworkWirelessRfProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkWirelessRfProfile |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkWirelessRfProfile'] = new CreateNetworkWirelessRfProfileModel({"key":"value"});

    controller.createNetworkWirelessRfProfile(input, function(error, response, context) {

    
    });
```



### <a name="update_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.updateNetworkWirelessRfProfile") updateNetworkWirelessRfProfile

> Updates specified RF profile for this network


```javascript
function updateNetworkWirelessRfProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWirelessRfProfile |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['rfProfileId'] = 'rfProfileId';
        input['updateNetworkWirelessRfProfile'] = new UpdateNetworkWirelessRfProfileModel({"key":"value"});

    controller.updateNetworkWirelessRfProfile(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.deleteNetworkWirelessRfProfile") deleteNetworkWirelessRfProfile

> Delete a RF Profile


```javascript
function deleteNetworkWirelessRfProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['rfProfileId'] = 'rfProfileId';

    controller.deleteNetworkWirelessRfProfile(input, function(error, response, context) {

    
    });
```



### <a name="get_network_wireless_rf_profile"></a>![Method: ](https://apidocs.io/img/method.png ".RadioSettingsController.getNetworkWirelessRfProfile") getNetworkWirelessRfProfile

> Return a RF profile


```javascript
function getNetworkWirelessRfProfile(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| rfProfileId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['rfProfileId'] = 'rfProfileId';

    controller.getNetworkWirelessRfProfile(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="saml_roles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SAMLRolesController") SAMLRolesController

### Get singleton instance

The singleton instance of the ``` SAMLRolesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SAMLRolesController;
```

### <a name="get_organization_saml_roles"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.getOrganizationSamlRoles") getOrganizationSamlRoles

> List the SAML roles for this organization


```javascript
function getOrganizationSamlRoles(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationSamlRoles(organizationId, function(error, response, context) {

    
    });
```



### <a name="create_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.createOrganizationSamlRole") createOrganizationSamlRole

> Create a SAML role


```javascript
function createOrganizationSamlRole(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| createOrganizationSamlRole |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['createOrganizationSamlRole'] = new CreateOrganizationSamlRoleModel({"key":"value"});

    controller.createOrganizationSamlRole(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.getOrganizationSamlRole") getOrganizationSamlRole

> Return a SAML role


```javascript
function getOrganizationSamlRole(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['samlRoleId'] = 'samlRoleId';

    controller.getOrganizationSamlRole(input, function(error, response, context) {

    
    });
```



### <a name="update_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.updateOrganizationSamlRole") updateOrganizationSamlRole

> Update a SAML role


```javascript
function updateOrganizationSamlRole(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSamlRole |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['samlRoleId'] = 'samlRoleId';
        input['updateOrganizationSamlRole'] = new UpdateOrganizationSamlRoleModel({"key":"value"});

    controller.updateOrganizationSamlRole(input, function(error, response, context) {

    
    });
```



### <a name="delete_organization_saml_role"></a>![Method: ](https://apidocs.io/img/method.png ".SAMLRolesController.deleteOrganizationSamlRole") deleteOrganizationSamlRole

> Remove a SAML role


```javascript
function deleteOrganizationSamlRole(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| samlRoleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['samlRoleId'] = 'samlRoleId';

    controller.deleteOrganizationSamlRole(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="sm_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SMController") SMController

### Get singleton instance

The singleton instance of the ``` SMController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SMController;
```

### <a name="create_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.createNetworkSmAppPolaris") createNetworkSmAppPolaris

> Create a new Polaris app


```javascript
function createNetworkSmAppPolaris(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmAppPolaris |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSmAppPolaris'] = new CreateNetworkSmAppPolarisModel({"key":"value"});

    controller.createNetworkSmAppPolaris(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmAppPolaris") getNetworkSmAppPolaris

> Get details for a Cisco Polaris app if it exists


```javascript
function getNetworkSmAppPolaris(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| bundleId |  ``` Optional ```  | The bundle ID of the app to be found, defaults to com.cisco.ciscosecurity.app |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['bundleId'] = 'bundleId';

    controller.getNetworkSmAppPolaris(input, function(error, response, context) {

    
    });
```



### <a name="update_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.updateNetworkSmAppPolaris") updateNetworkSmAppPolaris

> Update an existing Polaris app


```javascript
function updateNetworkSmAppPolaris(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmAppPolaris |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['appId'] = 'appId';
        input['updateNetworkSmAppPolaris'] = new UpdateNetworkSmAppPolarisModel({"key":"value"});

    controller.updateNetworkSmAppPolaris(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_sm_app_polaris"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.deleteNetworkSmAppPolaris") deleteNetworkSmAppPolaris

> Delete a Cisco Polaris app


```javascript
function deleteNetworkSmAppPolaris(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| appId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['appId'] = 'appId';

    controller.deleteNetworkSmAppPolaris(input, function(error, response, context) {

    
    });
```



### <a name="create_network_sm_bypass_activation_lock_attempt"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.createNetworkSmBypassActivationLockAttempt") createNetworkSmBypassActivationLockAttempt

> Bypass activation lock attempt


```javascript
function createNetworkSmBypassActivationLockAttempt(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSmBypassActivationLockAttempt |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSmBypassActivationLockAttempt'] = new CreateNetworkSmBypassActivationLockAttemptModel({"key":"value"});

    controller.createNetworkSmBypassActivationLockAttempt(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_bypass_activation_lock_attempt"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmBypassActivationLockAttempt") getNetworkSmBypassActivationLockAttempt

> Bypass activation lock attempt status


```javascript
function getNetworkSmBypassActivationLockAttempt(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| attemptId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['attemptId'] = 'attemptId';

    controller.getNetworkSmBypassActivationLockAttempt(input, function(error, response, context) {

    
    });
```



### <a name="update_network_sm_device_fields"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.updateNetworkSmDeviceFields") updateNetworkSmDeviceFields

> Modify the fields of a device


```javascript
function updateNetworkSmDeviceFields(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDeviceFields |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSmDeviceFields'] = new UpdateNetworkSmDeviceFieldsModel({"key":"value"});

    controller.updateNetworkSmDeviceFields(input, function(error, response, context) {

    
    });
```



### <a name="wipe_network_sm_device"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.wipeNetworkSmDevice") wipeNetworkSmDevice

> Wipe a device


```javascript
function wipeNetworkSmDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| wipeNetworkSmDevice |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['wipeNetworkSmDevice'] = new WipeNetworkSmDeviceModel({"key":"value"});

    controller.wipeNetworkSmDevice(input, function(error, response, context) {

    
    });
```



### <a name="refresh_network_sm_device_details"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.refreshNetworkSmDeviceDetails") refreshNetworkSmDeviceDetails

> Refresh the details of a device


```javascript
function refreshNetworkSmDeviceDetails(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.refreshNetworkSmDeviceDetails(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmDevices") getNetworkSmDevices

> List the devices enrolled in an SM network with various specified fields and filters


```javascript
function getNetworkSmDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| fields |  ``` Optional ```  | Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.
    The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
    systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
    ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
    simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
    isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
    hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion. |
| wifiMacs |  ``` Optional ```  | Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values. |
| serials |  ``` Optional ```  | Filter devices by serial(s). Multiple serials can be passed in as comma separated values. |
| ids |  ``` Optional ```  | Filter devices by id(s). Multiple ids can be passed in as comma separated values. |
| scope |  ``` Optional ```  | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values. |
| batchSize |  ``` Optional ```  | Number of devices to return, 1000 is the default as well as the max. |
| batchToken |  ``` Optional ```  | If the network has more devices than the batch size, a batch token will be returned
    as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.
    Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in
    with the original request. Additional parameters passed in with the batchToken will be ignored. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['fields'] = 'fields';
        input['wifiMacs'] = 'wifiMacs';
        input['serials'] = 'serials';
        input['ids'] = 'ids';
        input['scope'] = 'scope';
        input['batchSize'] = 22;
        input['batchToken'] = 'batchToken';

    controller.getNetworkSmDevices(input, function(error, response, context) {

    
    });
```



### <a name="checkin_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.checkinNetworkSmDevices") checkinNetworkSmDevices

> Force check-in a set of devices


```javascript
function checkinNetworkSmDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| checkinNetworkSmDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['checkinNetworkSmDevices'] = new CheckinNetworkSmDevicesModel({"key":"value"});

    controller.checkinNetworkSmDevices(input, function(error, response, context) {

    
    });
```



### <a name="move_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.moveNetworkSmDevices") moveNetworkSmDevices

> Move a set of devices to a new network


```javascript
function moveNetworkSmDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| moveNetworkSmDevices |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['moveNetworkSmDevices'] = new MoveNetworkSmDevicesModel({"key":"value"});

    controller.moveNetworkSmDevices(input, function(error, response, context) {

    
    });
```



### <a name="update_network_sm_devices_tags"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.updateNetworkSmDevicesTags") updateNetworkSmDevicesTags

> Add, delete, or update the tags of a set of devices


```javascript
function updateNetworkSmDevicesTags(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSmDevicesTags |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSmDevicesTags'] = new UpdateNetworkSmDevicesTagsModel({"key":"value"});

    controller.updateNetworkSmDevicesTags(input, function(error, response, context) {

    
    });
```



### <a name="unenroll_network_sm_device"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.unenrollNetworkSmDevice") unenrollNetworkSmDevice

> Unenroll a device


```javascript
function unenrollNetworkSmDevice(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.unenrollNetworkSmDevice(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmProfiles") getNetworkSmProfiles

> List all the profiles in the network


```javascript
function getNetworkSmProfiles(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSmProfiles(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_user_device_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmUserDeviceProfiles") getNetworkSmUserDeviceProfiles

> Get the profiles associated with a user


```javascript
function getNetworkSmUserDeviceProfiles(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['userId'] = 'userId';

    controller.getNetworkSmUserDeviceProfiles(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_user_softwares"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmUserSoftwares") getNetworkSmUserSoftwares

> Get a list of softwares associated with a user


```javascript
function getNetworkSmUserSoftwares(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| userId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['userId'] = 'userId';

    controller.getNetworkSmUserSoftwares(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_users"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmUsers") getNetworkSmUsers

> List the owners in an SM network with various specified fields and filters


```javascript
function getNetworkSmUsers(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| ids |  ``` Optional ```  | Filter users by id(s). Multiple ids can be passed in as comma separated values. |
| usernames |  ``` Optional ```  | Filter users by username(s). Multiple usernames can be passed in as comma separated values. |
| emails |  ``` Optional ```  | Filter users by email(s). Multiple emails can be passed in as comma separated values. |
| scope |  ``` Optional ```  | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['ids'] = 'ids';
        input['usernames'] = 'usernames';
        input['emails'] = 'emails';
        input['scope'] = 'scope';

    controller.getNetworkSmUsers(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_cellular_usage_history"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmCellularUsageHistory") getNetworkSmCellularUsageHistory

> Return the client's daily cellular data usage history. Usage data is in kilobytes.


```javascript
function getNetworkSmCellularUsageHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmCellularUsageHistory(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_certs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmCerts") getNetworkSmCerts

> List the certs on a device


```javascript
function getNetworkSmCerts(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmCerts(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_device_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmDeviceProfiles") getNetworkSmDeviceProfiles

> Get the profiles associated with a device


```javascript
function getNetworkSmDeviceProfiles(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmDeviceProfiles(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_network_adapters"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmNetworkAdapters") getNetworkSmNetworkAdapters

> List the network adapters of a device


```javascript
function getNetworkSmNetworkAdapters(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmNetworkAdapters(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_restrictions"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmRestrictions") getNetworkSmRestrictions

> List the restrictions on a device


```javascript
function getNetworkSmRestrictions(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmRestrictions(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_security_centers"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmSecurityCenters") getNetworkSmSecurityCenters

> List the security centers on a device


```javascript
function getNetworkSmSecurityCenters(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmSecurityCenters(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_softwares"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmSoftwares") getNetworkSmSoftwares

> Get a list of softwares associated with a device


```javascript
function getNetworkSmSoftwares(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmSoftwares(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_wlan_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmWlanLists") getNetworkSmWlanLists

> List the saved SSID names on a device


```javascript
function getNetworkSmWlanLists(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| deviceId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['deviceId'] = 'deviceId';

    controller.getNetworkSmWlanLists(input, function(error, response, context) {

    
    });
```



### <a name="lock_network_sm_devices"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.lockNetworkSmDevices") lockNetworkSmDevices

> Lock a set of devices


```javascript
function lockNetworkSmDevices(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| lockNetworkSmDevices |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = network_id;
        input['lockNetworkSmDevices'] = new LockNetworkSmDevicesModel({"key":"value"});

    controller.lockNetworkSmDevices(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_connectivity"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmConnectivity") getNetworkSmConnectivity

> Returns historical connectivity data (whether a device is regularly checking in to Dashboard).


```javascript
function getNetworkSmConnectivity(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = network_id;
        input['id'] = 'id';
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkSmConnectivity(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_desktop_logs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmDesktopLogs") getNetworkSmDesktopLogs

> Return historical records of various Systems Manager network connection details for desktop devices.


```javascript
function getNetworkSmDesktopLogs(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = network_id;
        input['id'] = 'id';
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkSmDesktopLogs(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_device_command_logs"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmDeviceCommandLogs") getNetworkSmDeviceCommandLogs

>     Return historical records of commands sent to Systems Manager devices.
>     <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
>     by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
>     of any reports.</p>
> 


```javascript
function getNetworkSmDeviceCommandLogs(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = network_id;
        input['id'] = 'id';
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkSmDeviceCommandLogs(input, function(error, response, context) {

    
    });
```



### <a name="get_network_sm_performance_history"></a>![Method: ](https://apidocs.io/img/method.png ".SMController.getNetworkSmPerformanceHistory") getNetworkSmPerformanceHistory

> Return historical records of various Systems Manager client metrics for desktop devices.


```javascript
function getNetworkSmPerformanceHistory(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| id |  ``` Required ```  | TODO: Add a parameter description |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = network_id;
        input['id'] = 'id';
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkSmPerformanceHistory(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="snmp_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SNMPSettingsController") SNMPSettingsController

### Get singleton instance

The singleton instance of the ``` SNMPSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SNMPSettingsController;
```

### <a name="get_network_snmp_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.getNetworkSnmpSettings") getNetworkSnmpSettings

> Return the SNMP settings for a network


```javascript
function getNetworkSnmpSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSnmpSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_snmp_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.updateNetworkSnmpSettings") updateNetworkSnmpSettings

> Update the SNMP settings for a network


```javascript
function updateNetworkSnmpSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSnmpSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSnmpSettings'] = new UpdateNetworkSnmpSettingsModel({"key":"value"});

    controller.updateNetworkSnmpSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.getOrganizationSnmp") getOrganizationSnmp

> Return the SNMP settings for an organization


```javascript
function getOrganizationSnmp(organizationId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var organizationId = 'organizationId';

    controller.getOrganizationSnmp(organizationId, function(error, response, context) {

    
    });
```



### <a name="update_organization_snmp"></a>![Method: ](https://apidocs.io/img/method.png ".SNMPSettingsController.updateOrganizationSnmp") updateOrganizationSnmp

> Update the SNMP settings for an organization


```javascript
function updateOrganizationSnmp(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| updateOrganizationSnmp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['updateOrganizationSnmp'] = new UpdateOrganizationSnmpModel({"key":"value"});

    controller.updateOrganizationSnmp(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="ssids_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SsidsController") SsidsController

### Get singleton instance

The singleton instance of the ``` SsidsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SsidsController;
```

### <a name="get_network_device_wireless_status"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.getNetworkDeviceWirelessStatus") getNetworkDeviceWirelessStatus

> Return the SSID statuses of an access point


```javascript
function getNetworkDeviceWirelessStatus(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';

    controller.getNetworkDeviceWirelessStatus(input, function(error, response, context) {

    
    });
```



### <a name="get_network_ssids"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.getNetwork_ssids") getNetwork_ssids

> List the SSIDs in a network. Supports networks with access points or wireless-enabled security appliances and teleworker gateways.


```javascript
function getNetwork_ssids(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetwork_ssids(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_ssid"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.getNetworkSsid") getNetworkSsid

> Return a single SSID


```javascript
function getNetworkSsid(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';

    controller.getNetworkSsid(input, function(error, response, context) {

    
    });
```



### <a name="update_network_ssid"></a>![Method: ](https://apidocs.io/img/method.png ".SsidsController.updateNetworkSsid") updateNetworkSsid

> Update the attributes of an SSID


```javascript
function updateNetworkSsid(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsid |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';
        input['updateNetworkSsid'] = new UpdateNetworkSsidModel({"key":"value"});

    controller.updateNetworkSsid(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="security_events_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SecurityEventsController") SecurityEventsController

### Get singleton instance

The singleton instance of the ``` SecurityEventsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SecurityEventsController;
```

### <a name="get_network_client_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.getNetworkClientSecurityEvents") getNetworkClientSecurityEvents

> List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.


```javascript
function getNetworkClientSecurityEvents(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 791 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 791 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkClientSecurityEvents(input, function(error, response, context) {

    
    });
```



### <a name="get_network_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.getNetworkSecurityEvents") getNetworkSecurityEvents

> List the security events for a network


```javascript
function getNetworkSecurityEvents(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 365 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getNetworkSecurityEvents(input, function(error, response, context) {

    
    });
```



### <a name="get_organization_security_events"></a>![Method: ](https://apidocs.io/img/method.png ".SecurityEventsController.getOrganizationSecurityEvents") getOrganizationSecurityEvents

> List the security events for an organization


```javascript
function getOrganizationSecurityEvents(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 365 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 365 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';

    controller.getOrganizationSecurityEvents(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="splash_login_attempts_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SplashLoginAttemptsController") SplashLoginAttemptsController

### Get singleton instance

The singleton instance of the ``` SplashLoginAttemptsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SplashLoginAttemptsController;
```

### <a name="get_network_splash_login_attempts"></a>![Method: ](https://apidocs.io/img/method.png ".SplashLoginAttemptsController.getNetworkSplashLoginAttempts") getNetworkSplashLoginAttempts

> List the splash login attempts for a network


```javascript
function getNetworkSplashLoginAttempts(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| ssidNumber |  ``` Optional ```  | Only return the login attempts for the specified SSID |
| loginIdentifier |  ``` Optional ```  | The username, email, or phone number used during login |
| timespan |  ``` Optional ```  | The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['ssidNumber'] = Object.keys(ssidNumber)[0];
        input['loginIdentifier'] = 'loginIdentifier';
        input['timespan'] = 22;

    controller.getNetworkSplashLoginAttempts(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="splash_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SplashSettingsController") SplashSettingsController

### Get singleton instance

The singleton instance of the ``` SplashSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SplashSettingsController;
```

### <a name="get_network_ssids_plash_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SplashSettingsController.getNetwork_ssids_PlashSettings") getNetwork_ssids_PlashSettings

> Display the splash page settings for the given SSID


```javascript
function getNetwork_ssids_PlashSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';

    controller.getNetwork_ssids_PlashSettings(input, function(error, response, context) {

    
    });
```



### <a name="update_network_ssids_plash_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SplashSettingsController.updateNetwork_ssids_PlashSettings") updateNetwork_ssids_PlashSettings

> Modify the splash page settings for the given SSID


```javascript
function updateNetwork_ssids_PlashSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_ssids_PlashSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';
        input['updateNetwork_ssids_PlashSettings'] = new UpdateNetworkSsidsPlashSettingsModel({"key":"value"});

    controller.updateNetwork_ssids_PlashSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_acls_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchAclsController") SwitchAclsController

### Get singleton instance

The singleton instance of the ``` SwitchAclsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchAclsController;
```

### <a name="get_network_switch_access_control_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchAclsController.getNetworkSwitchAccessControlLists") getNetworkSwitchAccessControlLists

> Return the access control lists for a MS network


```javascript
function getNetworkSwitchAccessControlLists(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchAccessControlLists(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_access_control_lists"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchAclsController.updateNetworkSwitchAccessControlLists") updateNetworkSwitchAccessControlLists

> Update the access control lists for a MS network


```javascript
function updateNetworkSwitchAccessControlLists(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchAccessControlLists |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchAccessControlLists'] = new UpdateNetworkSwitchAccessControlListsModel({"key":"value"});

    controller.updateNetworkSwitchAccessControlLists(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_port_schedules_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchPortSchedulesController") SwitchPortSchedulesController

### Get singleton instance

The singleton instance of the ``` SwitchPortSchedulesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchPortSchedulesController;
```

### <a name="get_network_switch_port_schedules"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.getNetworkSwitchPortSchedules") getNetworkSwitchPortSchedules

> List switch port schedules


```javascript
function getNetworkSwitchPortSchedules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchPortSchedules(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.createNetworkSwitchPortSchedule") createNetworkSwitchPortSchedule

> Add a switch port schedule


```javascript
function createNetworkSwitchPortSchedule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchPortSchedule |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSwitchPortSchedule'] = new CreateNetworkSwitchPortScheduleModel({"key":"value"});

    controller.createNetworkSwitchPortSchedule(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.deleteNetworkSwitchPortSchedule") deleteNetworkSwitchPortSchedule

> Delete a switch port schedule


```javascript
function deleteNetworkSwitchPortSchedule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| portScheduleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['portScheduleId'] = 'portScheduleId';

    controller.deleteNetworkSwitchPortSchedule(input, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_port_schedule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortSchedulesController.updateNetworkSwitchPortSchedule") updateNetworkSwitchPortSchedule

> Update a switch port schedule


```javascript
function updateNetworkSwitchPortSchedule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| portScheduleId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchPortSchedule |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['portScheduleId'] = 'portScheduleId';
        input['updateNetworkSwitchPortSchedule'] = new UpdateNetworkSwitchPortScheduleModel({"key":"value"});

    controller.updateNetworkSwitchPortSchedule(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_ports_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchPortsController") SwitchPortsController

### Get singleton instance

The singleton instance of the ``` SwitchPortsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchPortsController;
```

### <a name="get_device_switch_port_statuses"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.getDeviceSwitchPortStatuses") getDeviceSwitchPortStatuses

> Return the status for all the ports of a switch


```javascript
function getDeviceSwitchPortStatuses(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 31 days from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['timespan'] = 22.0392339686115;

    controller.getDeviceSwitchPortStatuses(input, function(error, response, context) {

    
    });
```



### <a name="get_device_switch_port_statuses_packets"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.getDeviceSwitchPortStatusesPackets") getDeviceSwitchPortStatusesPackets

> Return the packet counters for all the ports of a switch


```javascript
function getDeviceSwitchPortStatusesPackets(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 1 day from today. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['timespan'] = 22.0392339686115;

    controller.getDeviceSwitchPortStatusesPackets(input, function(error, response, context) {

    
    });
```



### <a name="get_device_switch_ports"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.getDeviceSwitchPorts") getDeviceSwitchPorts

> List the switch ports for a switch


```javascript
function getDeviceSwitchPorts(serial, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var serial = 'serial';

    controller.getDeviceSwitchPorts(serial, function(error, response, context) {

    
    });
```



### <a name="get_device_switch_port"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.getDeviceSwitchPort") getDeviceSwitchPort

> Return a switch port


```javascript
function getDeviceSwitchPort(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['number'] = 'number';

    controller.getDeviceSwitchPort(input, function(error, response, context) {

    
    });
```



### <a name="update_device_switch_port"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchPortsController.updateDeviceSwitchPort") updateDeviceSwitchPort

> Update a switch port


```javascript
function updateDeviceSwitchPort(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| serial |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateDeviceSwitchPort |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['serial'] = 'serial';
        input['number'] = 'number';
        input['updateDeviceSwitchPort'] = new UpdateDeviceSwitchPortModel({"key":"value"});

    controller.updateDeviceSwitchPort(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_profiles_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchProfilesController") SwitchProfilesController

### Get singleton instance

The singleton instance of the ``` SwitchProfilesController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchProfilesController;
```

### <a name="get_organization_config_template_switch_profiles"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchProfilesController.getOrganizationConfigTemplateSwitchProfiles") getOrganizationConfigTemplateSwitchProfiles

> List the switch profiles for your switch template configuration


```javascript
function getOrganizationConfigTemplateSwitchProfiles(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| configTemplateId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['configTemplateId'] = 'configTemplateId';

    controller.getOrganizationConfigTemplateSwitchProfiles(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchSettingsController") SwitchSettingsController

### Get singleton instance

The singleton instance of the ``` SwitchSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchSettingsController;
```

### <a name="get_network_switch_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettings") getNetworkSwitchSettings

> Returns the switch network settings


```javascript
function getNetworkSwitchSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettings") updateNetworkSwitchSettings

> Update switch network settings


```javascript
function updateNetworkSwitchSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettings'] = new UpdateNetworkSwitchSettingsModel({"key":"value"});

    controller.updateNetworkSwitchSettings(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_dhcp_server_policy"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsDhcpServerPolicy") getNetworkSwitchSettingsDhcpServerPolicy

> Return the DHCP server policy


```javascript
function getNetworkSwitchSettingsDhcpServerPolicy(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsDhcpServerPolicy(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_dhcp_server_policy"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsDhcpServerPolicy") updateNetworkSwitchSettingsDhcpServerPolicy

> Update the DHCP server policy


```javascript
function updateNetworkSwitchSettingsDhcpServerPolicy(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsDhcpServerPolicy |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsDhcpServerPolicy'] = new UpdateNetworkSwitchSettingsDhcpServerPolicyModel({"key":"value"});

    controller.updateNetworkSwitchSettingsDhcpServerPolicy(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_dscp_to_cos_mappings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsDscpToCosMappings") getNetworkSwitchSettingsDscpToCosMappings

> Return the DSCP to CoS mappings


```javascript
function getNetworkSwitchSettingsDscpToCosMappings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsDscpToCosMappings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_dscp_to_cos_mappings"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsDscpToCosMappings") updateNetworkSwitchSettingsDscpToCosMappings

> Update the DSCP to CoS mappings


```javascript
function updateNetworkSwitchSettingsDscpToCosMappings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsDscpToCosMappings |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsDscpToCosMappings'] = new UpdateNetworkSwitchSettingsDscpToCosMappingsModel({"key":"value"});

    controller.updateNetworkSwitchSettingsDscpToCosMappings(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_mtu"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsMtu") getNetworkSwitchSettingsMtu

> Return the MTU configuration


```javascript
function getNetworkSwitchSettingsMtu(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsMtu(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_mtu"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsMtu") updateNetworkSwitchSettingsMtu

> Update the MTU configuration


```javascript
function updateNetworkSwitchSettingsMtu(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsMtu |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsMtu'] = new UpdateNetworkSwitchSettingsMtuModel({"key":"value"});

    controller.updateNetworkSwitchSettingsMtu(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_multicast"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsMulticast") getNetworkSwitchSettingsMulticast

> Return multicast settings for a network


```javascript
function getNetworkSwitchSettingsMulticast(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsMulticast(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_multicast"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsMulticast") updateNetworkSwitchSettingsMulticast

> Update multicast settings for a network


```javascript
function updateNetworkSwitchSettingsMulticast(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsMulticast |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsMulticast'] = new UpdateNetworkSwitchSettingsMulticastModel({"key":"value"});

    controller.updateNetworkSwitchSettingsMulticast(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_qos_rules"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsQosRules") getNetworkSwitchSettingsQosRules

> List quality of service rules


```javascript
function getNetworkSwitchSettingsQosRules(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsQosRules(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.createNetworkSwitchSettingsQosRule") createNetworkSwitchSettingsQosRule

> Add a quality of service rule


```javascript
function createNetworkSwitchSettingsQosRule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchSettingsQosRule |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSwitchSettingsQosRule'] = new CreateNetworkSwitchSettingsQosRuleModel({"key":"value"});

    controller.createNetworkSwitchSettingsQosRule(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_qos_rules_order"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsQosRulesOrder") getNetworkSwitchSettingsQosRulesOrder

> Return the quality of service rule IDs by order in which they will be processed by the switch


```javascript
function getNetworkSwitchSettingsQosRulesOrder(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsQosRulesOrder(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_qos_rules_order"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsQosRulesOrder") updateNetworkSwitchSettingsQosRulesOrder

> Update the order in which the rules should be processed by the switch


```javascript
function updateNetworkSwitchSettingsQosRulesOrder(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsQosRulesOrder |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsQosRulesOrder'] = new UpdateNetworkSwitchSettingsQosRulesOrderModel({"key":"value"});

    controller.updateNetworkSwitchSettingsQosRulesOrder(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsQosRule") getNetworkSwitchSettingsQosRule

> Return a quality of service rule


```javascript
function getNetworkSwitchSettingsQosRule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qosRuleId'] = 'qosRuleId';

    controller.getNetworkSwitchSettingsQosRule(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.deleteNetworkSwitchSettingsQosRule") deleteNetworkSwitchSettingsQosRule

> Delete a quality of service rule


```javascript
function deleteNetworkSwitchSettingsQosRule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qosRuleId'] = 'qosRuleId';

    controller.deleteNetworkSwitchSettingsQosRule(input, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_qos_rule"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsQosRule") updateNetworkSwitchSettingsQosRule

> Update a quality of service rule


```javascript
function updateNetworkSwitchSettingsQosRule(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| qosRuleId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsQosRule |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['qosRuleId'] = 'qosRuleId';
        input['updateNetworkSwitchSettingsQosRule'] = new UpdateNetworkSwitchSettingsQosRuleModel({"key":"value"});

    controller.updateNetworkSwitchSettingsQosRule(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_storm_control"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsStormControl") getNetworkSwitchSettingsStormControl

> Return the storm control configuration for a switch network


```javascript
function getNetworkSwitchSettingsStormControl(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsStormControl(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_storm_control"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsStormControl") updateNetworkSwitchSettingsStormControl

> Update the storm control configuration for a switch network


```javascript
function updateNetworkSwitchSettingsStormControl(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsStormControl |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsStormControl'] = new UpdateNetworkSwitchSettingsStormControlModel({"key":"value"});

    controller.updateNetworkSwitchSettingsStormControl(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_settings_stp"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.getNetworkSwitchSettingsStp") getNetworkSwitchSettingsStp

> Returns STP settings


```javascript
function getNetworkSwitchSettingsStp(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchSettingsStp(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_switch_settings_stp"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchSettingsController.updateNetworkSwitchSettingsStp") updateNetworkSwitchSettingsStp

> Updates STP settings


```javascript
function updateNetworkSwitchSettingsStp(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSwitchSettingsStp |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSwitchSettingsStp'] = new UpdateNetworkSwitchSettingsStpModel({"key":"value"});

    controller.updateNetworkSwitchSettingsStp(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="switch_stacks_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SwitchStacksController") SwitchStacksController

### Get singleton instance

The singleton instance of the ``` SwitchStacksController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SwitchStacksController;
```

### <a name="get_network_switch_stacks"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.getNetworkSwitchStacks") getNetworkSwitchStacks

> List the switch stacks in a network


```javascript
function getNetworkSwitchStacks(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSwitchStacks(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.createNetworkSwitchStack") createNetworkSwitchStack

> Create a stack


```javascript
function createNetworkSwitchStack(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkSwitchStack'] = new CreateNetworkSwitchStackModel({"key":"value"});

    controller.createNetworkSwitchStack(input, function(error, response, context) {

    
    });
```



### <a name="get_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.getNetworkSwitchStack") getNetworkSwitchStack

> Show a switch stack


```javascript
function getNetworkSwitchStack(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['switchStackId'] = 'switchStackId';

    controller.getNetworkSwitchStack(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.deleteNetworkSwitchStack") deleteNetworkSwitchStack

> Delete a stack


```javascript
function deleteNetworkSwitchStack(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['switchStackId'] = 'switchStackId';

    controller.deleteNetworkSwitchStack(input, function(error, response, context) {

    
    });
```



### <a name="add_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.addNetworkSwitchStack") addNetworkSwitchStack

> Add a switch to a stack


```javascript
function addNetworkSwitchStack(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |
| addNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['switchStackId'] = 'switchStackId';
        input['addNetworkSwitchStack'] = new AddNetworkSwitchStackModel({"key":"value"});

    controller.addNetworkSwitchStack(input, function(error, response, context) {

    
    });
```



### <a name="remove_network_switch_stack"></a>![Method: ](https://apidocs.io/img/method.png ".SwitchStacksController.removeNetworkSwitchStack") removeNetworkSwitchStack

> Remove a switch from a stack


```javascript
function removeNetworkSwitchStack(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| switchStackId |  ``` Required ```  | TODO: Add a parameter description |
| removeNetworkSwitchStack |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['switchStackId'] = 'switchStackId';
        input['removeNetworkSwitchStack'] = new RemoveNetworkSwitchStackModel({"key":"value"});

    controller.removeNetworkSwitchStack(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="syslog_servers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".SyslogServersController") SyslogServersController

### Get singleton instance

The singleton instance of the ``` SyslogServersController ``` class can be accessed from the API Client.

```javascript
var controller = lib.SyslogServersController;
```

### <a name="get_network_syslog_servers"></a>![Method: ](https://apidocs.io/img/method.png ".SyslogServersController.getNetworkSyslogServers") getNetworkSyslogServers

> List the syslog servers for a network


```javascript
function getNetworkSyslogServers(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkSyslogServers(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_syslog_servers"></a>![Method: ](https://apidocs.io/img/method.png ".SyslogServersController.updateNetworkSyslogServers") updateNetworkSyslogServers

> Update the syslog servers for a network


```javascript
function updateNetworkSyslogServers(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSyslogServers |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkSyslogServers'] = new UpdateNetworkSyslogServersModel({"key":"value"});

    controller.updateNetworkSyslogServers(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="traffic_analysis_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TrafficAnalysisSettingsController") TrafficAnalysisSettingsController

### Get singleton instance

The singleton instance of the ``` TrafficAnalysisSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.TrafficAnalysisSettingsController;
```

### <a name="get_network_traffic_analysis_settings"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficAnalysisSettingsController.getNetworkTrafficAnalysisSettings") getNetworkTrafficAnalysisSettings

> Return the traffic analysis settings for a network


```javascript
function getNetworkTrafficAnalysisSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkTrafficAnalysisSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_traffic_analysis_settings"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficAnalysisSettingsController.updateNetworkTrafficAnalysisSettings") updateNetworkTrafficAnalysisSettings

> Update the traffic analysis settings for a network


```javascript
function updateNetworkTrafficAnalysisSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkTrafficAnalysisSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkTrafficAnalysisSettings'] = new UpdateNetworkTrafficAnalysisSettingsModel({"key":"value"});

    controller.updateNetworkTrafficAnalysisSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="traffic_shaping_controller"></a>![Class: ](https://apidocs.io/img/class.png ".TrafficShapingController") TrafficShapingController

### Get singleton instance

The singleton instance of the ``` TrafficShapingController ``` class can be accessed from the API Client.

```javascript
var controller = lib.TrafficShapingController;
```

### <a name="update_network_ssid_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.updateNetworkSsidTrafficShaping") updateNetworkSsidTrafficShaping

> Update the traffic shaping settings for an SSID on an MR network


```javascript
function updateNetworkSsidTrafficShaping(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkSsidTrafficShaping |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';
        input['updateNetworkSsidTrafficShaping'] = new UpdateNetworkSsidTrafficShapingModel({"key":"value"});

    controller.updateNetworkSsidTrafficShaping(input, function(error, response, context) {

    
    });
```



### <a name="get_network_ssid_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.getNetworkSsidTrafficShaping") getNetworkSsidTrafficShaping

> Display the traffic shaping settings for a SSID on an MR network


```javascript
function getNetworkSsidTrafficShaping(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| number |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['number'] = 'number';

    controller.getNetworkSsidTrafficShaping(input, function(error, response, context) {

    
    });
```



### <a name="update_network_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.updateNetworkTrafficShaping") updateNetworkTrafficShaping

> Update the traffic shaping settings for an MX network


```javascript
function updateNetworkTrafficShaping(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkTrafficShaping |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkTrafficShaping'] = new UpdateNetworkTrafficShapingModel({"key":"value"});

    controller.updateNetworkTrafficShaping(input, function(error, response, context) {

    
    });
```



### <a name="get_network_traffic_shaping"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.getNetworkTrafficShaping") getNetworkTrafficShaping

> Display the traffic shaping settings for an MX network


```javascript
function getNetworkTrafficShaping(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkTrafficShaping(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_traffic_shaping_application_categories"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.getNetworkTrafficShapingApplicationCategories") getNetworkTrafficShapingApplicationCategories

> Returns the application categories for traffic shaping rules.


```javascript
function getNetworkTrafficShapingApplicationCategories(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkTrafficShapingApplicationCategories(networkId, function(error, response, context) {

    
    });
```



### <a name="get_network_traffic_shaping_dscp_tagging_options"></a>![Method: ](https://apidocs.io/img/method.png ".TrafficShapingController.getNetworkTrafficShapingDscpTaggingOptions") getNetworkTrafficShapingDscpTaggingOptions

> Returns the available DSCP tagging options for your traffic shaping rules.


```javascript
function getNetworkTrafficShapingDscpTaggingOptions(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkTrafficShapingDscpTaggingOptions(networkId, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="uplink_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".UplinkSettingsController") UplinkSettingsController

### Get singleton instance

The singleton instance of the ``` UplinkSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.UplinkSettingsController;
```

### <a name="get_network_uplink_settings"></a>![Method: ](https://apidocs.io/img/method.png ".UplinkSettingsController.getNetworkUplinkSettings") getNetworkUplinkSettings

> Returns the uplink settings for your MX network.


```javascript
function getNetworkUplinkSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkUplinkSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_uplink_settings"></a>![Method: ](https://apidocs.io/img/method.png ".UplinkSettingsController.updateNetworkUplinkSettings") updateNetworkUplinkSettings

> Updates the uplink settings for your MX network.


```javascript
function updateNetworkUplinkSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkUplinkSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkUplinkSettings'] = new UpdateNetworkUplinkSettingsModel({"key":"value"});

    controller.updateNetworkUplinkSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="vlans_controller"></a>![Class: ](https://apidocs.io/img/class.png ".VlansController") VlansController

### Get singleton instance

The singleton instance of the ``` VlansController ``` class can be accessed from the API Client.

```javascript
var controller = lib.VlansController;
```

### <a name="get_network_vlans"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.getNetwork_vlans") getNetwork_vlans

> List the VLANs for an MX network


```javascript
function getNetwork_vlans(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetwork_vlans(networkId, function(error, response, context) {

    
    });
```



### <a name="create_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.createNetworkVlan") createNetworkVlan

> Add a VLAN


```javascript
function createNetworkVlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| createNetworkVlan |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['createNetworkVlan'] = new CreateNetworkVlanModel({"key":"value"});

    controller.createNetworkVlan(input, function(error, response, context) {

    
    });
```



### <a name="get_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.getNetworkVlan") getNetworkVlan

> Return a VLAN


```javascript
function getNetworkVlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['vlanId'] = 'vlanId';

    controller.getNetworkVlan(input, function(error, response, context) {

    
    });
```



### <a name="update_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.updateNetworkVlan") updateNetworkVlan

> Update a VLAN


```javascript
function updateNetworkVlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkVlan |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['vlanId'] = 'vlanId';
        input['updateNetworkVlan'] = new UpdateNetworkVlanModel({"key":"value"});

    controller.updateNetworkVlan(input, function(error, response, context) {

    
    });
```



### <a name="delete_network_vlan"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.deleteNetworkVlan") deleteNetworkVlan

> Delete a VLAN from a network


```javascript
function deleteNetworkVlan(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| vlanId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['vlanId'] = 'vlanId';

    controller.deleteNetworkVlan(input, function(error, response, context) {

    
    });
```



### <a name="get_network_vlans_enabled_state"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.getNetwork_vlans_EnabledState") getNetwork_vlans_EnabledState

> Returns the enabled status of VLANs for the network


```javascript
function getNetwork_vlans_EnabledState(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetwork_vlans_EnabledState(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_vlans_enabled_state"></a>![Method: ](https://apidocs.io/img/method.png ".VlansController.updateNetwork_vlans_EnabledState") updateNetwork_vlans_EnabledState

> Enable/Disable VLANs for the given network


```javascript
function updateNetwork_vlans_EnabledState(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetwork_vlans_EnabledState |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetwork_vlans_EnabledState'] = new UpdateNetworkVlansEnabledStateModel({"key":"value"});

    controller.updateNetwork_vlans_EnabledState(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="webhook_logs_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WebhookLogsController") WebhookLogsController

### Get singleton instance

The singleton instance of the ``` WebhookLogsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.WebhookLogsController;
```

### <a name="get_organization_webhook_logs"></a>![Method: ](https://apidocs.io/img/method.png ".WebhookLogsController.getOrganizationWebhookLogs") getOrganizationWebhookLogs

> Return the log of webhook POSTs sent


```javascript
function getOrganizationWebhookLogs(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| organizationId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 90 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 31 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. |
| perPage |  ``` Optional ```  | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. |
| startingAfter |  ``` Optional ```  | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| endingBefore |  ``` Optional ```  | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| url |  ``` Optional ```  | The URL the webhook was sent to |



#### Example Usage

```javascript

    var input = [];
        input['organizationId'] = 'organizationId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['perPage'] = 22;
        input['startingAfter'] = 'startingAfter';
        input['endingBefore'] = 'endingBefore';
        input['url'] = 'url';

    controller.getOrganizationWebhookLogs(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="wireless_health_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WirelessHealthController") WirelessHealthController

### Get singleton instance

The singleton instance of the ``` WirelessHealthController ``` class can be accessed from the API Client.

```javascript
var controller = lib.WirelessHealthController;
```

### <a name="get_network_clients_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkClientsConnectionStats") getNetworkClientsConnectionStats

> Aggregated connectivity info for this network, grouped by clients


```javascript
function getNetworkClientsConnectionStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';

    controller.getNetworkClientsConnectionStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_clients_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkClientsLatencyStats") getNetworkClientsLatencyStats

> Aggregated latency info for this network, grouped by clients


```javascript
function getNetworkClientsLatencyStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['fields'] = 'fields';

    controller.getNetworkClientsLatencyStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkClientConnectionStats") getNetworkClientConnectionStats

> Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.


```javascript
function getNetworkClientConnectionStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';

    controller.getNetworkClientConnectionStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_client_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkClientLatencyStats") getNetworkClientLatencyStats

> Aggregated latency info for a given client on this network. Clients are identified by their MAC.


```javascript
function getNetworkClientLatencyStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| clientId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['clientId'] = 'clientId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['fields'] = 'fields';

    controller.getNetworkClientLatencyStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkConnectionStats") getNetworkConnectionStats

> Aggregated connectivity info for this network


```javascript
function getNetworkConnectionStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';

    controller.getNetworkConnectionStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_devices_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkDevicesConnectionStats") getNetworkDevicesConnectionStats

> Aggregated connectivity info for this network, grouped by node


```javascript
function getNetworkDevicesConnectionStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';

    controller.getNetworkDevicesConnectionStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_devices_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkDevicesLatencyStats") getNetworkDevicesLatencyStats

> Aggregated latency info for this network, grouped by node


```javascript
function getNetworkDevicesLatencyStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['fields'] = 'fields';

    controller.getNetworkDevicesLatencyStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_connection_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkDeviceConnectionStats") getNetworkDeviceConnectionStats

> Aggregated connectivity info for a given AP on this network


```javascript
function getNetworkDeviceConnectionStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';

    controller.getNetworkDeviceConnectionStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_device_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkDeviceLatencyStats") getNetworkDeviceLatencyStats

> Aggregated latency info for a given AP on this network


```javascript
function getNetworkDeviceLatencyStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| serial |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['serial'] = 'serial';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['fields'] = 'fields';

    controller.getNetworkDeviceLatencyStats(input, function(error, response, context) {

    
    });
```



### <a name="get_network_failed_connections"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkFailedConnections") getNetworkFailedConnections

> List of all failed client connection events on this network in a given time range


```javascript
function getNetworkFailedConnections(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| serial |  ``` Optional ```  | Filter by AP |
| clientId |  ``` Optional ```  | Filter by client MAC |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['serial'] = 'serial';
        input['clientId'] = 'clientId';

    controller.getNetworkFailedConnections(input, function(error, response, context) {

    
    });
```



### <a name="get_network_latency_stats"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessHealthController.getNetworkLatencyStats") getNetworkLatencyStats

> Aggregated latency info for this network


```javascript
function getNetworkLatencyStats(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| t0 |  ``` Optional ```  | The beginning of the timespan for the data. The maximum lookback period is 180 days from today. |
| t1 |  ``` Optional ```  | The end of the timespan for the data. t1 can be a maximum of 7 days after t0. |
| timespan |  ``` Optional ```  | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. |
| ssid |  ``` Optional ```  | Filter results by SSID |
| vlan |  ``` Optional ```  | Filter results by VLAN |
| apTag |  ``` Optional ```  | Filter results by AP Tag |
| fields |  ``` Optional ```  | Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string. |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['t0'] = 't0';
        input['t1'] = 't1';
        input['timespan'] = 22.0392339686115;
        input['ssid'] = 22;
        input['vlan'] = 22;
        input['apTag'] = 'apTag';
        input['fields'] = 'fields';

    controller.getNetworkLatencyStats(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)

## <a name="wireless_settings_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WirelessSettingsController") WirelessSettingsController

### Get singleton instance

The singleton instance of the ``` WirelessSettingsController ``` class can be accessed from the API Client.

```javascript
var controller = lib.WirelessSettingsController;
```

### <a name="get_network_wireless_settings"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessSettingsController.getNetworkWirelessSettings") getNetworkWirelessSettings

> Return the wireless settings for a network


```javascript
function getNetworkWirelessSettings(networkId, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var networkId = 'networkId';

    controller.getNetworkWirelessSettings(networkId, function(error, response, context) {

    
    });
```



### <a name="update_network_wireless_settings"></a>![Method: ](https://apidocs.io/img/method.png ".WirelessSettingsController.updateNetworkWirelessSettings") updateNetworkWirelessSettings

> Update the wireless settings for a network


```javascript
function updateNetworkWirelessSettings(input, callback)
```
#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| networkId |  ``` Required ```  | TODO: Add a parameter description |
| updateNetworkWirelessSettings |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```javascript

    var input = [];
        input['networkId'] = 'networkId';
        input['updateNetworkWirelessSettings'] = new UpdateNetworkWirelessSettingsModel({"key":"value"});

    controller.updateNetworkWirelessSettings(input, function(error, response, context) {

    
    });
```



[Back to List of Controllers](#list_of_controllers)



