import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.cellularGateway.updateDeviceCellularGatewayPortForwardingRules(
    serial, 
    rules=[{'name': 'test', 'lanIp': '172.31.128.5', 'publicPort': '11-12', 'localPort': '4', 'allowedIps': ['10.10.10.10', '10.10.10.11'], 'protocol': 'tcp', 'access': 'any'}]
)

print(response)