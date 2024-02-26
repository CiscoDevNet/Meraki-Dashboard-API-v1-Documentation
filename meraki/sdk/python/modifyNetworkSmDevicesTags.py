import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
tags = ['tag1', 'tag2']
update_action = 'add'

response = dashboard.sm.modifyNetworkSmDevicesTags(
    network_id, tags, update_action, 
    wifiMacs=['00:11:22:33:44:55'], 
    ids=['1284392014819', '2983092129865'], 
    serials=['XY0XX0Y0X0', 'A01B01CD00E', 'X02YZ1ZYZX'], 
    scope=['withAny, old_tag']
)

print(response)