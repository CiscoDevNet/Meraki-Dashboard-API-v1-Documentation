import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'
link_aggregation_id = ''

response = dashboard.switch.updateNetworkSwitchLinkAggregation(
    network_id, link_aggregation_id, 
    switchPorts=[{'serial': 'Q234-ABCD-0001', 'portId': '1'}, {'serial': 'Q234-ABCD-0002', 'portId': '2'}, {'serial': 'Q234-ABCD-0003', 'portId': '3'}, {'serial': 'Q234-ABCD-0004', 'portId': '4'}, {'serial': 'Q234-ABCD-0005', 'portId': '5'}, {'serial': 'Q234-ABCD-0006', 'portId': '6'}, {'serial': 'Q234-ABCD-0007', 'portId': '7'}, {'serial': 'Q234-ABCD-0008', 'portId': '8'}]
)

print(response)