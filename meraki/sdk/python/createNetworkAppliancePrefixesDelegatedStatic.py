import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
prefix = '2001:db8:3c4d:15::/64'
origin = {'type': 'internet', 'interfaces': ['wan1']}

response = dashboard.appliance.createNetworkAppliancePrefixesDelegatedStatic(
    network_id, prefix, origin, 
    description='Prefix on WAN 1 of Long Island Office network'
)

print(response)