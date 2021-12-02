import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidSplashSettings(
    network_id, number, 
    splashUrl='https://www.custom_splash_url.com', 
    useSplashUrl=True, 
    redirectUrl='https://example.com', 
    useRedirectUrl=True, 
    welcomeMessage='Welcome!', 
    splashLogo={'md5': 'abcd1234', 'extension': 'jpg'}, 
    splashImage={'md5': '542cccac8d7dedee0f185311d154d194'}, 
    splashPrepaidFront={'md5': '542cccac8d7dedee0f185311d154d194'}
)

print(response)