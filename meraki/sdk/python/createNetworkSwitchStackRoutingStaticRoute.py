import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
switch_stack_id = ''
subnet = '192.168.1.0/24'
next_hop_ip = '1.2.3.4'

response = dashboard.switch.createNetworkSwitchStackRoutingStaticRoute(
    network_id, switch_stack_id, subnet, next_hop_ip, 
    name='My route', 
    advertiseViaOspfEnabled=False, 
    preferOverOspfRoutesEnabled=False
)

print(response)