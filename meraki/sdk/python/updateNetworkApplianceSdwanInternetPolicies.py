import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceSdwanInternetPolicies(
    network_id, 
    wanTrafficUplinkPreferences=[{'preferredUplink': 'wan1', 'failOverCriterion': 'poorPerformance', 'performanceClass': {'type': 'custom', 'builtinPerformanceClassName': 'VoIP', 'customPerformanceClassId': '123456'}, 'trafficFilters': [{'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': '1-1024', 'cidr': '192.168.1.0/24', 'vlan': 10, 'host': 254}, 'destination': {'port': 'any', 'cidr': 'any', 'applications': [{'id': 'meraki:layer7/application/3', 'name': 'DNS', 'type': 'major'}]}}}]}]
)

print(response)