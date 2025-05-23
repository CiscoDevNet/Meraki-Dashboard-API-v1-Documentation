import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
devices = [{'serial': 'Q234-ABCD-5678', 'switchports': '1, 2', 'interface': 'TenGigabitEthernet0/0/0'}]
name = 'Capture no. 3'

response = dashboard.organizations.bulkOrganizationDevicesPacketCaptureCapturesCreate(
    organization_id, devices, name, 
    notes='Debugging persistent issue on device', 
    duration=60, 
    filterExpression='(icmp)'
)

print(response)