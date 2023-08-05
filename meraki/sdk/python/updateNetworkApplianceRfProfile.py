import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

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