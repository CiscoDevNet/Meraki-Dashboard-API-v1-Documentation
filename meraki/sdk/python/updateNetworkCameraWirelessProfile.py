import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
wireless_profile_id = ''

response = dashboard.camera.updateNetworkCameraWirelessProfile(
    network_id, wireless_profile_id, 
    name='wireless profile A', 
    ssid={'name': 'ssid test', 'authMode': '8021x-radius', 'encryptionMode': 'wpa-eap', 'psk': 'sampleKey'}, 
    identity={'username': 'identityname', 'password': 'password123'}
)

print(response)