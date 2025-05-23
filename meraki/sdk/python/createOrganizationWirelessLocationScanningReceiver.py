import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
network = {'id': 'L_1234'}
url = 'https://www.myreceiver.com'
version = '3'
radio = {'type': 'Wi-Fi'}
shared_secret = 'mysecretvalue'

response = dashboard.wireless.createOrganizationWirelessLocationScanningReceiver(
    organization_id, network, url, version, radio, shared_secret
)

print(response)