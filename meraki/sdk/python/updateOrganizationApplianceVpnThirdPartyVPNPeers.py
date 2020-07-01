import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
peers = [{'name': 'My peer 1', 'publicIp': '123.123.123.1', 'privateSubnets': ['192.168.1.0/24', '192.168.128.0/24'], 'secret': 'asdf1234', 'ikeVersion': '2', 'ipsecPolicies': {'ikeCipherAlgo': ['tripledes'], 'ikeAuthAlgo': ['sha1'], 'ikePrfAlgo': ['prfsha1'], 'ikeDiffieHellmanGroup': ['group2'], 'ikeLifetime': 28800, 'childCipherAlgo': ['aes128'], 'childAuthAlgo': ['sha1'], 'childPfsGroup': ['disabled'], 'childLifetime': 28800}, 'networkTags': ['all']}, {'name': 'My peer 2', 'publicIp': '123.123.123.2', 'remoteId': 'miles@meraki.com', 'privateSubnets': ['192.168.2.0/24', '192.168.129.0/24'], 'secret': 'asdf56785678567856785678', 'networkTags': ['none'], 'ikeVersion': '1', 'ipsecPoliciesPreset': 'default'}]

response = dashboard.appliance.updateOrganizationApplianceVpnThirdPartyVPNPeers(
    organization_id, peers
)

print(response)