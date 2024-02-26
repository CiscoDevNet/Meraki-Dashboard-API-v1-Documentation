import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
ports = ['2', '8']

response = dashboard.devices.createDeviceLiveToolsCableTest(
    serial, ports, 
    callback={'url': 'https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031', 'sharedSecret': 'secret', 'httpServer': {'id': 'aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M='}, 'payloadTemplate': {'id': 'wpt_2100'}}
)

print(response)