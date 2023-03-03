import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'

response = dashboard.organizations.createOrganizationBrandingPolicy(
    organization_id, 
    name='My Branding Policy', 
    enabled=True, 
    adminSettings={'appliesTo': 'All admins of networks...', 'values': ['N_1234', 'L_5678']}, 
    helpSettings={'helpTab': 'show', 'getHelpSubtab': 'default or inherit', 'communitySubtab': 'show', 'casesSubtab': 'hide', 'dataProtectionRequestsSubtab': 'default or inherit', 'getHelpSubtabKnowledgeBaseSearch': '<h1>Some custom HTML content</h1>', 'universalSearchKnowledgeBaseSearch': 'hide', 'ciscoMerakiProductDocumentation': 'show', 'supportContactInfo': 'show', 'newFeaturesSubtab': 'show', 'firewallInfoSubtab': 'hide', 'apiDocsSubtab': 'default or inherit', 'hardwareReplacementsSubtab': 'hide', 'smForums': 'hide', 'helpWidget': 'hide'}, 
    customLogo={'enabled': True, 'image': {'contents': 'Hyperg26C8F4h8CvcoUqpA==', 'format': 'jpg'}}
)

print(response)