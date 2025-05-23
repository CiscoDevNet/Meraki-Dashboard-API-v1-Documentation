import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
role_id = ''

response = dashboard.camera.updateOrganizationCameraRole(
    organization_id, role_id, 
    name='Security_Guard', 
    appliedOnDevices=[{'tag': 'reception-desk', 'id': '', 'permissionScopeId': '1'}], 
    appliedOnNetworks=[{'tag': 'building-a', 'id': '', 'permissionScopeId': '2'}], 
    appliedOrgWide=[{'tag': 'building-a', 'id': '', 'permissionScopeId': '2'}]
)

print(response)