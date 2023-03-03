import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
rf_profile_id = ''

response = dashboard.wireless.updateNetworkWirelessRfProfile(
    network_id, rf_profile_id, 
    name='1234', 
    clientBalancingEnabled=True, 
    minBitrateType='band', 
    bandSelectionType='ap', 
    apBandSettings={'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, 
    twoFourGhzSettings={'maxPower': 30, 'minPower': 5, 'minBitrate': 11.0, 'validAutoChannels': [1, 6, 11], 'axEnabled': True, 'rxsop': -95}, 
    fiveGhzSettings={'maxPower': 30, 'minPower': 8, 'minBitrate': 12, 'validAutoChannels': [36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 149, 153, 157, 161, 165], 'channelWidth': 'auto', 'rxsop': -95}, 
    transmission={'enabled': True}, 
    perSsidSettings={'0': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '1': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '2': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '3': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '4': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '5': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '6': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '7': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '8': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '9': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '10': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '11': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '12': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '13': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}, '14': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bandSteeringEnabled': True}}
)

print(response)