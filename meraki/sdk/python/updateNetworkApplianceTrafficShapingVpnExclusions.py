import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceTrafficShapingVpnExclusions(
    network_id, 
    custom=[{'protocol': 'tcp', 'destination': '192.168.3.0/24', 'port': '8000'}], 
    majorApplications=[{'id': 'meraki:vpnExclusion/application/2', 'name': 'Office 365 Sharepoint'}]
)

print(response)