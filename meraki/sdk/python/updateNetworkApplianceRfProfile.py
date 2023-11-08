import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rf_profile_id = ''

response = dashboard.appliance.updateNetworkApplianceRfProfile(
    network_id, rf_profile_id, 
    name='MX RF Profile', 
    twoFourGhzSettings={'minBitrate': 12.0, 'axEnabled': True}, 
    fiveGhzSettings={'minBitrate': 48, 'axEnabled': True}, 
    perSsidSettings={'1': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '2': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '3': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '4': {'bandOperationMode': 'dual', 'bandSteeringEnabled': True}}
)

print(response)