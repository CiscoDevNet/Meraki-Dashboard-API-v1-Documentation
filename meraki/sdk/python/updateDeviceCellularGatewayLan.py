import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.cellular_gateway.updateDeviceCellularGatewayLan(
    serial, 
    reservedIpRanges=[{'start': '192.168.1.0', 'end': '192.168.1.1', 'comment': 'A reserved IP range'}], 
    fixedIpAssignments=[{'mac': '0b:00:00:00:00:ac', 'name': 'server 1', 'ip': '192.168.0.10'}, {'mac': '0b:00:00:00:00:ab', 'name': 'server 2', 'ip': '192.168.0.20'}]
)

print(response)