import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.cellularGateway.updateNetworkCellularGatewayDhcp(
    network_id, 
    dhcpLeaseTime='1 hour', 
    dnsNameservers='custom', 
    dnsCustomNameservers=['172.16.2.111', '172.16.2.30']
)

print(response)