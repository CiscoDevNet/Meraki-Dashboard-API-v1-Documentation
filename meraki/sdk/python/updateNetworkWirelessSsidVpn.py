import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidVpn(
    network_id, number, 
    concentrator={'networkId': 'N_123', 'name': 'some concentrator name'}, 
    splitTunnel={'enabled': True, 'rules': [{'protocol': 'Any', 'destCidr': '1.1.1.1/32', 'destPort': 'any', 'policy': 'allow', 'comment': 'split tunnel rule 1'}, {'destCidr': 'foo.com', 'destPort': 'any', 'policy': 'deny', 'comment': 'split tunnel rule 2'}]}, 
    failover={'requestIp': '1.1.1.1', 'heartbeatInterval': 10, 'idleTimeout': 30}
)

print(response)