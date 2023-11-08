import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
acl_id = ''

response = dashboard.organizations.updateOrganizationAdaptivePolicyAcl(
    organization_id, acl_id, 
    name='Block sensitive web traffic', 
    description='Blocks sensitive web traffic', 
    rules=[{'policy': 'deny', 'protocol': 'tcp', 'srcPort': '1,33', 'dstPort': '22-30'}], 
    ipVersion='ipv6'
)

print(response)