import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceTrafficShapingUplinkBandwidth(
    network_id, 
    bandwidthLimits={'wan1': {'limitUp': 1000000, 'limitDown': 1000000}, 'wan2': {'limitUp': 1000000, 'limitDown': 1000000}, 'cellular': {'limitUp': 1000000, 'limitDown': 1000000}}
)

print(response)