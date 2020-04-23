import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'

response = dashboard.switch.updateNetworkSwitchSettings(
    network_id, 
    vlan=100, 
    useCombinedPower=False, 
    powerExceptions=[{'serial': 'Q234-ABCD-0001', 'powerType': 'redundant'}, {'serial': 'Q234-ABCD-0002', 'powerType': 'combined'}, {'serial': 'Q234-ABCD-0003', 'powerType': 'redundant'}, {'serial': 'Q234-ABCD-0004', 'powerType': 'useNetworkSetting'}]
)

print(response)