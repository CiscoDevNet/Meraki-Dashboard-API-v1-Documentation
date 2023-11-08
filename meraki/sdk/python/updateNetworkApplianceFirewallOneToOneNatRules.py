import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rules = [{'name': 'Service behind NAT', 'lanIp': '192.168.128.22', 'publicIp': '146.12.3.33', 'uplink': 'internet1', 'allowedInbound': [{'protocol': 'tcp', 'destinationPorts': ['80'], 'allowedIps': ['10.82.112.0/24', '10.82.0.0/16']}, {'protocol': 'udp', 'destinationPorts': ['8080'], 'allowedIps': ['10.81.110.5', '10.81.0.0/16']}]}]

response = dashboard.appliance.updateNetworkApplianceFirewallOneToOneNatRules(
    network_id, rules
)

print(response)