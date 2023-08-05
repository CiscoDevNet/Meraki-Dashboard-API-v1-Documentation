import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchDhcpServerPolicy(
    network_id, 
    alerts={'email': {'enabled': True}}, 
    defaultPolicy='block', 
    allowedServers=['00:50:56:00:00:01', '00:50:56:00:00:02'], 
    blockedServers=['00:50:56:00:00:03', '00:50:56:00:00:04'], 
    arpInspection={'enabled': True}
)

print(response)