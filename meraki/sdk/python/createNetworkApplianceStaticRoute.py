import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'My route'
subnet = '192.168.1.0/24'
gateway_ip = '1.2.3.5'

response = dashboard.appliance.createNetworkApplianceStaticRoute(
    network_id, name, subnet, gateway_ip
)

print(response)