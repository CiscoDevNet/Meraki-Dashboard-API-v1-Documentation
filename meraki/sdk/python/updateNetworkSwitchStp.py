import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchStp(
    network_id, 
    rstpEnabled=True, 
    stpBridgePriority=[{'switchProfiles': ['1098', '1099', '1100'], 'switches': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'stacks': ['789102', '123456', '129102'], 'stpPriority': 4096}]
)

print(response)