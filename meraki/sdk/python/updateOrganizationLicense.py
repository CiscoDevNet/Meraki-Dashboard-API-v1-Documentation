import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
license_id = ''

response = dashboard.organizations.updateOrganizationLicense(
    organization_id, license_id, 
    deviceSerial='Q234-ABCD-5678'
)

print(response)