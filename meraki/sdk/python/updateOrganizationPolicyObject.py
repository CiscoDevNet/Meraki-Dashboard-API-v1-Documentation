import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
policy_object_id = ''

response = dashboard.organizations.updateOrganizationPolicyObject(
    organization_id, policy_object_id, 
    name='Web Servers - Datacenter 10', 
    groupIds=[]
)

print(response)