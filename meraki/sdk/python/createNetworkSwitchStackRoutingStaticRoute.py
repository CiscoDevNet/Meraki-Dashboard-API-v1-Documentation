import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

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