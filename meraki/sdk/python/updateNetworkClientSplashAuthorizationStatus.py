import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
client_id = ''
ssids = {'0': {'isAuthorized': True}, '2': {'isAuthorized': False}}

response = dashboard.networks.updateNetworkClientSplashAuthorizationStatus(
    network_id, client_id, ssids
)

print(response)