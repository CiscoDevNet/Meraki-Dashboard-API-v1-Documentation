import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'wireless profile A'
ssid = {'name': 'ssid test', 'authMode': '8021x-radius', 'encryptionMode': 'wpa-eap', 'psk': 'sampleKey'}

response = dashboard.camera.createNetworkCameraWirelessProfile(
    network_id, name, ssid, 
    identity={'username': 'identityname', 'password': 'password123'}
)

print(response)