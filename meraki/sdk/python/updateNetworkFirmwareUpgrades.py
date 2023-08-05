import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.networks.updateNetworkFirmwareUpgrades(
    network_id, 
    upgradeWindow={'dayOfWeek': 'sun', 'hourOfDay': '4:00'}, 
    timezone='America/Los_Angeles', 
    products={'wireless': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1000'}}, 'participateInNextBetaRelease': False}, 'appliance': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1001'}}, 'participateInNextBetaRelease': False}, 'switch': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1002'}}, 'participateInNextBetaRelease': False}, 'camera': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1003'}}, 'participateInNextBetaRelease': False}, 'cellularGateway': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1004'}}, 'participateInNextBetaRelease': False}, 'sensor': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1005'}}, 'participateInNextBetaRelease': False}, 'cloudGateway': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1006'}}, 'participateInNextBetaRelease': False}, 'switchCatalyst': {'nextUpgrade': {'time': '2019-03-17T17:22:52Z', 'toVersion': {'id': '1234'}}, 'participateInNextBetaRelease': False}}
)

print(response)