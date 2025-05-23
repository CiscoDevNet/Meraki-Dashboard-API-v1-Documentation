import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
account_id = '0987654321'
api_key = 'foobarfoobarfoobarfoobarfoobarfoobar'
service_provider = {'name': 'ATT'}
title = 'My AT&T account'
username = 'MerakiUser'

response = dashboard.cellularGateway.createOrganizationCellularGatewayEsimsServiceProvidersAccount(
    organization_id, account_id, api_key, service_provider, title, username
)

print(response)