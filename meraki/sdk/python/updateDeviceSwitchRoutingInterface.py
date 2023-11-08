import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
interface_id = ''

response = dashboard.switch.updateDeviceSwitchRoutingInterface(
    serial, interface_id, 
    name='L3 interface', 
    subnet='192.168.1.0/24', 
    interfaceIp='192.168.1.2', 
    multicastRouting='disabled', 
    vlanId=100, 
    defaultGateway='192.168.1.1', 
    ospfSettings={'area': '0', 'cost': 1, 'isPassiveEnabled': True}, 
    ospfV3={'area': '1', 'cost': 2, 'isPassiveEnabled': True}, 
    ipv6={'assignmentMode': 'static', 'prefix': '1:2:3:4::/48', 'address': '1:2:3:4::1', 'gateway': '1:2:3:4::2'}
)

print(response)