import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'No video streaming'

response = dashboard.networks.createNetworkGroupPolicy(
    network_id, name, 
    scheduling={'enabled': True, 'monday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'tuesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'wednesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'thursday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'friday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'saturday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'sunday': {'active': True, 'from': '9:00', 'to': '17:00'}}, 
    bandwidth={'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 
    firewallAndTrafficShaping={'settings': 'custom', 'trafficShapingRules': [{'definitions': [{'type': 'host', 'value': 'google.com'}], 'perClientBandwidthLimits': {'settings': 'custom', 'bandwidthLimits': {'limitUp': 1000000, 'limitDown': 1000000}}, 'dscpTagValue': 0, 'pcpTagValue': 0, 'priority': 'normal'}], 'l3FirewallRules': [{'comment': 'Allow TCP traffic to subnet with HTTP servers.', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '192.168.1.0/24'}], 'l7FirewallRules': [{'policy': 'deny', 'type': 'host', 'value': 'google.com'}]}, 
    contentFiltering={'allowedUrlPatterns': {'settings': 'network default', 'patterns': []}, 'blockedUrlPatterns': {'settings': 'append', 'patterns': ['http://www.example.com', 'http://www.betting.com']}, 'blockedUrlCategories': {'settings': 'override', 'categories': ['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7']}}, 
    splashAuthSettings='bypass', 
    vlanTagging={'settings': 'custom', 'vlanId': '1'}, 
    bonjourForwarding={'settings': 'custom', 'rules': [{'description': 'A simple bonjour rule', 'vlanId': '1', 'services': ['All Services']}]}
)

print(response)