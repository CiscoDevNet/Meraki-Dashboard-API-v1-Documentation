import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
id_ = ''

response = dashboard.organizations.updateOrganizationAdaptivePolicyPolicy(
    organization_id, id_, 
    sourceGroup={'id': '222', 'name': 'IoT Devices', 'sgt': 50}, 
    destinationGroup={'id': '333', 'name': 'IoT Servers', 'sgt': 51}, 
    acls=[{'id': '444', 'name': 'Block web'}], 
    lastEntryRule='allow'
)

print(response)