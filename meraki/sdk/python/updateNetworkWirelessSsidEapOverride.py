import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidEapOverride(
    network_id, number, 
    timeout=5, 
    identity={'retries': 5, 'timeout': 5}, 
    maxRetries=5, 
    eapolKey={'retries': 5, 'timeoutInMs': 5000}
)

print(response)