import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.updateNetworkAlertsSettings(
    network_id, 
    defaultDestinations={'emails': ['miles@meraki.com'], 'allAdmins': True, 'snmp': True, 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=']}, 
    alerts=[{'type': 'gatewayDown', 'enabled': True, 'alertDestinations': {'emails': ['miles@meraki.com'], 'smsNumbers': ['+15555555555'], 'allAdmins': False, 'snmp': False, 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=']}, 'filters': {'conditions': [{'type': 'temperature', 'unit': 'celsius', 'duration': 0, 'direction': '+', 'threshold': 72.5}], 'failureType': '802.1X auth fail', 'lookbackWindow': 360, 'minDuration': 60, 'name': 'Filter', 'period': 1800, 'priority': '', 'regex': '[a-z]', 'selector': '{"smartSensitivity":"medium","smartEnabled":false,"eventReminderPeriodSecs":10800}', 'serials': ['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 'ssidNum': 1, 'tag': 'tag1', 'threshold': 30, 'timeout': 60}}], 
    muting={'byPortSchedules': {'enabled': True}}
)

print(response)