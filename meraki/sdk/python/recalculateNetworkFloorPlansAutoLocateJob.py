import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
job_id = ''

response = dashboard.networks.recalculateNetworkFloorPlansAutoLocateJob(
    network_id, job_id, 
    devices=[{'serial': 'Q234-ABCD-5678', 'autoLocate': {'isAnchor': True, 'lat': 37.4180951010362, 'lng': -122.098531723022}}]
)

print(response)