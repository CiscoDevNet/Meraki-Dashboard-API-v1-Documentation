import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
name = 'Default profile'
hostnames = ['*.test1.com', '*.test2.com']
nameservers = {'addresses': ['12.1.10.1']}

response = dashboard.appliance.createOrganizationApplianceDnsSplitProfile(
    organization_id, name, hostnames, nameservers
)

print(response)