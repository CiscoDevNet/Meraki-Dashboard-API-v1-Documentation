import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
switch_stack_id = ''
interface_id = ''

response = dashboard.switch.updateNetworkSwitchStackRoutingInterface(
    network_id, switch_stack_id, interface_id, 
    name='L3 interface', 
    subnet='192.168.1.0/24', 
    interfaceIp='192.168.1.2', 
    multicastRouting='disabled', 
    vlanId=100, 
    ospfSettings={'area': '0', 'cost': 1, 'isPassiveEnabled': True}, 
    ipv6={'assignmentMode': 'static', 'address': '1:2:3:4::1', 'prefix': '1:2:3:4::/48', 'gateway': '1:2:3:4::2'}
)

print(response)