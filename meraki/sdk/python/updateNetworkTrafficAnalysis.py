import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.updateNetworkTrafficAnalysis(
    network_id, 
    mode='detailed', 
    customPieChartItems=[{'name': 'Item from hostname', 'type': 'host', 'value': 'example.com'}, {'name': 'Item from port', 'type': 'port', 'value': '440'}, {'name': 'Item from IP', 'type': 'ipRange', 'value': '192.1.0.0'}, {'name': 'Item from IP range (CIDR)', 'type': 'ipRange', 'value': '192.2.0.0/16'}, {'name': 'Item from IP range with port', 'type': 'ipRange', 'value': '192.3.0.0/16:80'}]
)

print(response)