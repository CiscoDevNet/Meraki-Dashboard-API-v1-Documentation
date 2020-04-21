import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
qos_rule_id = ''

response = dashboard.switch.updateNetworkSwitchQosRule(
    network_id, qos_rule_id, 
    vlan=100, 
    protocol='TCP', 
    srcPort=2000, 
    srcPortRange=None, 
    dstPort=None, 
    dstPortRange='3000-3100', 
    dscp=0
)

print(response)