import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''
name = 'Sample Identity PSK'
group_policy_id = '101'

response = dashboard.wireless.createNetworkWirelessSsidIdentityPsk(
    network_id, number, name, group_policy_id, 
    passphrase='secret', 
    expiresAt='2018-02-11T00:00:00.090210Z'
)

print(response)