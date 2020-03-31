## Authorization

The Meraki Dashboard API uses Bearer authentication, requiring an API key to be included in the header of each request.
 
```json
{
	"Authorization": Bearer <Meraki_API_Key>
}
```

```cUrl
curl https://api.meraki.com/api/v1/organizations \
  -H 'Authorization: Bearer {MERAKI-API-KEY}'
```

## Obtaining your Meraki API key

In order to interact with the Dashboard API, you must first obtain an API key.

- Open your Meraki dashboard: https://dashboard.meraki.com
- Once logged in, navigate to the Organization Settings menu.
- Ensure that the API Access is set to “Enable access to the Cisco Meraki Dashboard API”

![](../images/dashEnableOrgAPI.png)

Then go to your profile to generate the API key. 

> save this key in a secure location, as it represents your admin credentials

![](../images/dashGenerateAPIkey.png)
