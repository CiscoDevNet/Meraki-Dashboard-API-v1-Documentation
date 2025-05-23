import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
cluster_id = ''

response = dashboard.campusGateway.updateNetworkCampusGatewayCluster(
    network_id, cluster_id, 
    name='North Campus', 
    uplinks=[{'interface': 'man1', 'vlan': 5, 'addresses': [{'assignmentMode': 'static', 'protocol': 'ipv4', 'gateway': '1.2.3.5', 'subnetMask': '255.255.255.0'}]}], 
    tunnels=[{'uplink': {'interface': 'man1'}, 'interface': 'tun1', 'vlan': 6, 'addresses': [{'protocol': 'ipv4', 'gateway': '2.3.5.6', 'subnetMask': '255.255.255.0'}]}], 
    nameservers={'addresses': ['8.8.8.8', '8.8.4.4']}, 
    portChannels=[{'name': 'Port-channel1', 'vlan': 25, 'allowedVlans': '10-20'}], 
    devices=[{'serial': 'Q234-ABCD-0001', 'uplinks': [{'interface': 'man1', 'addresses': [{'protocol': 'ipv4', 'address': '5.1.2.3'}]}], 'tunnels': [{'interface': 'tun1', 'addresses': [{'protocol': 'ipv4', 'address': '6.2.6.7'}]}]}], 
    notes='This cluster is for New York Office'
)

print(response)