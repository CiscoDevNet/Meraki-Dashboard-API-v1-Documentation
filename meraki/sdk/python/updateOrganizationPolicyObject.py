import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
policy_object_id = ''

response = dashboard.organizations.updateOrganizationPolicyObject(
    organization_id, policy_object_id, 
    name='Web Servers - Datacenter 10', 
    cidr='10.0.0.0/24', 
    fqdn='example.com', 
    mask='255.255.0.0', 
    ip='1.2.3.4', 
    groupIds=['8']
)

print(response)