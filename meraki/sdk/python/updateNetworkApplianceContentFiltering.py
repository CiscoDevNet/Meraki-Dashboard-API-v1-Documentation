import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

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