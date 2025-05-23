import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
custom_performance_class_id = ''

response = dashboard.appliance.getNetworkApplianceTrafficShapingCustomPerformanceClass(
    network_id, custom_performance_class_id
)

print(response)