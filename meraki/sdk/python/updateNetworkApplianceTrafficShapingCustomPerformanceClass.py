import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
custom_performance_class_id = ''

response = dashboard.appliance.updateNetworkApplianceTrafficShapingCustomPerformanceClass(
    network_id, custom_performance_class_id, 
    name='myCustomPerformanceClass', 
    maxLatency=100, 
    maxJitter=100, 
    maxLossPercentage=5
)

print(response)