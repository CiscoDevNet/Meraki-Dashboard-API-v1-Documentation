import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchRoutingOspf(
    network_id, 
    enabled=True, 
    helloTimerInSeconds=10, 
    deadTimerInSeconds=40, 
    areas=[{'areaId': '1284392014819', 'areaName': 'Backbone', 'areaType': 'normal'}], 
    v3={'enabled': True, 'helloTimerInSeconds': 10, 'deadTimerInSeconds': 40, 'areas': [{'areaId': '1284392014819', 'areaName': 'V3 Backbone', 'areaType': 'normal'}]}, 
    md5AuthenticationEnabled=True, 
    md5AuthenticationKey={'id': 1234, 'passphrase': 'abc1234'}
)

print(response)