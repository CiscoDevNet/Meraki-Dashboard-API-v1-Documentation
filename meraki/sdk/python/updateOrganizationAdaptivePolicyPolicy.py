import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
adaptive_policy_id = ''

response = dashboard.organizations.updateOrganizationAdaptivePolicyPolicy(
    organization_id, adaptive_policy_id, 
    sourceGroup={'id': '222', 'name': 'IoT Devices', 'sgt': 50}, 
    destinationGroup={'id': '333', 'name': 'IoT Servers', 'sgt': 51}, 
    acls=[{'id': '444', 'name': 'Block web'}], 
    lastEntryRule='allow'
)

print(response)