## Authorization

The Meraki Dashboard API uses Bearer authentication, requiring an API key to be included in the header of each request.
 
```json
{
	"Authorization": Bearer <API_KEY>
}
```

```cURL
curl https://api.meraki.com/api/v1/organizations \
  -L -H 'Authorization: Bearer {API_KEY}'
```

```Python
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY)

# Instead, use an environment variable, for example:
# export MERAKI_DASHBOARD_API_KEY=6bec40cf957de430a6f1f2baa056b99a4fac9ea0
dashboard = meraki.DashboardAPI()
```

## Obtaining your Meraki API key

In order to interact with the Dashboard API, you must first obtain an API key.

- Open your Meraki dashboard: https://dashboard.meraki.com
- Once logged in, navigate to the _Organization > Settings_ page.
- Ensure that the API Access is set to “Enable access to the Cisco Meraki Dashboard API”

![](../images/dashEnableOrgAPI.png)

Then go to your profile by clicking on your account email address (on the upper-right) _> My profile_ to generate the API key.

> save this key in a secure location, as it represents your admin credentials

<img src="../images/dashGenerateAPIkey.png" width="400px">
