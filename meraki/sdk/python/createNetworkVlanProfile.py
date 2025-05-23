import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'My VLAN profile name'
vlan_names = [{'name': 'named-1', 'vlanId': '1', 'adaptivePolicyGroup': {'id': '791'}}]
vlan_groups = [{'name': 'named-group-1', 'vlanIds': '2,5-7'}]
iname = 'Profile1'

response = dashboard.networks.createNetworkVlanProfile(
    network_id, name, vlan_names, vlan_groups, iname
)

print(response)