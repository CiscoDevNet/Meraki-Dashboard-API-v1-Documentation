import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
id_ = ''

response = dashboard.sensor.updateNetworkSensorAlertsProfile(
    network_id, id_, 
    name='My Sensor Alert Profile', 
    schedule={'id': '5'}, 
    conditions=[{'metric': 'temperature', 'threshold': {'temperature': {'celsius': 20.5, 'fahrenheit': 70.0, 'quality': 'good'}, 'humidity': {'relativePercentage': 65, 'quality': 'inadequate'}, 'water': {'present': True}, 'door': {'open': True}, 'tvoc': {'concentration': 400, 'quality': 'poor'}, 'co2': {'concentration': 400, 'quality': 'poor'}, 'pm25': {'concentration': 90, 'quality': 'fair'}, 'noise': {'ambient': {'level': 120, 'quality': 'poor'}}, 'indoorAirQuality': {'score': 80, 'quality': 'fair'}, 'realPower': {'draw': 14.1}, 'apparentPower': {'draw': 17.2}, 'powerFactor': {'percentage': 81}, 'current': {'draw': 0.14}, 'voltage': {'level': 119.5}, 'frequency': {'level': 58.8}, 'upstreamPower': {'outageDetected': True}}, 'direction': 'above', 'duration': 60}], 
    recipients={'emails': ['miles@meraki.com'], 'smsNumbers': ['+15555555555'], 'httpServerIds': ['aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M=']}, 
    serials=['Q234-ABCD-0001', 'Q234-ABCD-0002', 'Q234-ABCD-0003'], 
    includeSensorUrl=True, 
    message='Check with Miles on what to do.'
)

print(response)