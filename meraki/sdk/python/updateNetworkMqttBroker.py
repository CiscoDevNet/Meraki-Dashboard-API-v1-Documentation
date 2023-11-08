import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
mqtt_broker_id = ''

response = dashboard.networks.updateNetworkMqttBroker(
    network_id, mqtt_broker_id, 
    name='MQTT_Broker_1', 
    host='1.1.1.1', 
    port=1234, 
    security={'mode': 'tls', 'tls': {'hasCaCertificate': True, 'verifyHostnames': True}}, 
    authentication={'username': 'Username'}
)

print(response)