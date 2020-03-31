Action Batches are a special type of Dashboard API mechanism for submitting batched configuration requests in a single synchronous or asynchronous transaction. Action Batches are ideal for bulk configuration, either in the initial provisioning process, or for rolling out wide-scale configuration changes. For example, add a switch to a network, configure all 48 ports, and set the switch’s management interface in a single POST.

## Use Cases
* Deploy multiple changes across networks and devices
* Run Batches synchronously or asynchronously 
* Avoid hitting the API rate limit for high-scale configuration changes
* Ensure all updates will succeed before changes are committed

## Details
* Action batches allow an API client to define a batch of write actions (**create**, **update**, **destroy**, etc.).
* Batches are run **atomically** (all or nothing, no partial success).
* Batches are run **asynchronously** by default. Smaller batches can be run **synchronously**.
* You can run up to **20 resources** synchronously in a single batch.
* A batch can consists of up to **100** resources.
* Limit of **5** concurrent running batches at a time.
* A batch should be completed within **10 minutes** from confirmation.
* Different types of resources and operations can be combined in a batch.
* The actions in a batch will be executed in the same order they are defined.
* Batches will not be executed until the confirmed property is set. Once a batch is confirmed it cannot be deleted. If a batch is defined but not confirmed it will be **automatically deleted after one week**.

## Create an Action Batch
To create an Action Batch, you will need to send a POST request containing an array or resources to be updated and whether or not it should run immediately. You can also select if the batch should run synchronously or asynchronously depending on the size of the batch.

```
POST /organizations/{organizationId}/actionBatches
```

### PARAMETERS
**Parameter**|**Description**
:-------------: |:-------------:
confirmed| Set to true for immediate execution. Set to false if the action should be previewed before executing.
synchronous| Force the batch to run synchronous. There can be at most 20 actions in synchronous batch.
actions| A set of changes to make as part of this action
resource| Unique identifier for the resource to be acted on
operation| The operation to be run on the resource, such as "**create**", "**update**", "**destroy**", "**bind**", etc
body| The body of the action. Example: `{"tags": tags, "type": "access", "vlan": vlan}`

#### SAMPLE REQUEST
```bash
curl -X POST https://api.meraki.com/api/v0/organizations/1234567890/actionBatches \
-L \
-H 'Content-Type: application/json' \
-H 'X-Cisco-Meraki-API-Key: <API_KEY>' \
-d '{
"confirmed": true,
"synchronous": true,
"actions": [
     {
      "resource": "/devices/QXXX-XXXX-XXXX/switchPorts/3",
      "operation": "update",
      "body": {
        "enabled": true
      }
    }
]
}'
```

#### SAMPLE RESPONSE
```
Successful HTTP Status: 201

	{
	  "id": "123",
	  "status": "completed",
	  "confirmed": true,
	  "actions": [
	    {
	      "resource": "/devices/QXXX-XXXX-XXXX/switchPorts/3",
	      "operation": "update",
	      "body": {
	        "enabled": false
	      }
	    }
	  ]
	}
```

## Supported Resources
The following list includes the API resources available for Action Batches.


