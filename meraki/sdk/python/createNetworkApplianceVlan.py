import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
id_ = '1234'
name = 'My VLAN'

response = dashboard.appliance.createNetworkApplianceVlan(
    network_id, id_, name, 
    subnet='192.168.1.0/24', 
    applianceIp='192.168.1.2', 
    groupPolicyId='101', 
    templateVlanType='same', 
    cidr='192.168.1.0/24', 
    mask=28, 
    ipv6={'enabled': True, 'prefixAssignments': [{'autonomous': False, 'staticPrefix': '2001:db8:3c4d:15::/64', 'staticApplianceIp6': '2001:db8:3c4d:15::1', 'origin': {'type': 'internet', 'interfaces': ['wan0']}}]}, 
    dhcpHandling='Run a DHCP server', 
    dhcpLeaseTime='30 minutes', 
    mandatoryDhcp={'enabled': True}, 
    dhcpBootOptionsEnabled=True, 
    dhcpOptions=[{'code': '3', 'type': 'text', 'value': 'five'}]
)

print(response)