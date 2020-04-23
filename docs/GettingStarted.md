## Base URI

Every API request will begin with the following **Base URI**. 

> `https://api.meraki.com/api/v1`

Read more about the path schema [here](PathSchema.md).

## Authorization

In addition to the path URL, an `Authorization` header must be added to every API request with the following format.
 
```json
{
	"Authorization": "Bearer <Meraki_API_Key>"
}
```

```cURL
curl https://api.meraki.com/api/v1/organizations \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
```

Read more about generating an API key [here](Authorization.md).

## Find your Organization ID 

To begin navigating the API, you will first need to know your Organization ID. This will be required for endpoints needing an `organizationId` parameter.

[List the organizations that the user has privileges on](##!get-organizations)


### Request
`GET /organizations` 

```cURL
curl https://api.meraki.com/api/v1/organizations \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
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

## Find your Network ID

Now that you have an Organization ID, list the networks of the organization. 
 
[List the networks in an organization](##!get-organization-networks)

### Request
`GET /organizations/:organizationId/networks`

```cURL
curl https://api.meraki.com/api/v1/organizations/{organizationId}/networks \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
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
[{'id': 'L_646829496481104079', 'organizationId': '549236', 'name': 'DevNet Sandbox Always on READ ONLY', 'timeZone': 'America/Los_Angeles', 'tags': None, 'productTypes': ['appliance', 'switch', 'wireless'], 'type': 'combined', 'disableMyMerakiCom': False, 'disableRemoteStatusPage': True}]
```

Note the `id` for future endpoints that require a `networkId`

## Find your Device Serials
 Use the `id` from the `~/networks` response as the `:networkId`  in the following request.
 
[List the devices in a network](##!get-network-devices)

### Request
`GET /networks/:networkId/devices`

```cURL
curl https://api.meraki.com/api/v1/networks/{networkId}/devices \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
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
[{'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2QN-9J8L-SLPD', 'mac': 'e0:55:3d:17:d4:23', 'wan1Ip': '10.10.10.106', 'wan2Ip': None, 'lanIp': '10.10.10.106', 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/hZB0Gcvc/manage/nodes/new_list/246656701813795', 'networkId': 'L_646829496481104079', 'model': 'MX65', 'firmware': 'wired-14-40', 'floorPlanId': None}, {'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2HP-F5K5-R88R', 'mac': '88:15:44:df:f3:af', 'lanIp': '192.168.128.2', 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/E8DpVavc/manage/nodes/new_list/149624931218351', 'networkId': 'L_646829496481104079', 'model': 'MS220-8P', 'switchProfileId': None, 'firmware': 'switch-11-22', 'floorPlanId': None}, {'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '', 'serial': 'Q2MD-BHHS-5FDL', 'mac': '88:15:44:60:21:10', 'lanIp': None, 'url': 'https://n149.meraki.com/DevNet-Sandbox-A/n/XT0N4cvc/manage/nodes/new_list/149624922841360', 'networkId': 'L_646829496481104079', 'model': 'MR53', 'firmware': 'wireless-25-14', 'floorPlanId': None}]
```
Note the `serial` for future usage.

## Get Network Device Uplink
 Use the `serial` from the `/networks/:networkId/devices` response as the `:networkId`  in the following request.

[Return the uplink information for a device](##!get-network-device-uplink)

### Request
`GET /devices/:serial/uplink`

### Response
```json
Successful HTTP Status: 200
[
  {
    "interface": "WAN 1",
    "status": "Active",
    "ip": "1.2.3.4",
    "gateway": "1.2.3.5",
    "publicIp": "123.123.123.1",
    "dns": "8.8.8.8, 8.8.4.4",
    "usingStaticIp": false
  }
]
```