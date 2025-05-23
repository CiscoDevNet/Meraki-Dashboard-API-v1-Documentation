import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
qos_rule_id = ''

response = dashboard.switch.updateNetworkSwitchQosRule(
    network_id, qos_rule_id, 
    vlan=100, 
    protocol='TCP', 
    srcPort=2000, 
    srcPortRange='70-80', 
    dstPort=3000, 
    dstPortRange='3000-3100', 
    dscp=0
)

print(response)