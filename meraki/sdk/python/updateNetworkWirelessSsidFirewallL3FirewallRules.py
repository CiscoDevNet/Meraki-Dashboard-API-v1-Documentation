import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidFirewallL3FirewallRules(
    network_id, number, 
    rules=[{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': 443, 'destCidr': '192.168.1.0/24'}]
)

print(response)