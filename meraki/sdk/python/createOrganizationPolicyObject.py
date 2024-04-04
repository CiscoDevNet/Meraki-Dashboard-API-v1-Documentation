import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
name = 'Web Servers - Datacenter 10'
category = 'network'
type = 'cidr'

response = dashboard.organizations.createOrganizationPolicyObject(
    organization_id, name, category, type, 
    cidr='10.0.0.0/24', 
    fqdn='example.com', 
    mask='255.255.0.0', 
    ip='1.2.3.4', 
    groupIds=['8']
)

print(response)