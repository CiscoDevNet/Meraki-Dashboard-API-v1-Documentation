import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
peers = [{'name': 'Peer Name', 'publicIp': '123.123.123.1', 'privateSubnets': ['192.168.1.0/24', '192.168.128.0/24'], 'localId': 'myMXId@meraki.com', 'remoteId': 'miles@meraki.com', 'ipsecPolicies': {'ikeCipherAlgo': ['tripledes'], 'ikeAuthAlgo': ['sha1'], 'ikePrfAlgo': ['prfsha1'], 'ikeDiffieHellmanGroup': ['group2'], 'ikeLifetime': 28800, 'childCipherAlgo': ['aes128'], 'childAuthAlgo': ['sha1'], 'childPfsGroup': ['disabled'], 'childLifetime': 28800}, 'ipsecPoliciesPreset': 'default', 'secret': 'Sample Password', 'ikeVersion': '2', 'networkTags': ['none']}]

response = dashboard.appliance.updateOrganizationApplianceVpnThirdPartyVPNPeers(
    organization_id, peers
)

print(response)