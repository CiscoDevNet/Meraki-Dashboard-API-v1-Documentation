import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
idp_id = ''

response = dashboard.organizations.updateOrganizationSamlIdp(
    organization_id, idp_id, 
    x509certSha1Fingerprint='00:11:22:33:44:55:66:77:88:99:00:11:22:33:44:55:66:77:88:99', 
    sloLogoutUrl='https://somewhere.com'
)

print(response)