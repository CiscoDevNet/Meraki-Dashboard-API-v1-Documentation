import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
devices = [{'deviceId': '161b2602-a713-4aac-b1eb-d9b55205353d', 'udi': 'PID:C9200L-24P-4G SN:JAE25220R2K', 'networkId': '1338481'}]

response = dashboard.organizations.createOrganizationInventoryOnboardingCloudMonitoringImport(
    organization_id, devices
)

print(response)