import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
interface_id = ''

response = dashboard.switch.updateDeviceSwitchRoutingInterfaceDhcp(
    serial, interface_id, 
    dhcpMode='dhcpServer', 
    dhcpRelayServerIps=['1.2.3.4'], 
    dhcpLeaseTime='1 day', 
    dnsNameserversOption='custom', 
    dnsCustomNameservers=['8.8.8.8, 8.8.4.4'], 
    bootOptionsEnabled=True, 
    bootNextServer='1.2.3.4', 
    bootFileName='home_boot_file', 
    dhcpOptions=[{'code': '5', 'type': 'text', 'value': 'five'}], 
    reservedIpRanges=[{'start': '192.168.1.1', 'end': '192.168.1.10', 'comment': 'A reserved IP range'}], 
    fixedIpAssignments=[{'name': 'Cisco Meraki valued client', 'mac': '22:33:44:55:66:77', 'ip': '192.168.1.12'}]
)

print(response)