import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchStp(
    network_id, 
    rstpEnabled=True, 
    stpBridgePriority=[{'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'stpPriority': 4096}, {'stacks': ['789102', '123456', '129102'], 'stpPriority': 28672}]
)

print(response)