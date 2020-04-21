import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
branding_policy_ids = ['123', '456', '789']

response = dashboard.organizations.updateOrganizationBrandingPoliciesPriorities(
    organization_id, branding_policy_ids
)

print(response)