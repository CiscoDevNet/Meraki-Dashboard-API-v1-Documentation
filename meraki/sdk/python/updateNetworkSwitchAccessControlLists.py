import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rules = [{'comment': 'Deny SSH', 'policy': 'deny', 'ipVersion': 'ipv4', 'protocol': 'tcp', 'srcCidr': '10.1.10.0/24', 'srcPort': 'any', 'dstCidr': '172.16.30/24', 'dstPort': '22', 'vlan': '10'}]

response = dashboard.switch.updateNetworkSwitchAccessControlLists(
    network_id, rules
)

print(response)