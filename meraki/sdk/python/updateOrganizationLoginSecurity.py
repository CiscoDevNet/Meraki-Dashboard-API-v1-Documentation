import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'

response = dashboard.organizations.updateOrganizationLoginSecurity(
    organization_id, 
    enforcePasswordExpiration=True, 
    passwordExpirationDays=90, 
    enforceDifferentPasswords=True, 
    numDifferentPasswords=3, 
    enforceStrongPasswords=True, 
    enforceAccountLockout=True, 
    accountLockoutAttempts=3, 
    enforceIdleTimeout=True, 
    idleTimeoutMinutes=30, 
    enforceTwoFactorAuth=True, 
    enforceLoginIpRanges=True, 
    loginIpRanges=['192.195.83.1', '192.195.83.255'], 
    apiAuthentication={'ipRestrictionsForKeys': {'enabled': True, 'ranges': ['192.195.83.1', '192.168.33.33']}}
)

print(response)