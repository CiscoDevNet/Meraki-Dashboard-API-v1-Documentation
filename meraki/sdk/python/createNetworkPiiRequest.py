import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.createNetworkPiiRequest(
    network_id, 
    type='delete', 
    datasets=['usage', 'events'], 
    username='milesmeraki', 
    email='miles@meraki.com', 
    mac='00:11:22:33:44:55', 
    smDeviceId='15551677676480', 
    smUserId='212406'
)

print(response)