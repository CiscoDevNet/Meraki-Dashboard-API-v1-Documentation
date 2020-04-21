import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
ports = ['1', '2-5', '1_MA-MOD-8X10G_1', '1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8']

response = dashboard.switch.cycleDeviceSwitchPorts(
    serial, ports
)

print(response)