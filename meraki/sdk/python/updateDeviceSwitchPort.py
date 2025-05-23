import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
port_id = ''

response = dashboard.switch.updateDeviceSwitchPort(
    serial, port_id, 
    name='My switch port', 
    tags=['tag1', 'tag2'], 
    enabled=True, 
    poeEnabled=True, 
    type='access', 
    vlan=10, 
    voiceVlan=20, 
    allowedVlans='1,3,5-10', 
    isolationEnabled=False, 
    rstpEnabled=True, 
    stpGuard='disabled', 
    linkNegotiation='Auto negotiate', 
    portScheduleId='1234', 
    udld='Alert only', 
    accessPolicyType='Sticky MAC allow list', 
    accessPolicyNumber=2, 
    macAllowList=['34:56:fe:ce:8e:a0', '34:56:fe:ce:8e:a1'], 
    macWhitelistLimit=10, 
    stickyMacAllowList=['34:56:fe:ce:8e:b0', '34:56:fe:ce:8e:b1'], 
    stickyMacAllowListLimit=5, 
    stormControlEnabled=True, 
    adaptivePolicyGroupId='123', 
    peerSgtCapable=False, 
    flexibleStackingEnabled=True, 
    daiTrusted=False, 
    profile={'enabled': False, 'id': '1284392014819', 'iname': 'iname'}, 
    dot3az={'enabled': False}
)

print(response)