import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
switch_stack_id = ''
static_route_id = ''

response = dashboard.switch.updateNetworkSwitchStackRoutingStaticRoute(
    network_id, switch_stack_id, static_route_id, 
    name='My route', 
    subnet='192.168.1.0/24', 
    nextHopIp='1.2.3.4', 
    managementNextHop='1.2.3.5', 
    advertiseViaOspfEnabled=False, 
    preferOverOspfRoutesEnabled=False
)

print(response)