import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceTrafficShapingUplinkSelection(
    network_id, 
    activeActiveAutoVpnEnabled=True, 
    defaultUplink='wan1', 
    loadBalancingEnabled=True, 
    wanTrafficUplinkPreferences=[{'trafficFilters': [{'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': 'any', 'cidr': '192.168.1.0/24'}, 'destination': {'port': 'any', 'cidr': 'any'}}}], 'preferredUplink': 'wan2'}, {'trafficFilters': [{'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': '1-1024', 'vlan': 10, 'host': 254}, 'destination': {'port': 'any', 'cidr': 'any'}}}], 'preferredUplink': 'wan1'}], 
    vpnTrafficUplinkPreferences=[{'trafficFilters': [{'type': 'applicationCategory', 'value': {'id': 'meraki:layer7/category/1'}}, {'type': 'application', 'value': {'id': 'meraki:layer7/application/33'}}, {'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': 'any', 'cidr': '192.168.1.0/24'}, 'destination': {'port': 'any', 'cidr': 'any'}}}, {'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': 'any', 'cidr': 'any'}, 'destination': {'port': 'any', 'network': 'L_23456789', 'vlan': 20, 'host': 200}}}, {'type': 'custom', 'value': {'protocol': 'tcp', 'source': {'port': 'any', 'cidr': 'any'}, 'destination': {'port': '1-1024', 'fqdn': 'www.google.com'}}}], 'preferredUplink': 'wan2', 'failOverCriterion': 'poorPerformance', 'performanceClass': {'type': 'custom', 'customPerformanceClassId': '123456'}}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/9'}}], 'preferredUplink': 'defaultUplink'}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/106'}}], 'preferredUplink': 'bestForVoIP'}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/107'}}], 'preferredUplink': 'loadBalancing', 'performanceClass': {'type': 'builtin', 'builtinPerformanceClassName': 'VoIP'}}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/162'}}], 'preferredUplink': 'loadBalancing', 'performanceClass': {'type': 'custom', 'customPerformanceClassId': '123456'}}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/168'}}], 'preferredUplink': 'wan2', 'failOverCriterion': 'poorPerformance', 'performanceClass': {'type': 'builtin', 'builtinPerformanceClassName': 'VoIP'}}, {'trafficFilters': [{'type': 'application', 'value': {'id': 'meraki:layer7/application/171'}}], 'preferredUplink': 'wan2', 'failOverCriterion': 'poorPerformance', 'performanceClass': {'type': 'custom', 'customPerformanceClassId': '123456'}}]
)

print(response)