import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
switch_stack_id = ''
interface_id = ''

response = dashboard.switch.updateNetworkSwitchSwitchStackRoutingInterfaceDhcp(
    network_id, switch_stack_id, interface_id, 
    dhcpMode='dhcpServer', 
    dhcpLeaseTime='1 day', 
    dnsNameserversOption='custom', 
    dnsCustomNameservers=['8.8.8.8, 8.8.4.4'], 
    bootOptionsEnabled=True, 
    bootNextServer='1.2.3.4', 
    bootFileName='home_boot_file', 
    dhcpOptions=[{'code': '5', 'type': 'text', 'value': 'five'}], 
    reservedIpRanges=[{'start': '192.168.1.1', 'end': '192.168.1.10', 'comment': 'A reserved IP range'}], 
    fixedIpAssignments=[{'mac': '22:33:44:55:66:77', 'name': 'Cisco Meraki valued client', 'ip': '192.168.1.12'}]
)

print(response)