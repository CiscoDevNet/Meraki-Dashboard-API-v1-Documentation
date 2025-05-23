import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.devices.createDeviceLiveToolsThroughputTest(
    serial, 
    callback={'url': 'https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031', 'sharedSecret': 'secret', 'httpServer': {'id': 'aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M='}, 'payloadTemplate': {'id': 'wpt_2100'}}
)

print(response)