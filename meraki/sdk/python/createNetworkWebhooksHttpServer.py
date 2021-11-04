import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'Example Webhook Server'
url = 'https://example.com'

response = dashboard.networks.createNetworkWebhooksHttpServer(
    network_id, name, url, 
    sharedSecret='shhh', 
    payloadTemplate={'payloadTemplateId': 'wpt_00001'}
)

print(response)