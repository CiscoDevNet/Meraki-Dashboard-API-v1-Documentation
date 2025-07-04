import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.devices.updateDevice(
    serial, 
    name='My AP', 
    tags=[' recently-added '], 
    lat=37.4180951010362, 
    lng=-122.098531723022, 
    address='1600 Pennsylvania Ave', 
    notes='My AP's note', 
    moveMapMarker=True, 
    switchProfileId='1234', 
    floorPlanId='g_2176982374'
)

print(response)