import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

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