import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.wireless.updateNetworkWirelessSettings(
    network_id, 
    meshingEnabled=True, 
    ipv6BridgeEnabled=False, 
    locationAnalyticsEnabled=False, 
    upgradeStrategy='minimizeUpgradeTime', 
    ledLightsOn=False, 
    namedVlans={'poolDhcpMonitoring': {'enabled': True, 'duration': 5}}
)

print(response)