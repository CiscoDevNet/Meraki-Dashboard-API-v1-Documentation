import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
static_route_id = ''

response = dashboard.appliance.updateNetworkApplianceStaticRoute(
    network_id, static_route_id, 
    name='My route', 
    subnet='192.168.1.0/24', 
    gatewayIp='1.2.3.5', 
    gatewayVlanId='100', 
    enabled=True, 
    fixedIpAssignments={'22:33:44:55:66:77': {'ip': '1.2.3.4', 'name': 'Some client name'}}, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}]
)

print(response)