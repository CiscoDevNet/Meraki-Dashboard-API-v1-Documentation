import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceSecurityIntrusion(
    network_id, 
    mode='prevention', 
    idsRulesets='balanced', 
    protectedNetworks={'useDefault': False, 'includedCidr': ['10.0.0.0/8', '127.0.0.0/8', '169.254.0.0/16', '172.16.0.0/12'], 'excludedCidr': ['10.0.0.0/8', '127.0.0.0/8']}
)

print(response)