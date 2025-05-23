import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
stages = [{'group': {'id': '1234'}, 'milestones': {'scheduledFor': '2018-02-11T00:00:00Z'}}]

response = dashboard.networks.rollbacksNetworkFirmwareUpgradesStagedEvents(
    network_id, stages, 
    reasons=[{'category': 'performance', 'comment': 'Network was slower with the upgrade'}]
)

print(response)