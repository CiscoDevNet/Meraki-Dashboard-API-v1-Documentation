import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
peers = [{'name': 'Peer Name', 'publicIp': '123.123.123.1', 'privateSubnets': ['192.168.1.0/24', '192.168.128.0/24'], 'localId': 'myMXId@meraki.com', 'remoteId': 'miles@meraki.com', 'ipsecPolicies': {'ikeCipherAlgo': ['tripledes'], 'ikeAuthAlgo': ['sha1'], 'ikePrfAlgo': ['prfsha1'], 'ikeDiffieHellmanGroup': ['group2'], 'ikeLifetime': 28800, 'childCipherAlgo': ['aes128'], 'childAuthAlgo': ['sha1'], 'childPfsGroup': ['disabled'], 'childLifetime': 28800}, 'ipsecPoliciesPreset': 'default', 'secret': 'Sample Password', 'ikeVersion': '2', 'networkTags': ['none']}]

response = dashboard.appliance.updateOrganizationApplianceVpnThirdPartyVPNPeers(
    organization_id, peers
)

print(response)