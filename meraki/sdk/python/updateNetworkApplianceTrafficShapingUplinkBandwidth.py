import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceTrafficShapingUplinkBandwidth(
    network_id, 
    bandwidthLimits={'wan1': {'limitUp': 1000, 'limitDown': 1000}, 'wan2': {'limitUp': 1000, 'limitDown': 1000}, 'cellular': {'limitUp': 1000, 'limitDown': 1000}}
)

print(response)