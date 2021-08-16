import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
access_policy_number = ''

response = dashboard.switch.updateNetworkSwitchAccessPolicy(
    network_id, access_policy_number, 
    name='Access policy #1', 
    radiusServers=[{'host': '1.2.3.4', 'port': 22, 'secret': 'password1'}], 
    radius={'criticalAuth': {'dataVlanId': 100, 'voiceVlanId': 100, 'suspendPortBounce': True}, 'failedAuthVlanId': 100, 'reAuthenticationInterval': 120, 'suspendReAuthentication': True}, 
    radiusTestingEnabled=False, 
    radiusCoaSupportEnabled=False, 
    radiusAccountingEnabled=True, 
    radiusAccountingServers=[{'host': '1.2.3.4', 'port': 22, 'secret': 'password1'}], 
    radiusGroupAttribute='11', 
    hostMode='Single-Host', 
    accessPolicyType='Hybrid authentication', 
    increaseAccessSpeed=False, 
    guestVlanId=100, 
    voiceVlanClients=True, 
    urlRedirectWalledGardenEnabled=True, 
    urlRedirectWalledGardenRanges='192.168.1.0/24'
)

print(response)