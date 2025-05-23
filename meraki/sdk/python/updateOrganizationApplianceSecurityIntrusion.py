import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
allowed_rules = [{'ruleId': 'meraki:intrusion/snort/GID/01/SID/688', 'message': 'SQL sa login failed'}, {'ruleId': 'meraki:intrusion/snort/GID/01/SID/5805', 'message': 'MALWARE-OTHER Trackware myway speedbar runtime detection - switch engines'}]

response = dashboard.appliance.updateOrganizationApplianceSecurityIntrusion(
    organization_id, allowed_rules
)

print(response)