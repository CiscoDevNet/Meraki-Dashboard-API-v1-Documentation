import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
type = 'wanUtilization'
alert_condition = {'duration': 60, 'window': 600, 'bit_rate_bps': 10000, 'interface': 'wan1'}
recipients = {'emails': ['admin@example.org'], 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vcGF0aA==']}
network_tags = ['tag1', 'tag2']

response = dashboard.organizations.createOrganizationAlertsProfile(
    organization_id, type, alert_condition, recipients, network_tags, 
    description='WAN 1 high utilization'
)

print(response)