import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

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