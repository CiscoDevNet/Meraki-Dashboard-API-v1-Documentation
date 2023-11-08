import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
prefix = '2001:db8:3c4d:15::/64'
origin = {'type': 'internet', 'interfaces': ['wan1']}

response = dashboard.appliance.createNetworkAppliancePrefixesDelegatedStatic(
    network_id, prefix, origin, 
    description='Prefix on WAN 1 of Long Island Office network'
)

print(response)