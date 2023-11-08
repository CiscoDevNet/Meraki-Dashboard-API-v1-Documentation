import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.updateNetworkAlertsSettings(
    network_id, 
    defaultDestinations={'emails': ['miles@meraki.com'], 'allAdmins': True, 'snmp': True, 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=']}, 
    alerts=[{'type': 'gatewayDown', 'enabled': True, 'alertDestinations': {'emails': ['miles@meraki.com'], 'allAdmins': False, 'snmp': False, 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=']}, 'filters': {'timeout': 60}}]
)

print(response)