|group|summary|resource|operation|
|----|----|----|----|
|Bluetooth device setting|Update the bluetooth settings for a wireless device|`/devices/{serial}/wireless/bluetooth/settings`|update|
|Cellular gateway connectivity monitoring destination|Update the connectivity testing destinations for an MG network|`/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations`|update|
|Cellular gateway device lan|Update the LAN Settings for a single MG.|`/devices/{serial}/cellularGateway/settings`|update|
|Cellular gateway dhcp setting|Update common DHCP settings of MGs|`/networks/{networkId}/cellularGateway/settings/dhcp`|update|
|Cellular gateway port forwarding rules|Updates the port forwarding rules for a single MG.|`/devices/{serial}/cellularGateway/settings/portForwardingRules`|update|
|Cellular gateway subnet pool|Update the subnet pool and mask configuration for MGs in the network.|`/networks/{networkId}/cellularGateway/settings/subnetPool`|update|
|Cellular gateway uplink setting|Updates the uplink settings for your MG network.|`/networks/{networkId}/cellularGateway/settings/uplink`|update|
|Device|Claim devices into a network|`/networks/{networkId}/devices`|claim|
|Dhcp server policy|Update the DHCP server policy|`/networks/{networkId}/switch/settings/dhcpServerPolicy`|update|
|Dscp cos mapping|Update the DSCP to CoS mappings|`/networks/{networkId}/switch/settings/dscpToCosMappings`|update|
|Floor plan|Destroy a floor plan|`/networks/{networkId}/floorPlans/{floorPlanId}`|destroy|
|Floor plan|Update a floor plan's geolocation and other meta data|`/networks/{networkId}/floorPlans/{floorPlanId}`|update|
|Group policy|Create a group policy|`/networks/{networkId}/groupPolicies`|create|
|Group policy|Delete a group policy|`/networks/{networkId}/groupPolicies/{groupPolicyId}`|destroy|
|Group policy|Update a group policy|`/networks/{networkId}/groupPolicies/{groupPolicyId}`|update|
|License|Assign SM seats to a network. This will increase the managed SM device limit of the network|`/organizations/{organizationId}/licenses`|assignSeats|
|License|Move licenses to another organization. This will also move any devices that the licenses are assigned to|`/organizations/{organizationId}/licenses`|move|
|License|Move SM seats to another organization|`/organizations/{organizationId}/licenses`|moveSeats|
|License|Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license|`/organizations/{organizationId}/licenses`|renewSeats|
|License|Update a license|`/organizations/{organizationId}/licenses/{licenseId}`|update|
|Link aggregation|Create a link aggregation group|`/networks/{networkId}/switch/linkAggregations`|create|
|Link aggregation|Split a link aggregation group into separate ports|`/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`|destroy|
|Link aggregation|Update a link aggregation group|`/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`|update|
|Management interface settings|Update the management interface settings for a device|`/devices/{serial}/managementInterface`|update|
|Monitored media server|Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.|`/organizations/{organizationId}/insight/monitoredMediaServers`|create|
|Monitored media server|Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.|`/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`|destroy|
|Monitored media server|Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.|`/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`|update|
|MTU configuration|Update the MTU configuration|`/networks/{networkId}/switch/settings/mtu`|update|
|Multicast|Update multicast settings for a network|`/networks/{networkId}/switch/settings/multicast`|update|
|MX connectivity monitoring destination|Update the connectivity testing destinations for an MX network|`/networks/{networkId}/appliance/connectivityMonitoringDestinations`|update|
|MX l7 firewall|Update the MX L7 firewall rules for an MX network|`/networks/{networkId}/l7FirewallRules`|update|
|MX port|Update the per-port VLAN settings for a single MX port.|`/networks/{networkId}/appliance/ports/{portId}`|update|
|MX uplink setting|Updates the uplink bandwidth settings for your MX network.|`/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth`|update|
|MX VLAN settings|Enable/Disable VLANs for the given network|`/networks/{networkId}/appliance/vlans/settings`|update|
|Network|Create a network|`/organizations/{organizationId}/networks`|create|
|Network|Delete a network|`/networks/{networkId}`|destroy|
|Network settings|Update the settings for a network|`/networks/{networkId}/settings`|update|
|Qos rule|Add a quality of service rule|`/networks/{networkId}/switch/settings/qosRules`|create|
|Qos rule|Delete a quality of service rule|`/networks/{networkId}/switch/settings/qosRules/{qosRuleId}`|destroy|
|Qos rule|Update a quality of service rule|`/networks/{networkId}/switch/settings/qosRules/{qosRuleId}`|update|
|Qos rule|Update the order in which the rules should be processed by the switch|`/networks/{networkId}/switch/settings/qosRules/order`|update_order|
|Quality and retention setting|Update quality and retention settings for the given camera|`/devices/{serial}/camera/qualityAndRetention`|update|
|Radio settings|Update the radio settings of a device|`/devices/{serial}/wireless/radio/settings`|update|
|RF profile|Creates new RF profile for this network|`/networks/{networkId}/wireless/rfProfiles`|create|
|RF profile|Delete a RF Profile|`/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`|destroy|
|RF profile|Updates specified RF profile for this network|`/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`|update|
|Site to site vpn|Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.|`/networks/{networkId}/appliance/vpn/siteToSiteVpn`|update|
|Ssid|Update the attributes of an SSID|`/networks/{networkId}/wireless/ssids/{number}`|update|
|Storm control|Update the storm control configuration for a switch network|`/networks/{networkId}/switch/settings/stormControl`|update|
|STP configuration|Updates STP settings|`/networks/{networkId}/switch/stp`|update|
|Switch port|Cycle a set of switch ports|`/devices/{serial}/switch/ports`|cycle|
|Switch port|Update a switch port|`/devices/{serial}/switch/ports/{portId}`|update|
|Switch port schedule|Update a switch port schedule|`/networks/{networkId}/switch/portSchedules/{portScheduleId}`|update|
|Traffic shaping settings|Update the traffic shaping settings for an MX network|`/networks/{networkId}/appliance/trafficShaping/rules`|update|
|Traffic shaping settings|Update the traffic shaping settings for an SSID on an MR network|`/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules`|update|
|VLAN|Add a VLAN|`/networks/{networkId}/appliance/vlans`|create|
|VLAN|Delete a VLAN from a network|`/networks/{networkId}/appliance/vlans/{vlanId}`|destroy|
|VLAN|Update a VLAN|`/networks/{networkId}/appliance/vlans/{vlanId}`|update|
|Warm spare|Swap MX primary and warm spare appliances|`/networks/{networkId}/swapWarmSpare`|swap|
|Warm spare|Update MX warm spare settings|`/networks/{networkId}/warmSpareSettings`|update|
|Wireless settings|Update the wireless settings for a network|`/networks/{networkId}/wireless/settings`|update|




