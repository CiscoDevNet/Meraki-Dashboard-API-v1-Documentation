import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
type = 'wanUtilization'
alert_condition = {'duration': 60, 'window': 600, 'bit_rate_bps': 10000, 'loss_ratio': 0.1, 'latency_ms': 100, 'jitter_ms': 100, 'mos': 3.5, 'interface': 'wan1'}
recipients = {'emails': ['admin@example.org'], 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vcGF0aA==']}
network_tags = ['tag1', 'tag2']

response = dashboard.organizations.createOrganizationAlertsProfile(
    organization_id, type, alert_condition, recipients, network_tags, 
    description='WAN 1 high utilization'
)

print(response)