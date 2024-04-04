import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
switch_stack_id = ''
name = 'L3 interface'
vlan_id = 100

response = dashboard.switch.createNetworkSwitchStackRoutingInterface(
    network_id, switch_stack_id, name, vlan_id, 
    subnet='192.168.1.0/24', 
    interfaceIp='192.168.1.2', 
    multicastRouting='disabled', 
    defaultGateway='192.168.1.1', 
    ospfSettings={'area': '0', 'cost': 1, 'isPassiveEnabled': True}, 
    ipv6={'assignmentMode': 'static', 'prefix': '1:2:3:4::/48', 'address': '1:2:3:4::1', 'gateway': '1:2:3:4::2'}
)

print(response)