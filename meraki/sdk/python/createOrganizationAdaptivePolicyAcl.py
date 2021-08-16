import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
name = 'Block sensitive web traffic'
rules = [{'policy': 'deny', 'protocol': 'tcp', 'srcPort': '1,33', 'dstPort': '22-30'}, {'policy': 'allow', 'protocol': 'any', 'srcPort': 'any', 'dstPort': 'any'}]
ip_version = 'ipv6'

response = dashboard.organizations.createOrganizationAdaptivePolicyAcl(
    organization_id, name, rules, ip_version, 
    description='Blocks sensitive web traffic'
)

print(response)