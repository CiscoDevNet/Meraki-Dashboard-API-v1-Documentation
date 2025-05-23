import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
id_ = ''

response = dashboard.organizations.updateOrganizationAdaptivePolicyGroup(
    organization_id, id_, 
    name='Employee Group', 
    sgt=1000, 
    description='Group of XYZ Corp Employees', 
    policyObjects=[{'id': '2345', 'name': 'Example Policy Object'}]
)

print(response)