import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

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