

### Postman Collection

Use graphical desktop utility to explore and interact with the Meraki API.

<div class="postman-run-button"
data-postman-action="collection/import"
data-postman-var-1="c751ca894f2eed4c4cbd"></div>
<script type="text/javascript">
  (function (p,o,s,t,m,a,n) {
    !p[s] && (p[s] = function () { (p[t] || (p[t] = [])).push(arguments); });
    !o.getElementById(s+t) && o.getElementsByTagName("head")[0].appendChild((
      (n = o.createElement("script")),
      (n.id = s+t), (n.async = 1), (n.src = m), n
    ));
  }(window, document, "_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));
</script>

### Python library

If using the Meraki [Python library](pythonLibrary.md), install it via `pip install meraki`.

## Base URI

In most parts of the world, every API request will begin with the following **base URI**: 

> `https://api.meraki.com/api/v1`

For organizations hosted in the China dashboard, please specify the following base URI instead:

> `https://api.meraki.cn/api/v1`

Read more about the path schema [here](PathSchema.md).

## Authorization

The Meraki Dashboard API requires a header parameter of `X-Cisco-Meraki-API-Key` to provide authorization for each request.
 
```json
{
	"X-Cisco-Meraki-API-Key": <Meraki_API_Key>
}
```

```curl
curl https://api.meraki.com/api/v1/organizations \
  -H 'X-Cisco-Meraki-API-Key: {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
```

Read more about generating an API key [here](Authorization.md).

## Find your organization ID 

To begin navigating the API, you will first need to know your organization ID. This will be required for endpoints needing an `organizationId` parameter.

[List the organizations that the user has privileges on](##!get-organizations)


### Request
`GET /organizations` 

```cURL
curl https://api.meraki.com/api/v1/organizations \
  -L -H 'X-Cisco-Meraki-API-Key: {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizations()
```

### Response
```json
Successful HTTP Status: 200
[
  {
    "id":12345678,
    "name":"My org"
  }
]
```

```Python
>>> print(response)
[{'id': '549236', 'name': 'DevNet Sandbox', 'url': 'https://n149.meraki.com/o/-t35Mb/manage/organization/overview'}]
```

## Find your network ID

Now that you have an organization ID, list the networks of the organization. 
 
[List the networks in an organization](##!get-organization-networks)

### Request
`GET /organizations/:organizationId/networks`

```cURL
curl https://api.meraki.com/api/v1/organizations/{organizationId}/networks \
  -L -H 'X-Cisco-Meraki-API-Key: {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationNetworks(org_id)
```

### Response
```json
Successful HTTP Status: 200
[
  {
    "id":"N_1234",
    "organizationId":"12345678",
    "type": "wireless",
    "name":"My network",
    "timeZone": "US/Pacific",
    "tags": null
  }
]
```

```Python
>>> print(response)
[{'id': 'L_646829496481105433', 'organizationId': '549236', 'name': 'DevNet Sandbox Always on READ ONLY', 'timeZone': 'America/Los_Angeles', 'tags': None, 'productTypes': ['appliance', 'switch', 'wireless'], 'type': 'combined', 'disableMyMerakiCom': False, 'disableRemoteStatusPage': True}]
```

Note the `id` for future endpoints that require a `networkId`.

## Find your device serials
 Use the `id` from the `~/networks` response as the `:networkId`  in the following request.
 
[List the devices in a network](##!get-network-devices)

### Request
`GET /networks/:networkId/devices`

```cURL
curl https://api.meraki.com/api/v1/networks/{networkId}/devices \
  -L -H 'X-Cisco-Meraki-API-Key: {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.networks.getNetworkDevices(net_id)
```

### Response
```json
Successful HTTP Status: 200
[
  {
    "name": "My AP",
    "lat": 37.4180951010362,
    "lng": -122.098531723022,
    "serial": "Q234-ABCD-5678",
    "mac": "00:11:22:33:44:55",
    "model": "MR34",
    "address": "1600 Pennsylvania Ave",
    "notes": "My AP's note",
    "lanIp": "1.2.3.4",
    "tags": " recently-added ",
    "networkId": "N_24329156",
    "beaconIdParams": {
      "uuid": "00000000-0000-0000-0000-000000000000",
      "major": 5,
      "minor": 3
    }
  }
]
```

```Python
>>> print(response)
[{'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2QN-9J8L-SLPD', 'mac': 'e0:55:3d:17:d4:23', 'wan1Ip': '10.10.10.106', 'wan2Ip': None, 'lanIp': '10.10.10.106', 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/hZB0Gcvc/manage/nodes/new_list/246656701813795', 'networkId': 'L_646829496481105433', 'model': 'MX65', 'firmware': 'wired-14-40', 'floorPlanId': None}, {'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2HP-F5K5-R88R', 'mac': '88:15:44:df:f3:af', 'lanIp': '192.168.128.2', 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/E8DpVavc/manage/nodes/new_list/149624931218351', 'networkId': 'L_646829496481105433', 'model': 'MS220-8P', 'switchProfileId': None, 'firmware': 'switch-11-22', 'floorPlanId': None}, {'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2MD-BHHS-5FDL', 'mac': '88:15:44:60:21:10', 'lanIp': None, 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/XT0N4cvc/manage/nodes/new_list/149624922841360', 'networkId': 'L_646829496481105433', 'model': 'MR53', 'firmware': 'wireless-25-14', 'floorPlanId': None}]
```
Note the `serial` for future usage.

## Get the device's management interface settings
 Use the `serial` from the `/networks/:networkId/devices` response as the `:serial`  in the following request to determine whether it has been assigned a dynamic or static IP address.

[Return the management interface settings for a device](##!get-device-management-interface)

### Request
`GET /devices/:serial/managementInterface`

```cURL
curl https://api.meraki.com/api/v1/devices/{serial}/managementInterface \
  -L -H 'X-Cisco-Meraki-API-Key: {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.networks.getNetworkDevices(serial)
print(response)
```

### Response
```json
Successful HTTP Status: 200
{
  "ddnsHostnames": {
    "activeDdnsHostname": "mx1-sample.dynamic-m.com",
    "ddnsHostnameWan1": "mx1-sample-1.dynamic-m.com",
    "ddnsHostnameWan2": "mx1-sample-2.dynamic-m.com"
  },
  "wan1": {
    "wanEnabled": "not configured",
    "usingStaticIp": true,
    "staticIp": "1.2.3.4",
    "staticSubnetMask": "255.255.255.0",
    "staticGatewayIp": "1.2.3.1",
    "staticDns": [ "1.2.3.2", "1.2.3.3" ],
    "vlan": 7
  },
  "wan2": {
    "wanEnabled": "enabled",
    "usingStaticIp": false,
    "vlan": 2
  }
}
```

```Python
>>> print(response)
{'wan1': {'wanEnabled': 'not configured', 'usingStaticIp': False, 'vlan': None}, 'wan2': {'wanEnabled': 'not configured', 'usingStaticIp': False, 'vlan': None}, 'ddnsHostnames': {'activeDdnsHostname': 'dnsmb0-wired-mttrcvbqjp.dynamic-m.com', 'ddnsHostnameWan1': 'dnsmb0-wired-mttrcvbqjp-1.dynamic-m.com', 'ddnsHostnameWan2': 'dnsmb0-wired-mttrcvbqjp-2.dynamic-m.com'}}
```