import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
group_policy_id = ''

response = dashboard.networks.updateNetworkGroupPolicy(
    network_id, group_policy_id, 
    name='No video streaming', 
    scheduling={'enabled': True, 'monday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'tuesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'wednesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'thursday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'friday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'saturday': {'active': False, 'from': '0:00', 'to': '24:00'}, 'sunday': {'active': False, 'from': '0:00', 'to': '24:00'}}, 
    bandwidth={'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 
    firewallAndTrafficShaping={'settings': 'custom', 'trafficShapingRules': [{'definitions': [{'type': 'host', 'value': 'google.com'}, {'type': 'port', 'value': '9090'}, {'type': 'ipRange', 'value': '192.1.0.0'}, {'type': 'ipRange', 'value': '192.1.0.0/16'}, {'type': 'ipRange', 'value': '10.1.0.0/16:80'}, {'type': 'localNet', 'value': '192.168.0.0/16'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 0, 'pcpTagValue': 0}], 'l3FirewallRules': [{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24'}], 'l7FirewallRules': [{'policy': 'deny', 'type': 'host', 'value': 'google.com'}, {'policy': 'deny', 'type': 'port', 'value': '23'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24'}, {'policy': 'deny', 'type': 'ipRange', 'value': '10.11.12.00/24:5555'}]}, 
    contentFiltering={'allowedUrlPatterns': {'settings': 'network default', 'patterns': []}, 'blockedUrlPatterns': {'settings': 'append', 'patterns': ['http://www.example.com', 'http://www.betting.com']}, 'blockedUrlCategories': {'settings': 'override', 'categories': ['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7']}}, 
    splashAuthSettings='bypass', 
    vlanTagging={'settings': 'custom', 'vlanId': '1'}, 
    bonjourForwarding={'settings': 'custom', 'rules': [{'description': 'A simple bonjour rule', 'vlanId': '1', 'services': ['All Services']}]}
)

print(response)