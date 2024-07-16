import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
access_policy_number = ''

response = dashboard.switch.updateNetworkSwitchAccessPolicy(
    network_id, access_policy_number, 
    name='Access policy #1', 
    radiusServers=[{'serverId': '1', 'organizationRadiusServerId': '42', 'host': '1.2.3.4', 'port': 22, 'secret': 'secret'}], 
    radius={'criticalAuth': {'dataVlanId': 100, 'voiceVlanId': 100, 'suspendPortBounce': True}, 'failedAuthVlanId': 100, 'reAuthenticationInterval': 120, 'cache': {'enabled': False, 'timeout': 24}}, 
    guestPortBouncing=False, 
    radiusTestingEnabled=False, 
    radiusCoaSupportEnabled=False, 
    radiusAccountingEnabled=True, 
    radiusAccountingServers=[{'serverId': '2', 'organizationRadiusServerId': '42', 'host': '1.2.3.4', 'port': 22, 'secret': 'secret'}], 
    radiusGroupAttribute='11', 
    hostMode='Single-Host', 
    accessPolicyType='Hybrid authentication', 
    increaseAccessSpeed=False, 
    guestVlanId=100, 
    dot1x={'controlDirection': 'inbound'}, 
    voiceVlanClients=True, 
    urlRedirectWalledGardenEnabled=True, 
    urlRedirectWalledGardenRanges=['192.168.1.0/24']
)

print(response)