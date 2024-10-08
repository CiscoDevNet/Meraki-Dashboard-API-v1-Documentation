## Authorization

Dashboard API v1 supports Bearer Auth using the standard `Authorization` header parameter. The value will be a string that begins with the word `Bearer`, followed by your Meraki API key.

> **Note:** When developing scripts, it's a best practice to create a local environment variable `MERAKI_DASHBOARD_API_KEY` and set it to your API key, so that you can omit it from your source code. Instructions vary by operating system, so please consult your OS vendor for more information.

```JSON
{
 "Authorization": "Bearer <API_KEY>"
}
```

```cURL
curl https://api.meraki.com/api/v1/organizations \
  -L -H 'Authorization: Bearer {API_KEY}'
```

```Python
# Example 1: Best practice
# This example will read the local environment variable `MERAKI_DASHBOARD_API_KEY`
# so that you don't have to add it to your source code. Please see above if you
# haven't already created this environment variable.
import meraki
dashboard = meraki.DashboardAPI()

# Example 2: Riskier
# Defining your API key as a variable in source code is not recommended. Please
# consult the above regarding best practices.
import meraki
API_KEY = '6bec40cf957de430a6f1f2baf056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(API_KEY)
```

## Obtaining your Meraki API key

In order to interact with the Dashboard API, you must first obtain an API key. Cisco Meraki Dashboard API is enabled by default on all organizations.

- Open your Meraki dashboard: <https://dashboard.meraki.com>
- Once logged in, navigate to the 'My Profile' page accessed via the avatar icon in the top right-hand corner of dashboard to generate the API key.

> save this key in a secure location, as it represents your admin credentials

<img src="../images/dashGenerateAPIkey.png" width="400px">

### Troubleshooting

If you get a 401 Unauthorized error (with message _"Missing API key"_) when using dashboard API v1 with Bearer token, check the following to troubleshoot:

1. As an example, when using your API key to retrieve the [GET /organizations](##!get-organizations) operation, you should see the same data as shown when navigating to [https://api.meraki.com/api/v1/organizations](https://api.meraki.com/api/v1/organizations) in your browser, using an authenticated session with the credentials that generated the API key.

2. Next, check that your API call has the correct header with the following (and not v0's `X-Cisco-Meraki-API-Key`):

```JSON
Authorization: Bearer {API_KEY}
```

3. If making the API call in cURL, check that the **--location-trusted** flag is included.

4. If making the API call in Postman, check that the setting “_Follow Authorization header_” is enabled.
<img src="../images/authorizationPostman.png" width="600px">

5. If using the [Python library](pythonLibrary.md), authorization is handled automatically, so assuming the right API key is supplied, the Python code snippet for [getOrganizations](##!get-organizations) > _Template_ > _Meraki Python Library_ will work w/ the v1 library installed.
<img src="../images/authorizationPython.png" width="800px">

6. If you really want to write your own functions in Python, then you will need to define a new instance of the **requests.Session** class that does not _rebuild_auth_ upon a redirect. For example:

```python
from requests import Session
class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
      '''
      No code here means requests will always preserve the Authorization header when redirected.
      Be careful not to leak your credentials to untrusted hosts!
      '''
session = NoRebuildAuthSession()
API_KEY = '6bec40cf957de430a6f1f2baf056b99a4fac9ea0'
response = session.get('https://api.meraki.com/api/v1/organizations/', headers={'Authorization': f'Bearer {API_KEY}'})
print(response.JSON())
```

7. If using PowerShell with **Invoke-RestMethod**, make sure that the _-PreserveAuthorizationOnRedirect_ flag is included.

8. The behavior here is standard and due to API clients like cURL and Postman stripping the Authorization header, for security purposes, when following an HTTP redirect.
