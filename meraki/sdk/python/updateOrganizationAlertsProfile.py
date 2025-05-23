import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
alert_config_id = ''

response = dashboard.organizations.updateOrganizationAlertsProfile(
    organization_id, alert_config_id, 
    enabled=True, 
    type='wanUtilization', 
    alertCondition={'duration': 60, 'window': 600, 'bit_rate_bps': 10000, 'loss_ratio': 0.1, 'latency_ms': 100, 'jitter_ms': 100, 'mos': 3.5, 'interface': 'wan1'}, 
    recipients={'emails': ['admin@example.org'], 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vcGF0aA==']}, 
    networkTags=['tag1', 'tag2'], 
    description='WAN 1 high utilization'
)

print(response)