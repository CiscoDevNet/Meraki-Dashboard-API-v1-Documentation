import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
static_route_id = ''

response = dashboard.appliance.updateNetworkApplianceStaticRoute(
    network_id, static_route_id, 
    name='My route', 
    subnet='192.168.1.0/24', 
    fixedIpAssignments={'22:33:44:55:66:77': {'ip': '1.2.3.4', 'name': 'Some client name'}}, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}]
)

print(response)