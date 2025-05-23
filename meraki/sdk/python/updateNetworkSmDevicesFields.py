import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
device_fields = {'name': "Miles's phone", 'notes': "Here's some info about my device"}

response = dashboard.sm.updateNetworkSmDevicesFields(
    network_id, device_fields, 
    wifiMac='00:11:22:33:44:55', 
    id='1284392014819', 
    serial='XY0XX0Y0X0'
)

print(response)