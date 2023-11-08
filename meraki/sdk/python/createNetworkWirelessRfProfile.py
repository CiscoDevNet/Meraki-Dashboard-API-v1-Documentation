import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'Main Office'
band_selection_type = 'ap'

response = dashboard.wireless.createNetworkWirelessRfProfile(
    network_id, name, band_selection_type, 
    clientBalancingEnabled=True, 
    minBitrateType='band', 
    apBandSettings={'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, 
    twoFourGhzSettings={'maxPower': 30, 'minPower': 5, 'minBitrate': 11.0, 'validAutoChannels': [1, 6, 11], 'axEnabled': True, 'rxsop': -95}, 
    fiveGhzSettings={'maxPower': 30, 'minPower': 8, 'minBitrate': 12, 'validAutoChannels': [36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 149, 153, 157, 161, 165], 'channelWidth': 'auto', 'rxsop': -95}, 
    sixGhzSettings={'maxPower': 30, 'minPower': 8, 'minBitrate': 12, 'validAutoChannels': [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121, 125, 129, 133, 137, 141, 145, 149, 153, 157, 161, 165, 169, 173, 177, 181, 185, 189, 193, 197, 201, 205, 209, 213, 217, 221, 225, 229, 233], 'channelWidth': 'auto', 'rxsop': -95}, 
    transmission={'enabled': True}, 
    perSsidSettings={'0': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '1': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '2': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '3': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '4': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '5': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '6': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '7': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '8': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '9': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '10': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '11': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '12': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '13': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}, '14': {'minBitrate': 11.0, 'bandOperationMode': 'dual', 'bands': {'enabled': ['2.4', '5']}, 'bandSteeringEnabled': True}}, 
    flexRadios={'byModel': [{'model': 'MR34', 'bands': ['5']}]}
)

print(response)