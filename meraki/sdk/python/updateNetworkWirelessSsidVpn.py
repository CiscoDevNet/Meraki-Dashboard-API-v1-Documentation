import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidVpn(
    network_id, number, 
    concentrator={'networkId': 'N_123', 'vlanId': 44, 'name': 'some concentrator name'}, 
    splitTunnel={'enabled': True, 'rules': [{'protocol': 'Any', 'destCidr': '1.1.1.1/32', 'destPort': 'any', 'policy': 'allow', 'comment': 'split tunnel rule 1'}, {'destCidr': 'foo.com', 'destPort': 'any', 'policy': 'deny', 'comment': 'split tunnel rule 2'}]}, 
    failover={'requestIp': '1.1.1.1', 'heartbeatInterval': 10, 'idleTimeout': 30}
)

print(response)