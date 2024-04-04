import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchMtu(
    network_id, 
    defaultMtuSize=9578, 
    overrides=[{'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'switchProfiles': ['1284392014819', '2983092129865'], 'mtuSize': 1500}]
)

print(response)