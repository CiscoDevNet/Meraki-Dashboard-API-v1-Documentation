import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchRoutingMulticast(
    network_id, 
    defaultSettings={'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}, 
    overrides=[{'switchProfiles': ['1234', '4567'], 'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'stacks': ['789102', '123456', '129102'], 'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}]
)

print(response)