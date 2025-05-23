import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.wireless.updateNetworkWirelessBluetoothSettings(
    network_id, 
    scanningEnabled=True, 
    advertisingEnabled=True, 
    uuid='00000000-0000-0000-000-000000000000', 
    majorMinorAssignmentMode='Non-unique', 
    major=1, 
    minor=1
)

print(response)