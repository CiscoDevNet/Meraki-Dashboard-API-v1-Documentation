import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'Weekdays schedule'

response = dashboard.switch.createNetworkSwitchPortSchedule(
    network_id, name, 
    portSchedule={'monday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'tuesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'wednesday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'thursday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'friday': {'active': True, 'from': '9:00', 'to': '17:00'}, 'saturday': {'active': False, 'from': '0:00', 'to': '24:00'}, 'sunday': {'active': False, 'from': '0:00', 'to': '24:00'}}
)

print(response)