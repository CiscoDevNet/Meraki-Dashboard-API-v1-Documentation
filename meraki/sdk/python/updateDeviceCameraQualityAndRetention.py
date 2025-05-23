import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2QN-9J8L-SLPD'

response = dashboard.camera.updateDeviceCameraQualityAndRetention(
    serial, 
    profileId='1234', 
    motionBasedRetentionEnabled=False, 
    audioRecordingEnabled=False, 
    restrictedBandwidthModeEnabled=False, 
    quality='Standard', 
    resolution='1280x720', 
    motionDetectorVersion=2
)

print(response)