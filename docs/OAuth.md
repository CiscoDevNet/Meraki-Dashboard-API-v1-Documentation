# OAuth 2.0
## OAuth 2.0 integration
An Open Authorization (OAuth) 2.0 integration (integration) is a software application or system that connects to the Meraki platform and interacts with Meraki's services and data. This integration forms a crucial link between external applications and Meraki's infrastructure, facilitating smooth interaction with the platform.

An integration uses API to automate, manage, or enhance functionalities within a Meraki environment. 

With OAuth 2.0, integrations enable developers to access Meraki resources securely. This secure access allows developers to monitor network status, configure settings, and collect data without needing to input credentials directly.

### OAuth 2.0 
OAuth 2.0 is a standard authorization framework that offers integrations to access Meraki data securely, eliminating the need for administrators to reveal their credentials or API keys. OAuth 2.0 is commonly used to allow delegated access, particularly in the context of API and web applications. OAuth 2.0 offers a secure, standardized method for the network administrator to authorize third-party access to their resources while maintaining data control.
[Learn more about the OAuth framework and definitions](https://oauth.net/2/)

### Benefits of OAuth 2.0 integrations

Using OAuth 2.0 for authentication offers several advantages compared to traditional API keys, including:

- **Flexible and least-privilege access**: Developers can request permission for a limited set of OAuth scopes, rather than having all-or-nothing access.
- **Avoid copy-pasting API keys**: OAuth 2.0 offers a secure, seamless process for exchanging credentials.
- **Avoid API key rotations**: OAuth 2.0 uses short-lived access tokens. These tokens rotate automatically every 60 minutes.
- **Simplified auditing**: Each integration has its identity, which makes it easy to trace API calls back to the integration invoking the API call.

### Guidelines for building an OAuth 2.0 integration
- Store the `refresh_token` and the `access_token` securely.
- Use HTTP Authentication.
  
### Building an OAuth 2.0 integration

Use OAuth 2.0 integration for secure access to Meraki resources, allowing structured authorization to applications.

You can build an OAuth integration with these components:
- **Application registry**: The platform where you register your application to get the necessary credentials.
- **Administrator**: The entity responsible for granting permissions to manage the organization.
- **Access token**: A token used to authenticate API calls to Meraki resources. An access token expires 60 minutes (one hour) after being generated.
- **Refresh token**: A token that is long-lived and used to get new access tokens once they expire. Always store the refresh tokens securely. The refresh token is automatically revoked after 90 days of inactivity.

These are the stages of building an OAuth 2.0 integration:
1. Register your integration with Meraki.
2. Request the administrator for permission to manage that organization using the OAuth Grant Flow. 
3. Acquire and use tokens to make API calls.
4. Refresh your tokens to ensure secure and continuous access to your Meraki resources.

#### 1. Register your integration with Meraki
To register your application, you must provide the necessary details in the application registry.

**Before you begin**: 
- Ensure you have Cisco.com credentials to access the application registry.
- Understand OAuth scopes. See the OAuth Scopes section. 

Follow these steps to register your application:
- Step 1: Access the application registry at [integrate.cisco.com](https://integrate.cisco.com) using your Cisco.com credentials.
- Step 2: Create a new application, provide the name and redirect URIs, select the relevant scopes, and enter any requested information. You can modify the scopes and redirect URIs later as well.

**Result**: Your application is registered, and you have the credentials that are needed for OAuth integration.

**Requirement**: Store the `client_secret` securely as it is displayed only once. 

#### 2.Request permission using an OAuth grant flow
To get permission to manage a Meraki organization, use the OAuth Grant Flow. This procedure involves obtaining an access grant from an administrator.

Follow these steps to request permission:
- Step 1: Trigger the OAuth process in your application, such as with a "Connect to Meraki" button or a link.
- Step 2: Redirect the administrator to [https://as.meraki.com/oauth/authorize](https://as.meraki.com/oauth/authorize) with the required query parameters:
  
  - `response_type`: Must be set as `code`
  - `client_id`: Issued when creating your application
  - `redirect_uri`: Must match one of the URIs provided when you registered your integration
  - `scope`: Your integration requests this space-separated list of scopes (see the "Understanding OAuth Scopes" section below)
  - `state`: A unique string passed back to your integration upon completion
  - `nonce` (optional)
  
	Here is an example link format:
	   ```
	https://as.meraki.com/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_url}&scope={scopes}
	```
- Step 3: Add a callback receiver to your application to handle responses when a request returns the redirection URL. Expect to receive a `code` attribute as one of the request parameters, which serves as the **access grant**. The access grant is valid for 10 minutes after issuance

**Result**: You receive an access grant valid for 10 minutes.

#### 3. Acquire and use tokens to make API calls
To authenticate API calls, acquire and use tokens obtained through the authorization process. Tokens are required to make authenticated API requests to Meraki resources.

Follow these steps to acquire and use tokens:
- Step 1: Use the received access grant to request an access token and a refresh token by sending a POST request to [https://as.meraki.com/oauth/token](https://as.meraki.com/oauth/token).
- Step 2: Include these parameters:
	- 	Headers: `Content-Type: application/x-www-form-urlencoded`.
	- 	Authentication: Basic authentication using the `client_id` and `client_secret`.
	- 	Payload:
	
		     ```
		     {
		       "grant_type": "authorization_code",
		       "code": "{access_code}",
		       "redirect_uri": "{redirect_url}",
		       "scope": "{scopes}"
		     }
		     ``
	  	The response includes the `access_token`, which is valid for 60 minutes (one hour), and the `refresh_token`, which is used to generate a new `access_token`.

- Step 3: Make API calls using the access token with the `Authorization` header in the format `Bearer <access_token>` format.
  
		```json
		{
			"Authorization": "Bearer <access_token>"
		}
		```

**Result**: You have acquired tokens and can securely interact with Meraki resources using the access tokens. You can now swap your API key with the access token in most operations.

**Required**: Store the `refresh token` securely.

#### 4. Refresh your tokens
Access tokens expire after 60 minutes (one hour) and require refreshing. To maintain continuous access to Meraki resources, refresh your access tokens as needed. 

Follow these steps to refresh your access tokens using your refresh token:
- Step 1: Send a POST request to `https://as.meraki.com/oauth/token`.
- Step 2: Include headers `Content-Type: application/x-www-form-urlencoded`.
- Step 3: Include the payload `grant_type=refresh_token&refresh_token={refresh_token}`.
- Step 4: Use HTTP basic authentication.

**Result**: You receive a new `access_token` and `refresh_token`. The refresh token is long-lived and can be used to get new access tokens.  The access token expires 60 minutes after being generated. The previous refresh token is revoked for security reasons. 

**Post-requisites:** Store the `refresh_token` and `access_token` securely.

**Note:** The refresh token is automatically revoked after 90 days of inactivity.

##### RFC 6749
The Refresh Token procedure is based on [RFC 6749: Refreshing an Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-6).  To know more about OAuth client authentication, see the [Client Password](https://datatracker.ietf.org/doc/html/rfc6749#section-2.3.1.) section of RFC 6749.

### Revoke an OAuth refresh token
For revoking an OAuth refresh token, you can use the Meraki dashboard or a client application.

#### Dashboard revocation by administrator
Revoke a refresh token by using the Meraki dashboard.

**Before you begin**: You must be a Meraki **Organization admin** (resource owner).

Follow these steps for revoking your refresh token:
- Step 1: From the Meraki dashboard left-navigation pane, choose **Organization** > **Integrations**.
- Step 2: From the **My integrations** tab, choose your integration.
- Step 3: From the integration window that opens, from the top-right corner, click **Remove**.
  
**Result**: The refresh token is revoked, and all API calls using the token fail. 

**Note**: Currently, the client application is not notified when its token is revoked.

#### Client application revocation
Revoke a refresh token using a client application.

**Before you begin**: Ensure you have the `client_id` and `client_secret`.

Follow these steps for revoking the token:
- Step 1: Send a POST request to `https://as.meraki.com/oauth/revoke`.
- Step 2: Include the following in the request:
  - Headers: `Content-Type: application/x-www-form-urlencoded`.
  - Authentication: Basic Authentication using `client_id` and `client_secret`.
  - Payload: 
    ```
    {'token': <the refresh token to be revoked>,
      'token_type_hint': 'refresh_token'}
    ```

**Result**: You receive a 200 OK response if the token is successfully revoked.

**Post-requisites**: Wait up to 10 minutes for the revoked access token to stop working.

#### **RFC 7009** 
The procedure for revoking an OAuth refresh token follows the guidelines in RFC 7009 for OAuth 2.0 token revocation."

## OAuth scopes
OAuth scopes in OAuth 2.0 are used to define and limit the access rights granted to an access token. 

When an integration requests authorization from an administrator, it  must include a list of scopes that the integration seeks access to.  The Meraki Dashboard presents these scopes to the admin during the authorization process, which allows them to approve or deny the request.

OAuth 2.0 offers a flexible and granular method for controlling access to resources through the use of scopes. This enables the administrator to make informed decisions regarding the level of access granted to integrations. This mechanism supports the principle of least privilege, enhancing security and privacy.

Meraki provides the following two scopes:
1. **`config`**: This scope grants access to configuration features that influence the operation of the network and the overall network experience. The config scope dictates the end-user network experience and the functioning of Meraki devices, such as VPNs, VLANs, access controls, policies, SSIDs, and sensor names. Note that the `config` scope excludes admin-facing telemetry configurations, which are managed using telemetry scopes.

2. **`telemetry`**: This scope grants access to telemetry data and configurations that do not impact the end-user network experience. They include features like event logs, syslog, bandwidth utilization, client counts, and camera snapshots.

Note: The Meraki scopes can have either "read-only" or "write" permission levels.


| Category              | Read                           | Write                          |
|-----------------------|--------------------------------|--------------------------------|
| **Dashboard**         | dashboard:iam:config:read     | dashboard:iam:config:write     |
|                       | dashboard:iam:telemetry:read  | dashboard:iam:telemetry:write  |
|                       | dashboard:general:config:read | dashboard:general:config:write |
|                       | dashboard:general:telemetry:read | dashboard:general:telemetry:write |
|                       | dashboard:licensing:config:read | dashboard:licensing:config:write |
|                       | dashboard:licensing:telemetry:read | dashboard:licensing:telemetry:write |
| **Network**           | sdwan:config:read             | sdwan:config:write             |
|                       | switch:config:read            | switch:config:write            |
|                       | wireless:config:read          | wireless:config:write          |
|                       | sdwan:telemetry:read          | sdwan:telemetry:write          |
|                       | switch:telemetry:read         | switch:telemetry:write         |
|                       | wireless:telemetry:read       | wireless:telemetry:write       |
| **IoT**               | camera:config:read            | camera:config:write            |
|                       | sensor:config:read            | sensor:config:write            |
|                       | camera:telemetry:read         | camera:telemetry:write         |
|                       | sensor:telemetry:read         | sensor:telemetry:write         |
| **Endpoint Management (SM)** | sm:telemetry:read      | sm:telemetry:write             |
|                       | sm:config:read                | sm:config:write                |


## Troubleshooting initial grant flow
**Issue 1:** The administrator cannot find the relevant organization in the dropdown menu.

**Solution:**
For an administrator to find an organization in the dropdown menu, do the following:
- Ensure that the Meraki administrator has full **Organization admin** rights. Both the "Organization admin" with read-only permissions and the "Network admin" have insufficient permissions to view the organization.
- Ensure that the application has been integrated.
- If the application has been integrated, you can revoke its access, and try integrating the application again. From the Meraki dashboard left-navigation pane, choose **Organization**>**Integrations**. From the **My integrations** tab, choose your integration. From the integration window that opens, from the top-right corner, click **Remove**. Now try integrating the application again. 

**Issue 2**: "An error has occurred: The requested redirect URI is malformed or doesn't match the client redirect URI."

**Solution**: Check whether the redirect URI in the request differs from the redirect URIs that were registered in the application registry.

**Issue 3**: Client authentication failed error. "An error has occurred: Client authentication failed due to an unknown client, no client authentication included, or unsupported authentication method.."

**Solution**: Check whether the client ID in the request is correct.


### Troubleshooting errors returned to the redirect URI
**Issue**: An invalid scope error is returned to the redirect URI. Here is an example of this error: 
```
https://localhost?error=invalid_scope&error_description=The+requested+scope+is+invalid%2C+unknown%2C+or+malformed.
```
In the above example, the redirect URI is `https://localhost/`.

**Solution**: 
- Check whether there is a mistake in the scopes included in the request. 
- Check whether the request includes scopes that were not included during the application's registration.

**Issue**: An access denied error is returned to the redirect URI. For example, 
```
https://localhost?error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request.
```
**Solution**: 
- Check whether the administrator has the required permissions. 

**Issue**: The provided authorization grant may be invalid, expired, or revoked. The authorization may not match the redirection URI used in the authorization request, or may have been issued to another client.

**Solution**:
- Ensure that the access grant has not been used already.
- Confirm that no more than 10 minutes have passed since the access grant was generated.
- Check whether the access grant matches the expected parameters, including the redirection URI and client details.



