import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
schedule_id = ''
devices = [{'serial': 'Q234-ABCD-5678', 'switchports': '1, 2', 'interface': 'TenGigabitEthernet0/0/0'}]

response = dashboard.organizations.updateOrganizationDevicesPacketCaptureSchedule(
    organization_id, schedule_id, devices, 
    name='daily_capture_for_debugging', 
    notes='Debugging persistent issue on device', 
    duration=60, 
    filterExpression='(icmp)', 
    enabled=True, 
    schedule={'name': 'Daily at 1pm', 'startTs': '2021-01-01T13:00:00Z', 'endTs': '2021-01-01T14:00:00Z', 'frequency': 'daily', 'weekdays': ['Monday', 'Wednesday', 'Friday'], 'recurrence': 1}
)

print(response)