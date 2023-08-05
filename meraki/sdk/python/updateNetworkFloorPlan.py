import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
floor_plan_id = ''

response = dashboard.networks.updateNetworkFloorPlan(
    network_id, floor_plan_id, 
    name='HQ Floor Plan', 
    center={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    bottomLeftCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    bottomRightCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    topLeftCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    topRightCorner={'lat': 37.770040510499996, 'lng': -122.38714009525}, 
    imageContents='2a9edd3f4ffd80130c647d13eacb59f3'
)

print(response)