import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
email = 'miles@meraki.com'
name = 'Miles Meraki'
org_access = 'none'

response = dashboard.organizations.createOrganizationAdmin(
    organization_id, email, name, org_access, 
    tags=[{'tag': 'west', 'access': 'read-only'}], 
    networks=[{'id': 'N_24329156', 'access': 'full'}], 
    authenticationMethod='Email'
)

print(response)