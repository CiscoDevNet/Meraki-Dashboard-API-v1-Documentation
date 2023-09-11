import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
serials = ['Q234-ABCD-5678']
stack_ids = ['1234']

response = dashboard.networks.reassignNetworkVlanProfilesAssignments(
    network_id, serials, stack_ids, 
    vlanProfile={'iname': 'Profile1'}
)

print(response)