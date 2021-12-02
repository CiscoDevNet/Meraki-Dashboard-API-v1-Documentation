import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.wireless.updateNetworkWirelessBilling(
    network_id, 
    currency='USD', 
    plans=[{'id': '1', 'price': 5, 'bandwidthLimits': {'limitUp': 1000, 'limitDown': 1000}, 'timeLimit': '1 hour'}]
)

print(response)