import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''
identity_psk_id = ''

response = dashboard.wireless.updateNetworkWirelessSsidIdentityPsk(
    network_id, number, identity_psk_id, 
    name='Sample Identity PSK', 
    passphrase='secret', 
    groupPolicyId='101', 
    expiresAt='2018-02-11T00:00:00.090210Z'
)

print(response)