import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
monitored_media_server_id = ''

response = dashboard.insight.deleteOrganizationInsightMonitoredMediaServer(
    organization_id, monitored_media_server_id
)

print(response)