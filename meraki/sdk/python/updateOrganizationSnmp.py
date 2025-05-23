import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'

response = dashboard.organizations.updateOrganizationSnmp(
    organization_id, 
    v2cEnabled=False, 
    v3Enabled=True, 
    v3AuthMode='SHA', 
    v3AuthPass='password', 
    v3PrivMode='AES128', 
    v3PrivPass='password', 
    peerIps=['123.123.123.1']
)

print(response)