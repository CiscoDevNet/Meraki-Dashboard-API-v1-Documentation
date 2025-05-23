import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
type = 'allow'
match = {'type': 'bssid', 'string': '00:11:22:33:44:55'}

response = dashboard.wireless.createNetworkWirelessAirMarshalRule(
    network_id, type, match
)

print(response)