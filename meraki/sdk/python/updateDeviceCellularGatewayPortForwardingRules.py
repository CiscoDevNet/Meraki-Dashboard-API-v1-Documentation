import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.cellularGateway.updateDeviceCellularGatewayPortForwardingRules(
    serial, 
    rules=[{'lanIp': '172.31.128.5', 'name': 'test', 'access': 'any', 'publicPort': '11-12', 'localPort': '4', 'uplink': 'both', 'protocol': 'tcp'}, {'lanIp': '172.31.128.5', 'name': 'test 2', 'access': 'restricted', 'allowedIps': ['10.10.10.10', '10.10.10.11'], 'publicPort': '99', 'localPort': '5', 'uplink': 'both', 'protocol': 'tcp'}]
)

print(response)