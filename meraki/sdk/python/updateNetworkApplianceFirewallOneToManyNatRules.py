import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rules = [{'publicIp': '146.11.11.13', 'uplink': 'internet1', 'portRules': [{'name': 'Rule 1', 'protocol': 'tcp', 'publicPort': '9443', 'localIp': '192.168.128.1', 'localPort': '443', 'allowedIps': ['any']}, {'name': 'Rule 2', 'protocol': 'tcp', 'publicPort': '8080', 'localIp': '192.168.128.1', 'localPort': '80', 'allowedIps': ['10.82.110.0/24', '10.82.111.0/24']}]}]

response = dashboard.appliance.updateNetworkApplianceFirewallOneToManyNatRules(
    network_id, rules
)

print(response)