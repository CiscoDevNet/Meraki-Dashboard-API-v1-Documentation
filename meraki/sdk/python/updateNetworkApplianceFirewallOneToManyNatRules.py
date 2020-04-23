import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
rules = [{'publicIp': '146.11.11.13', 'uplink': 'internet1', 'portRules': [{'name': 'Rule 1', 'protocol': 'tcp', 'publicPort': '9443', 'localIp': '192.168.128.1', 'localPort': '443', 'allowedIps': ['any']}, {'name': 'Rule 2', 'protocol': 'tcp', 'publicPort': '8080', 'localIp': '192.168.128.1', 'localPort': '80', 'allowedIps': ['10.82.110.0/24', '10.82.111.0/24']}]}]

response = dashboard.appliance.updateNetworkApplianceFirewallOneToManyNatRules(
    network_id, rules
)

print(response)