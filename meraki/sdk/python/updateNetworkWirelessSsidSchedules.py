import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidSchedules(
    network_id, number, 
    enabled=True, 
    ranges=[{'startDay': 'Tuesday', 'startTime': '01:00', 'endDay': 'Tuesday', 'endTime': '05:00'}, {'startDay': 'Fri', 'startTime': '19:00', 'endDay': 'monday', 'endTime': '05:00'}]
)

print(response)