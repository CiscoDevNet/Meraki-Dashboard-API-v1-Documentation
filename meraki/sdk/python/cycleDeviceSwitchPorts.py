import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
ports = ['1', '2-5', '1_MA-MOD-8X10G_1', '1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8']

response = dashboard.switch.cycleDeviceSwitchPorts(
    serial, ports
)

print(response)