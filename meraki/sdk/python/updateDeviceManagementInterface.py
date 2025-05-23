import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.devices.updateDeviceManagementInterface(
    serial, 
    wan1={'wanEnabled': 'not configured', 'usingStaticIp': True, 'staticIp': '1.2.3.4', 'staticGatewayIp': '1.2.3.1', 'staticSubnetMask': '255.255.255.0', 'staticDns': ['1.2.3.2', '1.2.3.3'], 'vlan': 7}, 
    wan2={'wanEnabled': 'enabled', 'usingStaticIp': False, 'staticIp': '1.2.3.4', 'staticGatewayIp': '1.2.3.1', 'staticSubnetMask': '255.255.255.0', 'staticDns': ['1.2.3.2', '1.2.3.3'], 'vlan': 2}
)

print(response)