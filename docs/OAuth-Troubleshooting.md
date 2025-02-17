
## Troubleshooting Initial Grant Flow
**Issue 1:** The administrator cannot find the relevant organization in the dropdown menu.

**Solution:**
For an administrator to find an organization in the dropdown menu, do the following:
- Ensure that the Meraki administrator has full **Organization admin** rights. Both the "Organization admin" with read-only permissions and the "Network admin" have insufficient permissions to view the organization.
- Ensure that the application has been integrated.
- If the application has been integrated, you can revoke the it's access, and try integrating the application again. From the Meraki dashboard left-navigation pane, choose **Organization**>**Integrations**. From the **My integrations** tab, choose your integration. From the integration window that opens, from the top-right corner, click **Remove**. Now try integrating the application again. 

**Issue 2**: "An error has occurred: The requested redirect URI is malformed or doesn't match the client redirect URI."

**Solution**: Check whether the redirect URI in the request differs from the redirect URIs that were registered in the application registry.

**Issue 3**: Client authentication failed error. "An error has occurred: Client authentication failed due to an unknown client, no client authentication included, or unsupported authentication method.."

**Solution**: Check whether the client ID in the request is correct.


### Troubleshooting Errors Returned to the Redirect URI
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

**Issue**: The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client.

**Solution**:
- Ensure that the access grant has not been used already.
- Confirm that no more than 10 minutes have passed since the access grant was generated.
- Check whether the access grant matches the expected parameters, including the redirection URI and client details.

