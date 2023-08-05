import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.appliance.updateNetworkApplianceSsid(
    network_id, number, 
    name='My SSID', 
    enabled=True, 
    defaultVlanId=1, 
    authMode='8021x-radius', 
    psk='psk', 
    radiusServers=[{'host': '0.0.0.0', 'port': 1000, 'secret': 'secret'}], 
    encryptionMode='wpa', 
    wpaEncryptionMode='WPA2 only', 
    visible=True, 
    dhcpEnforcedDeauthentication={'enabled': True}, 
    dot11w={'enabled': True, 'required': True}
)

print(response)