import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
meraki_auth_user_id = ''

response = dashboard.networks.updateNetworkMerakiAuthUser(
    network_id, meraki_auth_user_id, 
    name='Miles Meraki', 
    password='secret', 
    emailPasswordToUser=False, 
    authorizations=[{'ssidNumber': 1, 'expiresAt': '2018-03-13T00:00:00.090210Z'}]
)

print(response)