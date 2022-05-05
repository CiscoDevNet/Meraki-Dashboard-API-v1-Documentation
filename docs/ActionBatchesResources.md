
**Group**|**Summary**|**Resource**|**operation** 
:-------------:|:-------------:|:-------------:|:-------------:
Adaptive policy| Add an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies`| create
Adaptive policy| Delete an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies/{adaptivePolicyId}`| destroy
Adaptive policy| Update an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies/{adaptivePolicyId}`| update
Adaptive policy group| Creates a new adaptive policy group| `/organizations/{organizationId}/adaptivePolicy/groups`| create
Adaptive policy group| Deletes the specified adaptive policy group and any associated policies and references| `/organizations/{organizationId}/adaptivePolicy/groups/{groupId}`| destroy
Adaptive policy group| Updates an adaptive policy group. If updating "Infrastructure", only the SGT is allowed. Cannot update "Unknown".| `/organizations/{organizationId}/adaptivePolicy/groups/{groupId}`| update
Alternate management interface| Update the switch alternate management interface for the network| `/networks/{networkId}/switch/alternateManagementInterface`| update
Bgp setting| Update a Hub BGP Configuration| `/networks/{networkId}/appliance/vpn/bgp`| update
Billing| Update the billing settings| `/networks/{networkId}/wireless/billing`| update
Bluetooth device setting| Update the bluetooth settings for a wireless device| `/devices/{serial}/wireless/bluetooth/settings`| update
Camera custom analytics settings| Update custom analytics settings for a camera| `/devices/{serial}/camera/customAnalytics`| update
Camera video settings| Update video settings for the given camera| `/devices/{serial}/camera/video/settings`| update
Camera wireless profile settings| Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.| `/devices/{serial}/camera/wirelessProfiles`| update
Cellular gateway connectivity monitoring destination| Update the connectivity testing destinations for an MG network| `/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations`| update
Cellular gateway device lan| Update the LAN Settings for a single MG.| `/devices/{serial}/cellularGateway/lan`| update
Cellular gateway dhcp setting| Update common DHCP settings of MGs| `/networks/{networkId}/cellularGateway/dhcp`| update
Cellular gateway port forwarding rules| Updates the port forwarding rules for a single MG.| `/devices/{serial}/cellularGateway/portForwardingRules`| update
Cellular gateway subnet pool| Update the subnet pool and mask configuration for MGs in the network.| `/networks/{networkId}/cellularGateway/subnetPool`| update
Cellular gateway uplink setting| Updates the uplink settings for your MG network.| `/networks/{networkId}/cellularGateway/uplink`| update
Client| Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.| `/networks/{networkId}/clients`| provision
Config template| Create a new configuration template| `/organizations/{organizationId}/configTemplates`| create
Config template| Update a configuration template| `/organizations/{organizationId}/configTemplates/{configTemplateId}`| update
Custom performance class| Add a custom performance class for an MX network| `/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses`| create
Custom performance class| Delete a custom performance class from an MX network| `/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}`| destroy
Custom performance class| Update a custom performance class for an MX network| `/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}`| update
Device| Update the attributes of a device| `/devices/{serial}`| update
Device| Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)| `/networks/{networkId}/devices`| claim
Device| Remove a single device| `/networks/{networkId}/devices`| remove
Dhcp server policy| Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively| `/networks/{networkId}/switch/dhcpServerPolicy`| update
Dscp cos mapping| Update the DSCP to CoS mappings| `/networks/{networkId}/switch/dscpToCosMappings`| update
Eap override| Update the EAP overridden parameters for an SSID.| `/networks/{networkId}/wireless/ssids/{number}/eapOverride`| update
Firmware upgrade rollback| Rollback a Firmware Upgrade For A Network| `/networks/{networkId}/firmwareUpgrades/rollbacks`| create
Firmware upgrades update| Update firmware upgrade information for a network| `/networks/{networkId}/firmwareUpgrades`| update
Floor plan| Destroy a floor plan| `/networks/{networkId}/floorPlans/{floorPlanId}`| destroy
Floor plan| Update a floor plan's geolocation and other meta data| `/networks/{networkId}/floorPlans/{floorPlanId}`| update
Group policy| Create a group policy| `/networks/{networkId}/groupPolicies`| create
Group policy| Delete a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| destroy
Group policy| Update a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| update
Hotspot20| Update the Hotspot 2.0 settings of an SSID| `/networks/{networkId}/wireless/ssids/{number}/hotspot20`| update
L3 firewall| Update the L3 firewall rules of an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules`| update
L3 interface| Create a layer 3 interface for a switch| `/devices/{serial}/switch/routing/interfaces`| create
L3 interface| Delete a layer 3 interface from the switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}`| destroy
L3 interface| Update a layer 3 interface for a switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}`| update
L3 interface dhcp| Update a layer 3 interface DHCP configuration for a switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp`| update
L3 static route| Create a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes`| create
L3 static route| Delete a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}`| destroy
L3 static route| Update a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}`| update
License| Assign SM seats to a network. This will increase the managed SM device limit of the network| `/organizations/{organizationId}/licenses`| assignSeats
License| Move licenses to another organization. This will also move any devices that the licenses are assigned to| `/organizations/{organizationId}/licenses`| move
License| Move SM seats to another organization| `/organizations/{organizationId}/licenses`| moveSeats
License| Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license| `/organizations/{organizationId}/licenses`| renewSeats
License| Update a license| `/organizations/{organizationId}/licenses/{licenseId}`| update
Link aggregation| Create a link aggregation group| `/networks/{networkId}/switch/linkAggregations`| create
Link aggregation| Split a link aggregation group into separate ports| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| destroy
Link aggregation| Update a link aggregation group| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| update
MTU configuration| Update the MTU configuration| `/networks/{networkId}/switch/mtu`| update
MX VLAN settings| Enable/Disable VLANs for the given network| `/networks/{networkId}/appliance/vlans/settings`| update
MX connectivity monitoring destination| Update the connectivity testing destinations for an MX network| `/networks/{networkId}/appliance/connectivityMonitoringDestinations`| update
MX l7 firewall| Update the MX L7 firewall rules for an MX network| `/networks/{networkId}/appliance/firewall/l7FirewallRules`| update
MX port| Update the per-port VLAN settings for a single MX port.| `/networks/{networkId}/appliance/ports/{portId}`| update
MX uplink setting| Updates the uplink bandwidth settings for your MX network.| `/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth`| update
Management interface settings| Update the management interface settings for a device| `/devices/{serial}/managementInterface`| update
Meraki auth user| Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)| `/networks/{networkId}/merakiAuthUsers`| create
Meraki auth user| Deauthorize a user. To reauthorize a user after deauthorizing them, POST to this endpoint. (Currently, 802.1X RADIUS, splash guest, and client VPN users can be deauthorized.)| `/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}`| destroy
Meraki auth user| Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)| `/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}`| update
Monitored media server| Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers`| create
Monitored media server| Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| destroy
Monitored media server| Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| update
Mqtt broker| Add an MQTT broker| `/networks/{networkId}/mqttBrokers`| create
Mqtt broker| Delete an MQTT broker| `/networks/{networkId}/mqttBrokers/{mqttBrokerId}`| destroy
Mqtt broker| Update an MQTT broker| `/networks/{networkId}/mqttBrokers/{mqttBrokerId}`| update
Multicast| Update multicast settings for a network| `/networks/{networkId}/switch/routing/multicast`| update
Network| Bind a network to a template.| `/networks/{networkId}`| bind
Network| Delete a network| `/networks/{networkId}`| destroy
Network| Split a combined network into individual networks for each type of device| `/networks/{networkId}`| split
Network| Unbind a network from a template.| `/networks/{networkId}`| unbind
Network| Update a network| `/networks/{networkId}`| update
Network| Combine multiple networks into a single network| `/organizations/{organizationId}/networks`| combine
Network| Create a network| `/organizations/{organizationId}/networks`| create
Network settings| Update the settings for a network| `/networks/{networkId}/settings`| update
Org wide alerts/alert config| Create an organization-wide alert configuration| `/organizations/{organizationId}/alerts/profiles`| create
Org wide alerts/alert config| Removes an organization-wide alert config| `/organizations/{organizationId}/alerts/profiles/{alertConfigId}`| destroy
Org wide alerts/alert config| Update an organization-wide alert config| `/organizations/{organizationId}/alerts/profiles/{alertConfigId}`| update
Organization SAML IdP| Create a SAML IdP for your organization.| `/organizations/{organizationId}/saml/idps`| create
Organization SAML IdP| Remove a SAML IdP in your organization.| `/organizations/{organizationId}/saml/idps/{idpId}`| destroy
Organization SAML IdP| Update a SAML IdP in your organization| `/organizations/{organizationId}/saml/idps/{idpId}`| update
Organization login security settings| Update the login security settings for an organization| `/organizations/{organizationId}/loginSecurity`| update
Ospf routing| Update layer 3 OSPF routing configuration| `/networks/{networkId}/switch/routing/ospf`| update
Psk group| Create an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks`| create
Psk group| Delete an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}`| destroy
Psk group| Update an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}`| update
Qos rule| Add a quality of service rule| `/networks/{networkId}/switch/qosRules`| create
Qos rule| Update the order in which the rules should be processed by the switch| `/networks/{networkId}/switch/qosRules/order`| update_order
Qos rule| Delete a quality of service rule| `/networks/{networkId}/switch/qosRules/{qosRuleId}`| destroy
Qos rule| Update a quality of service rule| `/networks/{networkId}/switch/qosRules/{qosRuleId}`| update
Quality and retention setting| Update quality and retention settings for the given camera| `/devices/{serial}/camera/qualityAndRetention`| update
RF profile| Creates new RF profile for this network| `/networks/{networkId}/wireless/rfProfiles`| create
RF profile| Delete a RF Profile| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| destroy
RF profile| Updates specified RF profile for this network| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| update
Radio settings| Update the radio settings of a device| `/devices/{serial}/wireless/radio/settings`| update
Rendezvous point| Create a multicast rendezvous point| `/networks/{networkId}/switch/routing/multicast/rendezvousPoints`| create
Rendezvous point| Delete a multicast rendezvous point| `/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}`| destroy
Rendezvous point| Update a multicast rendezvous point| `/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}`| update
STP configuration| Updates STP settings| `/networks/{networkId}/switch/stp`| update
Sense setting| Update sense settings for the given camera| `/devices/{serial}/camera/sense`| update
Single lan| Update single LAN configuration| `/networks/{networkId}/appliance/singleLan`| update
Site to site vpn| Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.| `/networks/{networkId}/appliance/vpn/siteToSiteVpn`| update
Ssid| Update the attributes of an MR SSID| `/networks/{networkId}/wireless/ssids/{number}`| update
Ssid bonjour forwarding| Update the bonjour forwarding setting and rules for the SSID| `/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding`| update
Ssid device type group policies| Update the device type group policies for the SSID| `/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies`| update
Ssid outage schedule| Update the outage schedule for the SSID| `/networks/{networkId}/wireless/ssids/{number}/schedules`| update
Ssid splash settings| Modify the splash page settings for the given SSID| `/networks/{networkId}/wireless/ssids/{number}/splash/settings`| update
Ssid vpn| Update the VPN settings for the SSID| `/networks/{networkId}/wireless/ssids/{number}/vpn`| update
Storm control| Update the storm control configuration for a switch network| `/networks/{networkId}/switch/stormControl`| update
Switch| Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring| `/organizations/{organizationId}/switch/devices`| clone
Switch access policy| Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.| `/networks/{networkId}/switch/accessPolicies`| create
Switch access policy| Delete an access policy for a switch network| `/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}`| destroy
Switch access policy| Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.| `/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}`| update
Switch port| Cycle a set of switch ports| `/devices/{serial}/switch/ports`| cycle
Switch port| Update a switch port| `/devices/{serial}/switch/ports/{portId}`| update
Switch port schedule| Update a switch port schedule| `/networks/{networkId}/switch/portSchedules/{portScheduleId}`| update
Switch profile port| Update a switch profile port| `/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}`| update
Switch stacks l3 interface| Create a layer 3 interface for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces`| create
Switch stacks l3 interface| Delete a layer 3 interface from a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}`| destroy
Switch stacks l3 interface| Update a layer 3 interface for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}`| update
Switch stacks l3 interface dhcp| Update a layer 3 interface DHCP configuration for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp`| update
Switch stacks l3 static route| Create a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes`| create
Switch stacks l3 static route| Delete a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| destroy
Switch stacks l3 static route| Update a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| update
Switch warm spare settings| Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.| `/devices/{serial}/switch/warmSpare`| update
Traffic shaping settings| Update the traffic shaping settings rules for an MX network| `/networks/{networkId}/appliance/trafficShaping/rules`| update
Traffic shaping settings| Update the traffic shaping settings for an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules`| update
Uplink selection settings| Update uplink selection settings for an MX network| `/networks/{networkId}/appliance/trafficShaping/uplinkSelection`| update
User access device| Delete a User Access Device| `/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}`| destroy
V1/adaptive policy acl| Creates new adaptive policy ACL| `/organizations/{organizationId}/adaptivePolicy/acls`| create
V1/adaptive policy acl| Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.| `/organizations/{organizationId}/adaptivePolicy/acls/{id}`| destroy
V1/adaptive policy acl| Updates an adaptive policy ACL| `/organizations/{organizationId}/adaptivePolicy/acls/{id}`| update
V1/adaptive policy settings| Update global adaptive policy settings| `/organizations/{organizationId}/adaptivePolicy/settings`| update
VLAN| Add a VLAN| `/networks/{networkId}/appliance/vlans`| create
VLAN| Delete a VLAN from a network| `/networks/{networkId}/appliance/vlans/{vlanId}`| destroy
VLAN| Update a VLAN| `/networks/{networkId}/appliance/vlans/{vlanId}`| update
Vmx| Claim a vMX into a network| `/networks/{networkId}/devices/claim`| claim
Vmx token| Generate a new vMX authentication token| `/devices/{serial}/appliance/vmx/authenticationToken`| create
Warm spare| Swap MX primary and warm spare appliances| `/networks/{networkId}/appliance/warmSpare`| swap
Warm spare| Update MX warm spare settings| `/networks/{networkId}/appliance/warmSpare`| update
Webhook template| Create a webhook payload template for a network| `/networks/{networkId}/webhooks/payloadTemplates`| create
Webhook template| Destroy a webhook payload template for a network. Does not work for included templates ('wpt_00001', 'wpt_00002', 'wpt_00003' or 'wpt_00004')| `/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}`| destroy
Webhook template| Update a webhook payload template for a network| `/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}`| update
Wireless alternate management interface| Update alternate management interface and device static IP| `/networks/{networkId}/wireless/alternateManagementInterface`| update
Wireless l7 firewall| Update the L7 firewall rules of an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules`| update
Wireless settings| Update the wireless settings for a network| `/networks/{networkId}/wireless/settings`| update

