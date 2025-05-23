import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.sm.rebootNetworkSmDevices(
    network_id, 
    wifiMacs=['00:11:22:33:44:55'], 
    ids=['1284392014819', '2983092129865'], 
    serials=['XY0XX0Y0X0', 'A01B01CD00E', 'X02YZ1ZYZX'], 
    scope=['withAny', 'tag1', 'tag2'], 
    kextPaths=['test'], 
    notifyUser=True, 
    rebuildKernelCache=True, 
    requestRequiresNetworkTether=True
)

print(response)