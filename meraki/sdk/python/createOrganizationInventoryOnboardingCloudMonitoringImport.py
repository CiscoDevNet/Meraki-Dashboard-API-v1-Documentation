import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
devices = [{'deviceId': '161b2602-a713-4aac-b1eb-d9b55205353d', 'udi': 'PID:C9200L-24P-4G SN:JAE25220R2K', 'networkId': '1338481'}]

response = dashboard.organizations.createOrganizationInventoryOnboardingCloudMonitoringImport(
    organization_id, devices
)

print(response)