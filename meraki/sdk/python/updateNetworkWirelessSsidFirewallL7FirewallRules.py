import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidFirewallL7FirewallRules(
    network_id, number, 
    rules=[{'policy': 'deny', 'type': 'application', 'value': {'id': 'meraki:layer7/application/67', 'name': 'Xbox LIVE'}}, {'policy': 'deny', 'type': 'applicationCategory', 'value': {'id': 'meraki:layer7/category/2', 'name': 'Blogging'}}, {'policy': 'deny', 'type': 'host', 'value': 'google.com'}, {'policy': 'deny', 'type': 'port', 'value': '23'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}]
)

print(response)