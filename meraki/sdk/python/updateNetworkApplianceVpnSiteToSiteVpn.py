import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
mode = 'spoke'

response = dashboard.appliance.updateNetworkApplianceVpnSiteToSiteVpn(
    network_id, mode, 
    hubs=[{'hubId': 'N_4901849', 'useDefaultRoute': True}, {'hubId': 'N_1892489', 'useDefaultRoute': False}], 
    subnets=[{'localSubnet': '192.168.1.0/24', 'useVpn': True}, {'localSubnet': '192.168.128.0/24', 'useVpn': True}]
)

print(response)