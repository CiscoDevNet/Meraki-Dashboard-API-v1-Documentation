import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
admin_id = ''

response = dashboard.organizations.updateOrganizationAdmin(
    organization_id, admin_id, 
    name='Miles Meraki', 
    orgAccess='none', 
    tags=[{'tag': 'west', 'access': 'read-only'}], 
    networks=[{'id': 'N_24329156', 'access': 'full'}]
)

print(response)