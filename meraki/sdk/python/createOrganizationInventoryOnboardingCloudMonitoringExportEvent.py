import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
log_event = 'download'
timestamp = 1526087474

response = dashboard.organizations.createOrganizationInventoryOnboardingCloudMonitoringExportEvent(
    organization_id, log_event, timestamp, 
    targetOS='mac', 
    request='r=cb'
)

print(response)