import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.devices.updateDeviceCellularSims(
    serial, 
    sims=[{'slot': 'sim1', 'isPrimary': False, 'apns': [{'name': 'internet', 'allowedIpTypes': ['ipv4', 'ipv6'], 'authentication': {'type': 'pap', 'username': 'milesmeraki', 'password': 'secret'}}], 'simOrder': 3}], 
    simOrdering=['sim1', 'sim2', 'sim3'], 
    simFailover={'enabled': True, 'timeout': 300}
)

print(response)