import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
vlan_id = ''

response = dashboard.appliance.updateNetworkApplianceVlan(
    network_id, vlan_id, 
    name='My VLAN', 
    subnet='192.168.1.0/24', 
    applianceIp='192.168.1.2', 
    groupPolicyId='101', 
    vpnNatSubnet='192.168.1.0/24', 
    dhcpHandling='Run a DHCP server', 
    dhcpRelayServerIps=['192.168.1.0/24', '192.168.128.0/24'], 
    dhcpLeaseTime='1 day', 
    dhcpBootOptionsEnabled=False, 
    dhcpBootNextServer='1.2.3.4', 
    dhcpBootFilename='sample.file', 
    fixedIpAssignments={'22:33:44:55:66:77': {'ip': '1.2.3.4', 'name': 'Some client name'}}, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}], 
    dnsNameservers='google_dns', 
    dhcpOptions=[{'code': '5', 'type': 'text', 'value': 'five'}], 
    templateVlanType='same', 
    cidr='192.168.1.0/24', 
    mask=28, 
    ipv6={'enabled': True, 'prefixAssignments': [{'autonomous': False, 'staticPrefix': '2001:db8:3c4d:15::/64', 'staticApplianceIp6': '2001:db8:3c4d:15::1', 'origin': {'type': 'internet', 'interfaces': ['wan0']}}]}, 
    mandatoryDhcp={'enabled': True}
)

print(response)