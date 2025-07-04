import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
name = 'Main Office'
product_types = ['appliance', 'switch', 'wireless']

response = dashboard.organizations.createOrganizationNetwork(
    organization_id, name, product_types, 
    tags=['tag1', 'tag2'], 
    timeZone='America/Los_Angeles', 
    copyFromNetworkId='N_24329156', 
    notes='Additional description of the network'
)

print(response)