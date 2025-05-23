import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'

response = dashboard.organizations.updateOrganizationLoginSecurity(
    organization_id, 
    enforcePasswordExpiration=True, 
    passwordExpirationDays=90, 
    enforceDifferentPasswords=True, 
    numDifferentPasswords=3, 
    enforceStrongPasswords=True, 
    minimumPasswordLength=12, 
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