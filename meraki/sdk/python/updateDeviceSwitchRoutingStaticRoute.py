import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
static_route_id = ''

response = dashboard.switch.updateDeviceSwitchRoutingStaticRoute(
    serial, static_route_id, 
    name='My route', 
    subnet='192.168.1.0/24', 
    nextHopIp='1.2.3.4', 
    managementNextHop='1.2.3.5', 
    advertiseViaOspfEnabled=False, 
    preferOverOspfRoutesEnabled=False
)

print(response)