import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481104079'

response = dashboard.appliance.updateNetworkApplianceSecurityIntrusion(
    network_id, 
    mode='prevention', 
    idsRulesets='balanced', 
    protectedNetworks={'useDefault': False, 'includedCidr': ['10.0.0.0/8', '127.0.0.0/8', '169.254.0.0/16', '172.16.0.0/12'], 'excludedCidr': ['10.0.0.0/8', '127.0.0.0/8']}
)

print(response)