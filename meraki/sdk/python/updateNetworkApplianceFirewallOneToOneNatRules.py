import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
rules = [{'name': 'Service behind NAT', 'lanIp': '192.168.128.22', 'publicIp': '146.12.3.33', 'uplink': 'internet1', 'allowedInbound': [{'protocol': 'tcp', 'destinationPorts': ['80'], 'allowedIps': ['10.82.112.0/24', '10.82.0.0/16']}, {'protocol': 'udp', 'destinationPorts': ['8080'], 'allowedIps': ['10.81.110.5', '10.81.0.0/16']}]}]

response = dashboard.appliance.updateNetworkApplianceFirewallOneToOneNatRules(
    network_id, rules
)

print(response)