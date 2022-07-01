import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
new_network = '1284392014819'

response = dashboard.sm.moveNetworkSmDevices(
    network_id, new_network, 
    wifiMacs=['00:11:22:33:44:55'], 
    ids=['1284392014819', '2983092129865'], 
    serials=['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 
    scope=['withAny', 'tag1', 'tag2']
)

print(response)