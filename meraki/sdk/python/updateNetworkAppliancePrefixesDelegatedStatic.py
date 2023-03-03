import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
static_delegated_prefix_id = ''

response = dashboard.appliance.updateNetworkAppliancePrefixesDelegatedStatic(
    network_id, static_delegated_prefix_id, 
    prefix='2001:db8:3c4d:15::/64', 
    origin={'type': 'internet', 'interfaces': ['wan1']}, 
    description='Prefix on WAN 1 of Long Island Office network'
)

print(response)