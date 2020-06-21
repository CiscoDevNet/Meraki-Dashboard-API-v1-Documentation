import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
subnet = '192.168.1.0/24'
next_hop_ip = '1.2.3.4'

response = dashboard.switch.createDeviceSwitchRoutingStaticRoute(
    serial, subnet, next_hop_ip, 
    name='My route', 
    advertiseViaOspfEnabled=False, 
    preferOverOspfRoutesEnabled=False
)

print(response)