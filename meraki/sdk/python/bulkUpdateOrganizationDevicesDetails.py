import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
serials = ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003']
details = [{'name': 'username', 'value': 'ABC'}, {'name': 'password', 'value': 'ABC123'}, {'name': 'enable password', 'value': 'ABC123'}]

response = dashboard.organizations.bulkUpdateOrganizationDevicesDetails(
    organization_id, serials, details
)

print(response)