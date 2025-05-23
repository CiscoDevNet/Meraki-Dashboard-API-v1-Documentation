import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
record_id = ''

response = dashboard.appliance.updateOrganizationApplianceDnsLocalRecord(
    organization_id, record_id, 
    hostname='www.test.com', 
    address='10.1.1.0', 
    profile={'id': '1'}
)

print(response)