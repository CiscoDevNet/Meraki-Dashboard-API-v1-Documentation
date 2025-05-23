import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
url = 'https://www.example.com/path'

response = dashboard.networks.createNetworkWebhooksWebhookTest(
    network_id, url, 
    sharedSecret='shhh', 
    payloadTemplateId='wpt_00001', 
    payloadTemplateName='Payload Template', 
    alertTypeId='power_supply_down'
)

print(response)