# API Endpoints
This group of Dashboard API endpoints is available to submit, monitor and manage your Action Batches. Refer to the respective endpoint links for more details.

[Create an action batch]()

`POST /organizations/{organizationId}/actionBatches`

[Return the list of action batches in the organization]()

`GET /organizations/{organizationId}/actionBatches`

[Return an action batch]()

`GET /organizations/{organizationId}/actionBatches/{id}`

[Delete an action batch]()

`DELETE /organizations/{organizationId}/actionBatches/{id}`

[Update an action batch]()

`PUT /organizations/{organizationId}/actionBatches/{id}`

## Response Errors

### Unsupported operation
When you have attempted to use an API endpoint that is not a supported resource as listed above.

```json
{
    "errors": [
        "Unsupported operation"
    ]
}
```

### Execution error
If the batch fails because one of the resources had an error, the `status` parameter will contain additional information.

```json
"status": {
        "completed": false,
        "failed": true,
        "errors": [
            "Error occurred while executing create /networks/L_643451796760561416/vlans/ with {\"id\":111,\"name\":\"New-VLAN\",\"applianceIp\":\"172.16.111.1\",\"subnet\":\"172.16.111.0/24\"}: Validation failed: Vlan has already been taken"
        ]
    },
```

# Example Script

This example Python script will create a new VLAN on a Meraki MX Security Appliance. It will then update multiple switches with new tags. Finally, several ports will be updated to leverage the new VLAN settings. 

```python
# actionBatch-VlanUpdate.py

import requests

# Environment Variables
API_KEY = "aaaaaaaaaaaaaaaaaaabbbbbbbcccccccc"
org_id = 1234567
vlan = 99
net_id = "L_000000000000000"
switch_a = "AAAA-BBBB-CCCC"
switch_b = "DDDD-EEEE-FFFF"
tags = "APIness"

url = f"https://api.meraki.com/api/v0/organizations/{org_id}/actionBatches"

payload = {
    "confirmed": True,
    "synchronous": True,
    "actions": [
        {
            "resource": f"/networks/{net_id}/vlans",
            "operation": "create",
            "body": {
                "id": vlan,
                "name": "API-VLAN",
                "applianceIp": f"172.16.{vlan}.1",
                "subnet": f"172.16.{vlan}.0/24",
            },
        },
        {
            "resource": f"/networks/{net_id}/devices/{switch_a}",
            "operation": "update",
            "body": {"tags": tags},
        },
        {
            "resource": f"/networks/{net_id}/devices/{switch_b}",
            "operation": "update",
            "body": {"tags": tags},
        },
        {
            "resource": f"/devices/{switch_a}/switchPorts/1",
            "operation": "update",
            "body": {"tags": tags, "type": "access", "vlan": vlan},
        },
        {
            "resource": f"/devices/{switch_b}/switchPorts/1",
            "operation": "update",
            "body": {"tags": tags, "type": "access", "vlan": vlan},
        },
    ],
}

headers = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)

```
```bash
$ python3 actionBatch-VlanUpdate.py 
{"id":"643451796760559653","organizationId":"1234567","confirmed":true,"synchronous":true,"status":{"completed":true,"failed":false,"errors":[]},"actions":[{"resource":"/networks/L_00000000000000/vlans/","operation":"create","body": ....
```