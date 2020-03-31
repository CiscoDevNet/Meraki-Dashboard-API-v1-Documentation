collect = {}
organization_id = 'organizationId4'
collect['organization_id'] = organization_id

claim_organization = ClaimOrganizationModel()
claim_organization.orders = ['4CXXXXXXX']
claim_organization.serials = ['Q234-ABCD-5678']
claim_organization.licenses = []

claim_organization.licenses.append(LicenseModel())
claim_organization.licenses[0].key = 'Z2XXXXXXXXXX'
claim_organization.licenses[0].mode = Mode2Enum.ADDDEVICES

collect['claim_organization'] = claim_organization

result = organizations_controller.claim_organization(collect)
