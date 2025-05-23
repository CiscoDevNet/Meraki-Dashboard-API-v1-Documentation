import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'MQTT_Broker_1'
host = '1.2.3.4'
port = 443

response = dashboard.networks.createNetworkMqttBroker(
    network_id, name, host, port, 
    security={'mode': 'tls', 'tls': {'caCertificate': '*****', 'verifyHostnames': True}}, 
    authentication={'username': 'milesmeraki', 'password': '*****'}
)

print(response)