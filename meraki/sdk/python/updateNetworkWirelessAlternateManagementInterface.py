import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.wireless.updateNetworkWirelessAlternateManagementInterface(
    network_id, 
    enabled=True, 
    vlanId=100, 
    protocols=['radius', 'snmp', 'syslog', 'ldap'], 
    accessPoints=[{'serial': 'Q234-ABCD-5678', 'alternateManagementIp': '1.2.3.4', 'subnetMask': '255.255.255.0', 'gateway': '1.2.3.5', 'dns1': '8.8.8.8', 'dns2': '8.8.4.4'}]
)

print(response)