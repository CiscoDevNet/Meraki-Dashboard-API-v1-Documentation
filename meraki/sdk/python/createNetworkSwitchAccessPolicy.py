import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'Access policy #1'
radius_servers = [{'organizationRadiusServerId': '42', 'host': '1.2.3.4', 'port': 22, 'secret': 'secret'}]
radius_testing_enabled = False
radius_coa_support_enabled = False
radius_accounting_enabled = True
host_mode = 'Single-Host'
url_redirect_walled_garden_enabled = True

response = dashboard.switch.createNetworkSwitchAccessPolicy(
    network_id, name, radius_servers, radius_testing_enabled, radius_coa_support_enabled, radius_accounting_enabled, host_mode, url_redirect_walled_garden_enabled, 
    radius={'criticalAuth': {'dataVlanId': 100, 'voiceVlanId': 100, 'suspendPortBounce': True}, 'failedAuthVlanId': 100, 'reAuthenticationInterval': 120, 'cache': {'enabled': False, 'timeout': 24}}, 
    guestPortBouncing=False, 
    radiusAccountingServers=[{'organizationRadiusServerId': '42', 'host': '1.2.3.4', 'port': 22, 'secret': 'secret'}], 
    radiusGroupAttribute='11', 
    accessPolicyType='Hybrid authentication', 
    increaseAccessSpeed=False, 
    guestVlanId=100, 
    dot1x={'controlDirection': 'inbound'}, 
    voiceVlanClients=True, 
    urlRedirectWalledGardenRanges=['192.168.1.0/24']
)

print(response)