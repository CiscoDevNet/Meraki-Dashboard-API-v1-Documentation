import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'

response = dashboard.cellulargateway.updateNetworkCellularGatewayConnectivityMonitoringDestinations(
    network_id, 
    destinations=[{'ip': '8.8.8.8', 'description': 'Google', 'default': False}, {'ip': '1.23.45.67', 'description': 'test description', 'default': True}, {'ip': '9.8.7.6'}]
)

print(response)