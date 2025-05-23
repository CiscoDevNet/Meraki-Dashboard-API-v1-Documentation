import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
enabled = True

response = dashboard.appliance.updateNetworkApplianceWarmSpare(
    network_id, enabled, 
    spareSerial='Q234-ABCD-5678', 
    uplinkMode='virtual', 
    virtualIp1='1.2.3.4', 
    virtualIp2='1.2.3.4'
)

print(response)