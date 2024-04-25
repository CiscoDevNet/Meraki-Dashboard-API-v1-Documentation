# Getting Started

## Overview

In this guide, we'll:

1. Find out which organizations we can access using our auth token
2. Retrieve the list of networks in one of those organizations
3. Retrieve the list of devices in one of those organizations
4. Find the uplink addresses for one or two Meraki devices in that organization using query parameters

## Tools

### Postman Collection

If you prefer to use a graphical desktop utility, you can use [Postman and our Postman collection](https://documenter.getpostman.com/view/897512/SzYXYfmJ) to explore and interact with the Meraki API.

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

If using Python, we recommend using the Meraki [Python library](pythonLibrary.md). Install it via `pip install meraki`.

## Base URI

In most parts of the world, every API request will begin with the following **base URI**:

> `https://api.meraki.com/api/v1`

For organizations hosted in the following country dashboard, please specify the respective base URI instead:

|  Country         |  URI                              |
|------------------|-----------------------------------|
| Canada           | `https://api.meraki.ca/api/v1`    |
| China            | `https://api.meraki.cn/api/v1`    |
| India            | `https://api.meraki.in/api/v1`    |
| United States FedRAMP | `https://api.gov-meraki.com/api/v1` |


Read more about the path schema [here](PathSchema.md).

## Authorization

The Meraki Dashboard API requires a bearer token to provide authorization for each request. [Read more about API auth here](#!authorization).

```JSON
{
 "Authorization": "Bearer <Meraki_API_Key>"
}
```

```curl
curl https://api.meraki.com/api/v1/organizations \
  -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
```

## Find your organization ID

To begin navigating the API, you will first need to know your organization ID. This will be required for endpoints needing an `organizationId` parameter.

> **NB:** some response attributes irrelevant to this guide may be ommitted from the examples for brevity.

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

```JSON
Successful HTTP Status: 200
[
  {
    "id": "549236",
    "name":"DevNet Sandbox"
  }
]
```

```Python
>>> print(response)
[{'id': '549236', 'name': 'DevNet Sandbox'}]
```

## Find your network ID

Now that you have an organization ID, list the networks of the organization.

[List the networks in an organization documentation](##!get-organization-networks)

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

```JSON
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

## Find your devices and their serials

 Use the `id` from the `~/networks` response as the `:networkId`  in the following request.

[List the devices in an organization](##!get-organization-devices/)

### Request

`GET /organizations/:organizationId/devices`

```cURL
curl https://api.meraki.com/api/v1/organizations/{organizationId}/devices \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationDevices({organizationId})
```

### Response

```JSON
Successful HTTP Status: 200
[
    {
        "name": "My AP",
        "lat": 37.4180951010362,
        "lng": -122.098531723022,
        "address": "1600 Pennsylvania Ave",
        "notes": "My AP note",
        "tags": [ "recently-added" ],
        "networkId": "N_24329156",
        "serial": "Q234-ABCD-5678",
        "model": "MR34",
        "mac": "00:11:22:33:44:55",
        "lanIp": "1.2.3.4",
        "firmware": "wireless-25-14",
        "productType": "wireless"
    }
]
```

```Python
>>> print(response)
[{ 'name': 'My AP', 'lat': 37.4180951010362, 'lng': -122.098531723022, 'address': '1600 Pennsylvania Ave', 'notes': 'My AP note', 'tags': [ 'recently-added' ], 'networkId': 'N_24329156', 'serial': 'Q234-ABCD-5678', 'model': 'MR34', 'mac': '00:11:22:33:44:55', 'lanIp': '1.2.3.4', 'firmware': 'wireless-25-14', 'productType': 'wireless'}]
```

Note the `serial` for use in requests allowing a serial as path or query parameter. If you have two devices in your organization, note two of them.

## Get devices uplinks addresses

Depending on configuration, some Meraki devices support multiple uplink addresses. To find them, you can use this endpoint to return the uplinks addresses for _all_ devices in an organization, but for this example, we'll filter it to one or two specific devices using the `serials[]` query parameter.

[List the current uplink addresses for devices in an organization documentation](##!get-organization-devices-uplinks-addresses-by-device)

### Request for one device

`GET /organizations/:organizationId/devices/uplinks/addresses/byDevice?serials[]={serial}`

```cURL
curl https://api.meraki.com/api/v1/organizations/:organizationId/devices/uplinks/addresses/byDevice?serials[]={serial} \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationDevicesUplinksAddressesByDevice({organizationId}, serials=["{serial}"])
```

### Response for one device

```JSON
Successful HTTP Status: 200
[
 {
  "mac": "00:11:22:33:44:55",
  "name": "My Switch 1",
  "network": {
   "id": "L_24329156"
  },
  "productType": "switch",
  "serial": "{serial}",
  "tags": [
   "example",
   "switch"
  ],
  "uplinks": [
   {
    "interface": "man1",
    "addresses": [
     {
      "protocol": "ipv4",
      "address": "10.0.1.2",
      "gateway": "10.0.1.1",
      "assignmentMode": "dynamic",
      "nameservers": {
       "addresses": [
        "208.67.222.222",
        "208.67.220.220"
       ]
      },
      "public": {
       "address": "78.11.19.49"
      }
     },
     {
      "protocol": "ipv6",
      "address": "2600:1700:ae0::c8ff:fe1e:12d2",
      "gateway": "fe80::fe1b:202a",
      "assignmentMode": "dynamic",
      "nameservers": {
       "addresses": [
        "::",
        "::"
       ]
      },
      "public": {
       "address": None
      }
     }
    ]
   }
  ]
 }
]
```

```Python
[{'mac': '00:11:22:33:44:55', 'name': 'My Switch 1', 'network': {'id': 'L_24329156'}, 'productType': 'switch', 'serial': '{serial}', 'tags': ['example', 'switch'], 'uplinks': [{'interface': 'man1', 'addresses': [{'protocol': 'ipv4', 'address': '10.0.1.2', 'gateway': '10.0.1.1', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['208.67.222.222', '208.67.220.220']}, 'public': {'address': '78.11.19.49'}}, {'protocol': 'ipv6', 'address': '2600:1700:ae0::c8ff:fe1e:12d2', 'gateway': 'fe80::fe1b:202a', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['::', '::']}, 'public': {'address': None}}]}]}]
```

### Request for two devices

`GET /organizations/:organizationId/devices/uplinks/addresses/byDevice?serials[]={serial1}&serials[]={serial1}&serials[]={serial2}`

```cURL
curl https://api.meraki.com/api/v1/organizations/:organizationId/devices/uplinks/addresses/byDevice?serials[]={serial1}&serials[]={serial2} \
  -L -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

```Python
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
response = dashboard.organizations.getOrganizationDevicesUplinksAddressesByDevice({organizationId}, serials=["{serial1}", "{serial2}"])
```

### Response for two devices

```Python
>>> print(response)
[{'mac': '00:11:22:33:44:55', 'name': 'My Switch 1', 'network': {'id': 'L_24329156'}, 'productType': 'switch', 'serial': '{serial1}', 'tags': ['example', 'switch'], 'uplinks': [{'interface': 'man1', 'addresses': [{'protocol': 'ipv4', 'address': '10.0.1.2', 'gateway': '10.0.1.1', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['208.67.222.222', '208.67.220.220']}, 'public': {'address': '78.11.19.49'}}, {'protocol': 'ipv6', 'address': '2600:1700:ae0::c8ff:fe1e:12d2', 'gateway': 'fe80::fe1b:202a', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['::', '::']}, 'public': {'address': None}}]}]}, {'mac': '00:11:22:33:44:55', 'name': 'My Switch 2', 'network': {'id': 'L_24329156'}, 'productType': 'switch', 'serial': '{serial2}', 'tags': ['example', 'switch'], 'uplinks': [{'interface': 'man1', 'addresses': [{'protocol': 'ipv4', 'address': '10.0.1.3', 'gateway': '10.0.1.1', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['208.67.222.222', '208.67.220.220']}, 'public': {'address': '78.11.19.49'}}, {'protocol': 'ipv6', 'address': '2600:1700:ae0:f84c::9c2f', 'gateway': 'fe80::aa46::202a', 'assignmentMode': 'dynamic', 'nameservers': {'addresses': ['::', '::']}, 'public': {'address': None}}]}]}]
```
