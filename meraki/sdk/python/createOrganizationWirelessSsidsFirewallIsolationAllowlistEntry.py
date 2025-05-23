import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
client = {'mac': 'A1:B2:C3:D4:E5:F6'}
ssid = {'number': 2}
network = {'id': 'N_123'}

response = dashboard.wireless.createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(
    organization_id, client, ssid, network, 
    description='Example mac address'
)

print(response)