import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'L_646829496481105433'
number = ''

response = dashboard.wireless.updateNetworkWirelessSsidSplashSettings(
    network_id, number, 
    splashUrl='https://www.custom_splash_url.com', 
    useSplashUrl=True, 
    splashTimeout=1440, 
    redirectUrl='https://example.com', 
    useRedirectUrl=True, 
    welcomeMessage='Welcome!', 
    splashLogo={'md5': 'abcd1234', 'extension': 'jpg', 'image': {'format': 'jpg', 'contents': 'Q2lzY28gTWVyYWtp'}}, 
    splashImage={'md5': '542cccac8d7dedee0f185311d154d194', 'extension': 'jpg', 'image': {'format': 'jpg', 'contents': 'Q2lzY28gTWVyYWtp'}}, 
    splashPrepaidFront={'md5': '542cccac8d7dedee0f185311d154d194', 'extension': 'jpg', 'image': {'format': 'jpg', 'contents': 'Q2lzY28gTWVyYWtp'}}, 
    blockAllTrafficBeforeSignOn=False, 
    controllerDisconnectionBehavior='default', 
    allowSimultaneousLogins=False, 
    guestSponsorship={'durationInMinutes': 30, 'guestCanRequestTimeframe': False}, 
    billing={'freeAccess': {'enabled': True, 'durationInMinutes': 120}, 'prepaidAccessFastLoginEnabled': True, 'replyToEmailAddress': 'user@email.com'}, 
    sentryEnrollment={'systemsManagerNetwork': {'id': 'N_1234'}, 'strength': 'focused', 'enforcedSystems': ['iOS']}
)

print(response)