import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'

response = dashboard.switch.updateNetworkSwitchMtu(
    network_id, 
    defaultMtuSize=9578, 
    overrides=[{'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'mtuSize': 1500}, {'switchProfiles': ['1284392014819', '2983092129865'], 'mtuSize': 1600}]
)

print(response)