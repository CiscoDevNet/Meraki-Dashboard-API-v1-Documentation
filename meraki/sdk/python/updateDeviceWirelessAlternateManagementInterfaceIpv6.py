import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.wireless.updateDeviceWirelessAlternateManagementInterfaceIpv6(
    serial, 
    addresses=[{'protocol': 'ipv6', 'assignmentMode': 'static', 'address': '2001:db8:3c4d:15::1', 'gateway': 'fe80:db8:c15:c0:d0c::10ca:1d02', 'prefix': '2001:db8:3c4d:15::/64', 'nameservers': {'addresses': ['2001:db8:3c4d:15::1', '2001:db8:3c4d:15::1']}}]
)

print(response)