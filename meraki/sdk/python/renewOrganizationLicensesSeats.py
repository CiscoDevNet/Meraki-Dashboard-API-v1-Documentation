import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
license_id_to_renew = '123'
unused_license_id = '1234'

response = dashboard.organizations.renewOrganizationLicensesSeats(
    organization_id, license_id_to_renew, unused_license_id
)

print(response)