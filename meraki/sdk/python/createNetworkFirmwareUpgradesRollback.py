import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
reasons = [{'category': 'performance', 'comment': 'Network was slower with the upgrade'}]

response = dashboard.networks.createNetworkFirmwareUpgradesRollback(
    network_id, reasons, 
    product='switch', 
    time='2020-10-21T02:00:00Z', 
    toVersion={'id': '7857'}
)

print(response)