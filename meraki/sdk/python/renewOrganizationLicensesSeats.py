import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
license_id_to_renew = '123'
unused_license_id = '1234'

response = dashboard.organizations.renewOrganizationLicensesSeats(
    organization_id, license_id_to_renew, unused_license_id
)

print(response)