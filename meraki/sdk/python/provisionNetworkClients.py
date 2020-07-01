import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
clients = [{'mac': '00:11:22:33:44:55', 'clientId': 'k74272e', 'name': "Miles's phone"}]
device_policy = 'Group policy'

response = dashboard.networks.provisionNetworkClients(
    network_id, clients, device_policy, 
    groupPolicyId='101'
)

print(response)