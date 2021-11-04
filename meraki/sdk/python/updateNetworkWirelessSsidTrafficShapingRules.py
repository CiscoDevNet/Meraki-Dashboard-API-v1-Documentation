import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidTrafficShapingRules(
    network_id, number, 
    trafficShapingEnabled=True, 
    defaultRulesEnabled=True, 
    rules=[{'definitions': [{'type': 'host', 'value': 'google.com'}, {'type': 'port', 'value': '9090'}, {'type': 'ipRange', 'value': '192.1.0.0'}, {'type': 'ipRange', 'value': '192.1.0.0/16'}, {'type': 'ipRange', 'value': '10.1.0.0/16:80'}, {'type': 'localNet', 'value': '192.168.0.0/16'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 0, 'pcpTagValue': 0}]
)

print(response)