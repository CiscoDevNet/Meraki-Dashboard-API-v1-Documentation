import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
serials = ['Q234-ABCD-5678']
name = 'Capture no. 3'

response = dashboard.organizations.createOrganizationDevicesPacketCaptureCapture(
    organization_id, serials, name, 
    outputType='upload_to_cloud', 
    destination='upload_to_cloud', 
    ports='1, 3', 
    notes='Debugging connectivity issue...', 
    duration=3, 
    filterExpression='host 10.1.27.253', 
    interface='wireless'
)

print(response)