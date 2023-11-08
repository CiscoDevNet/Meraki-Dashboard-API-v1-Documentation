import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
branding_policy_id = ''

response = dashboard.organizations.updateOrganizationBrandingPolicy(
    organization_id, branding_policy_id, 
    name='My Branding Policy', 
    enabled=True, 
    adminSettings={'appliesTo': 'All admins of networks...', 'values': ['N_1234', 'L_5678']}, 
    helpSettings={'helpTab': 'show', 'getHelpSubtab': 'default or inherit', 'communitySubtab': 'show', 'casesSubtab': 'hide', 'dataProtectionRequestsSubtab': 'default or inherit', 'getHelpSubtabKnowledgeBaseSearch': '<h1>Some custom HTML content</h1>', 'universalSearchKnowledgeBaseSearch': 'hide', 'ciscoMerakiProductDocumentation': 'show', 'supportContactInfo': 'show', 'newFeaturesSubtab': 'show', 'firewallInfoSubtab': 'hide', 'apiDocsSubtab': 'default or inherit', 'hardwareReplacementsSubtab': 'hide', 'smForums': 'hide', 'helpWidget': 'hide'}, 
    customLogo={'enabled': True, 'image': {'contents': 'Hyperg26C8F4h8CvcoUqpA==', 'format': 'jpg'}}
)

print(response)