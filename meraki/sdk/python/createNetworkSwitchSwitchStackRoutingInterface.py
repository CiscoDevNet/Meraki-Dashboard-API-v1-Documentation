import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
switch_stack_id = ''
name = 'L3 interface'
subnet = '192.168.1.0/24'
interface_ip = '192.168.1.2'
vlan_id = 100

response = dashboard.switch.createNetworkSwitchSwitchStackRoutingInterface(
    network_id, switch_stack_id, name, subnet, interface_ip, vlan_id, 
    multicastRouting='disabled', 
    defaultGateway='192.168.1.1', 
    ospfSettings={'area': '0', 'cost': 1, 'isPassiveEnabled': True}
)

print(response)