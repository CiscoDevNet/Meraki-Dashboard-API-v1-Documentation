import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.createNetworkSwitchLinkAggregation(
    network_id, 
    switchPorts=[{'serial': 'Q234-ABCD-0001', 'portId': '1'}, {'serial': 'Q234-ABCD-0002', 'portId': '2'}, {'serial': 'Q234-ABCD-0003', 'portId': '3'}, {'serial': 'Q234-ABCD-0004', 'portId': '4'}, {'serial': 'Q234-ABCD-0005', 'portId': '5'}, {'serial': 'Q234-ABCD-0006', 'portId': '6'}, {'serial': 'Q234-ABCD-0007', 'portId': '7'}, {'serial': 'Q234-ABCD-0008', 'portId': '8'}]
)

print(response)