import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
items = [{'networkId': 'N_24329156', 'policies': [{'policyId': '1284392014819', 'smNetworkId': 'N_24329156', 'scope': 'withAny', 'tags': ['tag1', 'tag2'], 'groupPolicyId': '1284392014819'}]}]

response = dashboard.sm.updateOrganizationSmSentryPoliciesAssignments(
    organization_id, items
)

print(response)