import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
mqtt_broker_id = ''

response = dashboard.networks.updateNetworkMqttBroker(
    network_id, mqtt_broker_id, 
    name='MQTT_Broker_1', 
    host='1.1.1.1', 
    port=1234
)

print(response)