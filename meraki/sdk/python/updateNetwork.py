import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.updateNetwork(
    network_id, 
    name='Main Office', 
    timeZone='America/Los_Angeles', 
    tags=['tag1', 'tag2'], 
    enrollmentString='my-enrollment-string', 
    notes='Additional description of the network'
)

print(response)