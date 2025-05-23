import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.switch.updateNetworkSwitchAlternateManagementInterface(
    network_id, 
    enabled=True, 
    vlanId=100, 
    protocols=['radius', 'snmp', 'syslog'], 
    switches=[{'serial': 'Q234-ABCD-5678', 'alternateManagementIp': '1.2.3.4', 'subnetMask': '255.255.255.0', 'gateway': '1.2.3.5'}]
)

print(response)