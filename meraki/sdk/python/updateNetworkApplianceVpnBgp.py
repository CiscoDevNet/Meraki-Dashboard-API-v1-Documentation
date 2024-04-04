import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
enabled = True

response = dashboard.appliance.updateNetworkApplianceVpnBgp(
    network_id, enabled, 
    asNumber=64515, 
    ibgpHoldTimer=120, 
    neighbors=[{'ip': '10.10.10.22', 'ipv6': {'address': '2002::1234:abcd:ffff:c0a8:101'}, 'remoteAsNumber': 64343, 'receiveLimit': 120, 'allowTransit': True, 'ebgpHoldTimer': 180, 'ebgpMultihop': 2, 'sourceInterface': 'wan1', 'nextHopIp': '1.2.3.4', 'ttlSecurity': {'enabled': False}, 'authentication': {'password': 'abc123'}}]
)

print(response)