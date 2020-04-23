import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
rules = [{'lanIp': '192.168.128.1', 'allowedIps': ['any'], 'name': 'Description of Port Forwarding Rule', 'protocol': 'tcp', 'publicPort': '8100-8101', 'localPort': '442-443', 'uplink': 'both'}]

response = dashboard.appliance.updateNetworkApplianceFirewallPortForwardingRules(
    network_id, rules
)

print(response)