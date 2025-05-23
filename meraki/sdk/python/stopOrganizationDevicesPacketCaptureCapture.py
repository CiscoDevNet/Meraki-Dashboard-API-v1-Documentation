import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
capture_id = ''
serials = ['Q234-ABCD-5678']

response = dashboard.organizations.stopOrganizationDevicesPacketCaptureCapture(
    organization_id, capture_id, serials
)

print(response)