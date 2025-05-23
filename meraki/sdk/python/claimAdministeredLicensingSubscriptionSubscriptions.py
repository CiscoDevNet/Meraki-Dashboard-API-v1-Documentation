import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

claim_key = 'S2345-6789A-BCDEF-GHJKM'
organization_id = '12345678910'

response = dashboard.licensing.claimAdministeredLicensingSubscriptionSubscriptions(
    claim_key, organization_id, 
    name='Corporate subscription', 
    description='Subscription for all main offices'
)

print(response)