import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
interfaces = {'wan1': {'enabled': True, 'vlanTagging': {'enabled': True, 'vlanId': 1}, 'svis': {'ipv4': {'assignmentMode': 'static', 'address': '9.10.11.10/16', 'gateway': '13.14.15.16', 'nameservers': {'addresses': ['1.2.3.4']}}, 'ipv6': {'assignmentMode': 'static', 'address': '1:2:3::4', 'gateway': '1:2:3::5', 'nameservers': {'addresses': ['1001:4860:4860::8888', '1001:4860:4860::8844']}}}, 'pppoe': {'enabled': True, 'authentication': {'enabled': True, 'username': 'username', 'password': 'password'}}}, 'wan2': {'enabled': True, 'vlanTagging': {'enabled': True, 'vlanId': 1}, 'svis': {'ipv4': {'assignmentMode': 'static', 'address': '9.10.11.10/16', 'gateway': '13.14.15.16', 'nameservers': {'addresses': ['1.2.3.4']}}, 'ipv6': {'assignmentMode': 'static', 'address': '1:2:3::4', 'gateway': '1:2:3::5', 'nameservers': {'addresses': ['1001:4860:4860::8888', '1001:4860:4860::8844']}}}, 'pppoe': {'enabled': True, 'authentication': {'enabled': True, 'username': 'username', 'password': 'password'}}}}

response = dashboard.appliance.updateDeviceApplianceUplinksSettings(
    serial, interfaces
)

print(response)