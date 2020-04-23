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
  -H 'Authorization: Bearer {MERAKI-API-KEY}'
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
  -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
print(dashboard.organizations.getOrganizations())
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
Note the `id` for future endpoints that require a `networkId`

## Find your Device Serials
 Use the `id` from the `~/networks` response as the `:networkId`  in the following request.
 
[List the devices in a network](##!get-network-devices)

### Request
`GET /networks/:networkId/devices`

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