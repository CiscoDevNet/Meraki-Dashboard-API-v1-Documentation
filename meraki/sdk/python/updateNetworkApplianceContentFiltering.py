import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'

response = dashboard.appliance.updateNetworkApplianceContentFiltering(
    network_id, 
    allowedUrlPatterns=['http://www.example.org', 'http://help.com.au'], 
    blockedUrlPatterns=['http://www.example.com', 'http://www.betting.com'], 
    blockedUrlCategories=['meraki:contentFiltering/category/1', 'meraki:contentFiltering/category/7'], 
    urlCategoryListSize='topSites'
)

print(response)