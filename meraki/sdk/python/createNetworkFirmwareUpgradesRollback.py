import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
reasons = [{'category': 'performance', 'comment': 'Network was slower with the upgrade'}, {'category': 'stability', 'comment': "We saw some errors in the logs we didn't expect"}]

response = dashboard.networks.createNetworkFirmwareUpgradesRollback(
    network_id, reasons, 
    product='switch', 
    time='2020-10-21T02:00:00Z', 
    toVersion={'id': '7857'}
)

print(response)