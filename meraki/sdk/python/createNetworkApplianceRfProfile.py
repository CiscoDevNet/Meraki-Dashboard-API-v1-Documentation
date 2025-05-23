import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'MX RF Profile'

response = dashboard.appliance.createNetworkApplianceRfProfile(
    network_id, name, 
    twoFourGhzSettings={'minBitrate': 12.0, 'axEnabled': True}, 
    fiveGhzSettings={'minBitrate': 48, 'axEnabled': True}, 
    perSsidSettings={'1': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '2': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '3': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '4': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}}
)

print(response)