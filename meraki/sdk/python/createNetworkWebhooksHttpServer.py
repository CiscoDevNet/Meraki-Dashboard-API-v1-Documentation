import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'Example Webhook Server'
url = 'https://example.com'

response = dashboard.networks.createNetworkWebhooksHttpServer(
    network_id, name, url, 
    sharedSecret='shhh', 
    payloadTemplate={'payloadTemplateId': 'wpt_00001', 'name': 'Meraki (included)'}
)

print(response)