import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
mode = 'spoke'

response = dashboard.appliance.updateNetworkApplianceVpnSiteToSiteVpn(
    network_id, mode, 
    hubs=[{'hubId': 'N_4901849', 'useDefaultRoute': True}], 
    subnets=[{'localSubnet': '192.168.1.0/24', 'useVpn': True}]
)

print(response)