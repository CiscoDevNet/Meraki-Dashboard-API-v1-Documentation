import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rule_ids = ['1284392014819', '2983092129865']

response = dashboard.switch.updateNetworkSwitchQosRulesOrder(
    network_id, rule_ids
)

print(response)