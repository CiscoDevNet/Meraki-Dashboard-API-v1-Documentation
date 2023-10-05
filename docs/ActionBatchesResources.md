
**Group**|**Summary**|**Resource**|**operation** 
:-------------:|:-------------:|:-------------:|:-------------:
Adaptive policy| Add an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies`| create
Adaptive policy| Delete an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies/{id}`| destroy
Adaptive policy| Update an Adaptive Policy| `/organizations/{organizationId}/adaptivePolicy/policies/{id}`| update
Adaptive policy group| Creates a new adaptive policy group| `/organizations/{organizationId}/adaptivePolicy/groups`| create
Adaptive policy group| Deletes the specified adaptive policy group and any associated policies and references| `/organizations/{organizationId}/adaptivePolicy/groups/{id}`| destroy
Adaptive policy group| Updates an adaptive policy group. If updating "Infrastructure", only the SGT is allowed. Cannot update "Unknown".| `/organizations/{organizationId}/adaptivePolicy/groups/{id}`| update
Adaptive policy settings| Update global adaptive policy settings| `/organizations/{organizationId}/adaptivePolicy/settings`| update
Alternate management interface| Update the switch alternate management interface for the network| `/networks/{networkId}/switch/alternateManagementInterface`| update
Appliance radio settings| Update the radio settings of an appliance| `/devices/{serial}/appliance/radio/settings`| update
Appliance ssid| Update the attributes of an MX SSID| `/networks/{networkId}/appliance/ssids/{number}`| update
Bgp settings| Update a Hub BGP Configuration| `/networks/{networkId}/appliance/vpn/bgp`| update
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
Dai trusted server| Add a server to be trusted by Dynamic ARP Inspection on this network| `/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers`| create
Dai trusted server| Remove a server from being trusted by Dynamic ARP Inspection on this network| `/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}`| destroy
Dai trusted server| Update a server that is trusted by Dynamic ARP Inspection on this network| `/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}`| update
Dash xl/dashboard branding policy| Add a new branding policy to an organization| `/organizations/{organizationId}/brandingPolicies`| create
Dash xl/dashboard branding policy| Delete a branding policy| `/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}`| destroy
Dash xl/dashboard branding policy| Update a branding policy| `/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}`| update
Dash xl/dashboard branding policy priorities| Update the priority ordering of an organization's branding policies.| `/organizations/{organizationId}/brandingPolicies/priorities`| update
Device| Update the attributes of a device| `/devices/{serial}`| update
Device| Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)| `/networks/{networkId}/devices`| claim
Device| Remove a single device| `/networks/{networkId}/devices`| remove
Dhcp server policy| Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively| `/networks/{networkId}/switch/dhcpServerPolicy`| update
Dscp cos mapping| Update the DSCP to CoS mappings| `/networks/{networkId}/switch/dscpToCosMappings`| update
Eap override| Update the EAP overridden parameters for an SSID.| `/networks/{networkId}/wireless/ssids/{number}/eapOverride`| update
End users/actions/meraki auth user| Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)| `/networks/{networkId}/merakiAuthUsers`| create
End users/actions/meraki auth user| Delete an 802.1X RADIUS user, or deauthorize and optionally delete a splash guest or client VPN user.| `/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}`| destroy
End users/actions/meraki auth user| Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)| `/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}`| update
Feature opt in| Update an early access feature opt-in for an organization| `/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}`| update
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
Monitored media server| Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers`| create
Monitored media server| Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| destroy
Monitored media server| Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| update
Mqtt broker| Add an MQTT broker| `/networks/{networkId}/mqttBrokers`| create
Mqtt broker| Delete an MQTT broker| `/networks/{networkId}/mqttBrokers/{mqttBrokerId}`| destroy
Mqtt broker| Update an MQTT broker| `/networks/{networkId}/mqttBrokers/{mqttBrokerId}`| update
Mr/actions/ap port profile| Create an AP port profile| `/networks/{networkId}/wireless/ethernet/ports/profiles`| create
Mr/actions/ap port profile| Delete an AP port profile| `/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}`| destroy
Mr/actions/ap port profile| Update the AP port profile by ID for this network| `/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}`| update
Mr/actions/ap port profile assign| Assign AP port profile to list of APs| `/networks/{networkId}/wireless/ethernet/ports/profiles`| aps
Mr/actions/ap port profile set| Set the AP port profile to be default for this network| `/networks/{networkId}/wireless/ethernet/ports/profiles`| default
Mr/actions/wireless alternate management interface v6| Update alternate management interface IPv6 address| `/devices/{serial}/wireless/alternateManagementInterface/ipv6`| update
Ms/actions/switch| Update switch network settings| `/networks/{networkId}/switch/settings`| settings/update
Mt/api/actions/alert profiles| Creates a sensor alert profile for a network.| `/networks/{networkId}/sensor/alerts/profiles`| create
Mt/api/actions/alert profiles| Deletes a sensor alert profile from a network.| `/networks/{networkId}/sensor/alerts/profiles/{id}`| destroy
Mt/api/actions/alert profiles| Updates a sensor alert profile for a network.| `/networks/{networkId}/sensor/alerts/profiles/{id}`| update
Mt/api/actions/sensor mqtt broker| Update the sensor settings of an MQTT broker. To update the broker itself, use /networks/{networkId}/mqttBrokers/{mqttBrokerId}.| `/networks/{networkId}/sensor/mqttBrokers/{mqttBrokerId}`| update
Multicast| Update multicast settings for a network| `/networks/{networkId}/switch/routing/multicast`| update
Network| Bind a network to a template.| `/networks/{networkId}`| bind
Network| Delete a network| `/networks/{networkId}`| destroy
Network| Split a combined network into individual networks for each type of device| `/networks/{networkId}`| split
Network| Unbind a network from a template.| `/networks/{networkId}`| unbind
Network| Update a network| `/networks/{networkId}`| update
Network| Combine multiple networks into a single network| `/organizations/{organizationId}/networks`| combine
Network| Create a network| `/organizations/{organizationId}/networks`| create
Network appliance settings| Update the appliance settings for a network| `/networks/{networkId}/appliance/settings`| update
Network settings| Update the settings for a network| `/networks/{networkId}/settings`| update
Org wide alerts/alert config| Create an organization-wide alert configuration| `/organizations/{organizationId}/alerts/profiles`| create
Org wide alerts/alert config| Removes an organization-wide alert config| `/organizations/{organizationId}/alerts/profiles/{alertConfigId}`| destroy
Org wide alerts/alert config| Update an organization-wide alert config| `/organizations/{organizationId}/alerts/profiles/{alertConfigId}`| update
Organization SAML IdP| Create a SAML IdP for your organization.| `/organizations/{organizationId}/saml/idps`| create
Organization SAML IdP| Remove a SAML IdP in your organization.| `/organizations/{organizationId}/saml/idps/{idpId}`| destroy
Organization SAML IdP| Update a SAML IdP in your organization| `/organizations/{organizationId}/saml/idps/{idpId}`| update
Organization login security settings| Update the login security settings for an organization| `/organizations/{organizationId}/loginSecurity`| update
Ospf routing| Update layer 3 OSPF routing configuration| `/networks/{networkId}/switch/routing/ospf`| update
Policy object| Creates a new Policy Object.| `/organizations/{organizationId}/policyObjects`| create
Policy object| Deletes a Policy Object.| `/organizations/{organizationId}/policyObjects/{policyObjectId}`| destroy
Policy object| Updates a Policy Object.| `/organizations/{organizationId}/policyObjects/{policyObjectId}`| update
Policy object group| Creates a new Policy Object Group.| `/organizations/{organizationId}/policyObjects/groups`| create
Policy object group| Deletes a Policy Object Group.| `/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}`| destroy
Policy object group| Updates a Policy Object Group.| `/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}`| update
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
Sensor gateway role| Assign one or more sensor roles to a given sensor or camera device.| `/devices/{serial}/sensor/relationships`| update
Single lan| Update single LAN configuration| `/networks/{networkId}/appliance/singleLan`| update
Site to site vpn| Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.| `/networks/{networkId}/appliance/vpn/siteToSiteVpn`| update
Ssid| Update the attributes of an MR SSID| `/networks/{networkId}/wireless/ssids/{number}`| update
Ssid bonjour forwarding| Update the bonjour forwarding setting and rules for the SSID| `/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding`| update
Ssid device type group policies| Update the device type group policies for the SSID| `/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies`| update
Ssid outage schedule| Update the outage schedule for the SSID| `/networks/{networkId}/wireless/ssids/{number}/schedules`| update
Ssid splash settings| Modify the splash page settings for the given SSID| `/networks/{networkId}/wireless/ssids/{number}/splash/settings`| update
Ssid vpn| Update the VPN settings for the SSID| `/networks/{networkId}/wireless/ssids/{number}/vpn`| update
Staged upgrade/group| Create a Staged Upgrade Group for a network| `/networks/{networkId}/firmwareUpgrades/staged/groups`| create
Staged upgrade/group| Delete a Staged Upgrade Group| `/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}`| destroy
Static delegated prefix| Add a static delegated prefix from a network| `/networks/{networkId}/appliance/prefixes/delegated/statics`| create
Static delegated prefix| Delete a static delegated prefix from a network| `/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}`| destroy
Static delegated prefix| Update a static delegated prefix from a network| `/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}`| update
Storm control| Update the storm control configuration for a switch network| `/networks/{networkId}/switch/stormControl`| update
Switch| Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring| `/organizations/{organizationId}/switch/devices`| clone
Switch access policy| Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.| `/networks/{networkId}/switch/accessPolicies`| create
Switch access policy| Delete an access policy for a switch network| `/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}`| destroy
Switch access policy| Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.| `/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}`| update
Switch port| Cycle a set of switch ports| `/devices/{serial}/switch/ports`| cycle
Switch port| Update a switch port| `/devices/{serial}/switch/ports/{portId}`| update
Switch port schedule| Update a switch port schedule| `/networks/{networkId}/switch/portSchedules/{portScheduleId}`| update
Switch profile port| Update a switch template port| `/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}`| update
Switch stacks l3 interface| Create a layer 3 interface for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces`| create
Switch stacks l3 interface| Delete a layer 3 interface from a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}`| destroy
Switch stacks l3 interface| Update a layer 3 interface for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}`| update
Switch stacks l3 interface dhcp| Update a layer 3 interface DHCP configuration for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp`| update
Switch stacks l3 static route| Create a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes`| create
Switch stacks l3 static route| Delete a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| destroy
Switch stacks l3 static route| Update a layer 3 static route for a switch stack| `/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| update
Switch warm spare settings| Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.| `/devices/{serial}/switch/warmSpare`| update
Traffic shaping settings| Update the traffic shaping settings rules for an MX network| `/networks/{networkId}/appliance/trafficShaping/rules`| update
Traffic shaping settings| Update the traffic shaping rules for an SSID on an MR network.| `/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules`| update
Uplink selection settings| Update uplink selection settings for an MX network| `/networks/{networkId}/appliance/trafficShaping/uplinkSelection`| update
User access device| Delete a User Access Device| `/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}`| destroy
V1/adaptive policy acl| Creates new adaptive policy ACL| `/organizations/{organizationId}/adaptivePolicy/acls`| create
V1/adaptive policy acl| Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.| `/organizations/{organizationId}/adaptivePolicy/acls/{aclId}`| destroy
V1/adaptive policy acl| Updates an adaptive policy ACL| `/organizations/{organizationId}/adaptivePolicy/acls/{aclId}`| update
VLAN| Add a VLAN| `/networks/{networkId}/appliance/vlans`| create
VLAN| Delete a VLAN from a network| `/networks/{networkId}/appliance/vlans/{vlanId}`| destroy
VLAN| Update a VLAN| `/networks/{networkId}/appliance/vlans/{vlanId}`| update
VLAN profile| Create a VLAN profile for a network| `/networks/{networkId}/vlanProfiles`| create
VLAN profile| Delete a VLAN profile of a network| `/networks/{networkId}/vlanProfiles/{iname}`| destroy
Vmx| Claim a vMX into a network| `/networks/{networkId}/devices/claim`| claim
Vmx token| Generate a new vMX authentication token| `/devices/{serial}/appliance/vmx/authenticationToken`| create
Warm spare| Swap MX primary and warm spare appliances| `/networks/{networkId}/appliance/warmSpare`| swap
Warm spare| Update MX warm spare settings| `/networks/{networkId}/appliance/warmSpare`| update
Webhook template| Create a webhook payload template for a network| `/networks/{networkId}/webhooks/payloadTemplates`| create
Webhook template| Destroy a webhook payload template for a network. Does not work for included templates ('wpt_00001', 'wpt_00002', 'wpt_00003', 'wpt_00004', 'wpt_00005' or 'wpt_00006')| `/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}`| destroy
Webhook template| Update a webhook payload template for a network| `/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}`| update
Wired/actions/vpn exclusions| Update VPN exclusion rules for an MX network.| `/networks/{networkId}/appliance/trafficShaping/vpnExclusions`| update
Wired/appliance RF profile| Creates new RF profile for this network| `/networks/{networkId}/appliance/rfProfiles`| create
Wired/appliance RF profile| Delete a RF Profile| `/networks/{networkId}/appliance/rfProfiles/{rfProfileId}`| destroy
Wired/appliance RF profile| Updates specified RF profile for this network| `/networks/{networkId}/appliance/rfProfiles/{rfProfileId}`| update
Wired/uplinks/settings| Update the uplink settings for an MX appliance| `/devices/{serial}/appliance/uplinks/settings`| update
Wired/vpn/third party vpn peers| Update the third party VPN peers for an organization| `/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers`| update
Wireless alternate management interface| Update alternate management interface and device static IP| `/networks/{networkId}/wireless/alternateManagementInterface`| update
Wireless l7 firewall| Update the L7 firewall rules of an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules`| update
Wireless settings| Update the wireless settings for a network| `/networks/{networkId}/wireless/settings`| update

