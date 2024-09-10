import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

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