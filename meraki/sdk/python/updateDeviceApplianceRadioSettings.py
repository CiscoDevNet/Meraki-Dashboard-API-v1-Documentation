import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.appliance.updateDeviceApplianceRadioSettings(
    serial, 
    rfProfileId='1234', 
    twoFourGhzSettings={'channel': 11, 'targetPower': 21}, 
    fiveGhzSettings={'channel': 149, 'channelWidth': 20, 'targetPower': 15}
)

print(response)