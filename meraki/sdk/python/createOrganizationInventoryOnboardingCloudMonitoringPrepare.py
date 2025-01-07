import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(API_KEY)

organization_id = '549236'
devices = [{'sudi': '-----BEGIN CERTIFICATE-----\n        MIIDyTCCArGgAwIBAgIKBBNXOVCGU1YztjANBgkqhkiG9w0BAQsFADAnMQ4wDAYD\n        VQQKEwVDaXNjbzEVMBMGA1UEAxMMQUNUMiBTVURJIENBMB4XDTIxMDUzMTEzNTUx\n        NVoXDTI5MDUxNDIwMjU0MVowbTEpMCcGA1UEBRMgUElEOkM5MjAwTC0yNFAtNEcg\n        U046SkFFMjUyMjBSMksxDjAMBgNVBAoTBUNpc2NvMRgwFgYDVQQLEw9BQ1QtMiBM\n        aXRlIFNVREkxFjAUBgNVBAMTDUM5MjAwTC0yNFAtNEcwggEiMA0GCSqGSIb3DQEB\n        AQUAA4IBDwAwggEKAoIBAQDaUPxW76gT5MdoEAt+UrDFiYA9RYh2iHicDViBEyow\n        TR1TuP36bHh13X3vtGiDsCD88Ci2TZIqd/EDkkc7v9ipUUYVVH+YDrPt2Aukb1PH\n        D6K0R+KhgEzRo5x54TlU6oWvjUpwNZUwwdhMWIQaUVkMyZBYNy0jGPLO8jwZhyBg\n        1Fneybr9pwedGbLrAaz+gdEikB8B4a/fvPjVfL5Ngb4QRjFqWuE+X3nLc0kHedep\n        6nfgpUNXMlStVm5nIXKP6OjmzfCHPYh9L2Ehs1TrSk1ser9Ofx0ZMVL/jBZR2EIj\n        OZ8tH6KlX2/B2pbSPIO6kD5c4UA8Cf1SbDJCwJ/kI9ihAgMBAAGjgbAwga0wDgYD\n        VR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUSNjx8cJw1Vu7\n        fHMJk6+4uDAD+H8wTQYDVR0RBEYwRKBCBgkrBgEEAQkVAgOgNRMzQ2hpcElEPVVV\n        VUNNaElGcUVFMklFUUVBQWNBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9MB0GA1Ud\n        DgQWBBRdhMkFD/z5hokaQeLbaRsp4hkvbzANBgkqhkiG9w0BAQsFAAOCAQEAMtuh\n        YpBz4xEZ7YdJsLpw67Q0TTJGnTBRpzAeY1urYDoDz8TSx556XG7z3IRzuED5KVSp\n        OwmH/iZ+tDfYQ3W3ElWTW93871DkuW4WQIfbnoHg/F7bF0DKYVkD3rpZjyz3NhzH\n        d7cjTdJXQ85bTAOXDuxKH3qewrXxxOGXgh3I6NUq0UwMTWh84lND7Jl+ZAQkYNS2\n        iHanTZFQBk3ML0NUb7fKDYGRTZRqwQ/upIO4S6LV1cxH/6V0qbMy3sCSHZoMLrW3\n        0m3M6yKpe5+VZzHZwmWdUf3Ot+zKjhveK5/YNsMIASdvtvymxUizq2Hr1hvR/kPc\n        p1vuyWxipU8JfzOh/A==\n        -----END CERTIFICATE-----\n        ', 'tunnel': {'certificateName': 'DeviceSUDI', 'name': 'MERAKI', 'loopbackNumber': 1000, 'localInterface': 1}, 'user': {'username': 'Meraki'}, 'vty': {'startLineNumber': 16, 'endLineNumber': 17, 'authentication': {'group': {'name': ''}}, 'authorization': {'group': {'name': 'MERAKI'}}, 'accessList': {'vtyIn': {'name': 'MERAKI_IN'}, 'vtyOut': {'name': 'MERAKI_OUT'}}, 'rotaryNumber': 50}}]

response = dashboard.organizations.createOrganizationInventoryOnboardingCloudMonitoringPrepare(
    organization_id, devices, 
    options={'skipCommit': False}
)

print(response)