import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
allowed_rules = [{'ruleId': 'meraki:intrusion/snort/GID/01/SID/688', 'message': 'SQL sa login failed'}, {'ruleId': 'meraki:intrusion/snort/GID/01/SID/5805', 'message': 'MALWARE-OTHER Trackware myway speedbar runtime detection - switch engines'}]

response = dashboard.appliance.updateOrganizationApplianceSecurityIntrusion(
    organization_id, allowed_rules
)

print(response)