import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
dest_organization_id = '2930418'
license_id = '1234'
seat_count = 20

response = dashboard.organizations.moveOrganizationLicensesSeats(
    organization_id, dest_organization_id, license_id, seat_count
)

print(response)