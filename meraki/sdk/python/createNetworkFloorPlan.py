import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
name = 'HQ Floor Plan'
image_contents = '2a9edd3f4ffd80130c647d13eacb59f3'

response = dashboard.networks.createNetworkFloorPlan(
    network_id, name, image_contents, 
    center={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    bottomLeftCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    bottomRightCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    topLeftCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    topRightCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    floorNumber=5.0
)

print(response)