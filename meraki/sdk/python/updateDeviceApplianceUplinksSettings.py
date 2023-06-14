import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'
interfaces = {'wan1': {'enabled': True, 'vlanTagging': {'enabled': True, 'vlanId': 1}, 'svis': {'ipv4': {'assignmentMode': 'static', 'address': '9.10.11.10/16', 'gateway': '13.14.15.16', 'nameservers': {'addresses': ['1.2.3.4']}}, 'ipv6': {'assignmentMode': 'static', 'address': '1:2:3::4', 'gateway': '1:2:3::5', 'nameservers': {'addresses': ['1001:4860:4860::8888', '1001:4860:4860::8844']}}}, 'pppoe': {'enabled': True, 'authentication': {'enabled': True, 'username': 'username', 'password': 'password'}}}, 'wan2': {'enabled': True, 'vlanTagging': {'enabled': True, 'vlanId': 1}, 'svis': {'ipv4': {'assignmentMode': 'static', 'address': '9.10.11.10/16', 'gateway': '13.14.15.16', 'nameservers': {'addresses': ['1.2.3.4']}}, 'ipv6': {'assignmentMode': 'static', 'address': '1:2:3::4', 'gateway': '1:2:3::5', 'nameservers': {'addresses': ['1001:4860:4860::8888', '1001:4860:4860::8844']}}}, 'pppoe': {'enabled': True, 'authentication': {'enabled': True, 'username': 'username', 'password': 'password'}}}}

response = dashboard.appliance.updateDeviceApplianceUplinksSettings(
    serial, interfaces
)

print(response)