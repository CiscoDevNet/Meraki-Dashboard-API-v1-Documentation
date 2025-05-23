import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.createNetworkSwitchLinkAggregation(
    network_id, 
    switchPorts=[{'serial': 'Q234-ABCD-0001', 'portId': '1'}], 
    switchProfilePorts=[{'profile': '1234', 'portId': '2'}]
)

print(response)