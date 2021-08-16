import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidHotspot20(
    network_id, number, 
    enabled=True, 
    operator={'name': 'Meraki Product Management'}, 
    venue={'name': 'SF Branch', 'type': 'Unspecified Assembly'}, 
    networkAccessType='Private network', 
    domains=['meraki.local', 'domain2.com'], 
    roamConsortOis=['ABC123', '456EFG'], 
    mccMncs=[{'mcc': '123', 'mnc': '456'}, {'mcc': '563', 'mnc': '232'}], 
    naiRealms=[{'format': 1, 'name': 'Realm 1', 'methods': [{'id': '1', 'authenticationTypes': {'nonEapInnerAuthentication': ['MSCHAP'], 'eapInnerAuthentication': ['EAP-TTLS with MSCHAPv2'], 'credentials': [], 'tunneledEapMethodCredentials': []}}]}]
)

print(response)