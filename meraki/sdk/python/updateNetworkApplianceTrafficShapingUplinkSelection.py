import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceTrafficShapingUplinkSelection(
    network_id, 
    activeActiveAutoVpnEnabled=True, 
    defaultUplink='wan1', 
    loadBalancingEnabled=True, 
    failoverAndFailback={'immediate': {'enabled': True}}, 
    wanTrafficUplinkPreferences=[{'trafficFilters': [{'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': '1-1024', 'cidr': '192.168.1.0/24', 'vlan': 10, 'host': 254}, 'destination': {'port': 'any', 'cidr': 'any'}}}], 'preferredUplink': 'wan1'}], 
    vpnTrafficUplinkPreferences=[{'trafficFilters': [{'type': 'applicationCategory', 'value': {'id': 'meraki:layer7/category/1', 'protocol': 'tcp', 'source': {'port': 'any', 'cidr': '192.168.1.0/24', 'network': 'L_23456789', 'vlan': 20, 'host': 200}, 'destination': {'port': '1-1024', 'cidr': 'any', 'network': 'L_12345678', 'vlan': 10, 'host': 254, 'fqdn': 'www.google.com'}}}], 'preferredUplink': 'bestForVoIP', 'failOverCriterion': 'poorPerformance', 'performanceClass': {'type': 'custom', 'builtinPerformanceClassName': 'VoIP', 'customPerformanceClassId': '123456'}}]
)

print(response)