import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

claim_key = 'S2345-6789A-BCDEF-GHJKM'
organization_id = '12345678910'

response = dashboard.licensing.claimAdministeredLicensingSubscriptionSubscriptions(
    claim_key, organization_id, 
    name='Corporate subscription', 
    description='Subscription for all main offices'
)

print(response)