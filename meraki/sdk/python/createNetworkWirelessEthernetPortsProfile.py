import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'name'
ports = [{'name': 'port', 'enabled': True, 'ssid': 1, 'pskGroupId': '2'}]

response = dashboard.wireless.createNetworkWirelessEthernetPortsProfile(
    network_id, name, ports, 
    usbPorts=[{'name': 'usb port', 'enabled': True, 'ssid': 2}]
)

print(response)