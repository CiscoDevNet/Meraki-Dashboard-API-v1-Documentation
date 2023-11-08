import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchRoutingMulticast(
    network_id, 
    defaultSettings={'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}, 
    overrides=[{'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}, {'stacks': ['789102', '123456', '129102'], 'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}, {'switchProfiles': ['1234', '4567'], 'igmpSnoopingEnabled': True, 'floodUnknownMulticastTrafficEnabled': True}]
)

print(response)