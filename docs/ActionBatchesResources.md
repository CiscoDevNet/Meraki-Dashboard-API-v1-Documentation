
**Group**|**Summary**|**Resource**|**operation** 
:-------------:|:-------------:|:-------------:|:-------------:
Bluetooth device setting| Update the bluetooth settings for a wireless device| `/devices/{serial}/wireless/bluetooth/settings`| update
Camera video settings| Update video settings for the given camera| `/devices/{serial}/camera/video/settings`| update
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
Device| Claim devices into a network| `/networks/{networkId}/devices`| claim
Device| Remove a single device| `/networks/{networkId}/devices`| remove
Dhcp server policy| Update the DHCP server policy| `/networks/{networkId}/switch/dhcpServerPolicy`| update
Dscp cos mapping| Update the DSCP to CoS mappings| `/networks/{networkId}/switch/dscpToCosMappings`| update
Floor plan| Destroy a floor plan| `/networks/{networkId}/floorPlans/{floorPlanId}`| destroy
Floor plan| Update a floor plan's geolocation and other meta data| `/networks/{networkId}/floorPlans/{floorPlanId}`| update
Group policy| Create a group policy| `/networks/{networkId}/groupPolicies`| create
Group policy| Delete a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| destroy
Group policy| Update a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| update
L3 interface| Delete a layer 3 interface from the switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}`| destroy
L3 interface| Create a layer 3 interface for a switch| `/devices/{serial}/switch/routing/interfaces`| create
L3 interface| Update a layer 3 interface for a switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}`| update
L3 interface dhcp| Update a layer 3 interface DHCP configuration for a switch| `/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp`| update
L3 static route| Delete a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}`| destroy
L3 static route| Create a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes`| create
L3 static route| Update a layer 3 static route for a switch| `/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}`| update
License| Assign SM seats to a network. This will increase the managed SM device limit of the network| `/organizations/{organizationId}/licenses`| assignSeats
License| Move licenses to another organization. This will also move any devices that the licenses are assigned to| `/organizations/{organizationId}/licenses`| move
License| Move SM seats to another organization| `/organizations/{organizationId}/licenses`| moveSeats
License| Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license| `/organizations/{organizationId}/licenses`| renewSeats
License| Update a license| `/organizations/{organizationId}/licenses/{licenseId}`| update
Link aggregation| Split a link aggregation group into separate ports| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| destroy
Link aggregation| Update a link aggregation group| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| update
Link aggregation| Create a link aggregation group| `/networks/{networkId}/switch/linkAggregations`| create
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
Multicast| Update multicast settings for a network| `/networks/{networkId}/switch/routing/multicast`| update
Network| Delete a network| `/networks/{networkId}`| destroy
Network| Update a network| `/networks/{networkId}`| update
Network| Combine multiple networks into a single network| `/organizations/{organizationId}/networks`| combine
Network| Create a network| `/organizations/{organizationId}/networks`| create
Network| Split a combined network into individual networks for each type of device| `/networks/{networkId}`| split
Network settings| Update the settings for a network| `/networks/{networkId}/settings`| update
Organization SAML IdP| Create a SAML IdP for your organization.| `/organizations/{organizationId}/saml/idps`| create
Organization SAML IdP| Update a SAML IdP in your organization| `/organizations/{organizationId}/saml/idps/{idpId}`| update
Organization SAML IdP| Remove a SAML IdP in your organization.| `/organizations/{organizationId}/saml/idps/{idpId}`| destroy
Psk group| Create an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks`| create
Psk group| Delete an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}`| destroy
Psk group| Update an Identity PSK| `/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}`| update
Qos rule| Update the order in which the rules should be processed by the switch| `/networks/{networkId}/switch/qosRules/order`| update_order
Qos rule| Delete a quality of service rule| `/networks/{networkId}/switch/qosRules/{qosRuleId}`| destroy
Qos rule| Add a quality of service rule| `/networks/{networkId}/switch/qosRules`| create
Qos rule| Update a quality of service rule| `/networks/{networkId}/switch/qosRules/{qosRuleId}`| update
Quality and retention setting| Update quality and retention settings for the given camera| `/devices/{serial}/camera/qualityAndRetention`| update
RF profile| Creates new RF profile for this network| `/networks/{networkId}/wireless/rfProfiles`| create
RF profile| Delete a RF Profile| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| destroy
RF profile| Updates specified RF profile for this network| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| update
Radio settings| Update the radio settings of a device| `/devices/{serial}/wireless/radio/settings`| update
STP configuration| Updates STP settings| `/networks/{networkId}/switch/stp`| update
Sense setting| Update sense settings for the given camera| `/devices/{serial}/camera/sense`| update
Single lan| Update single LAN configuration| `/networks/{networkId}/appliance/singleLan`| update
Site to site vpn| Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.| `/networks/{networkId}/appliance/vpn/siteToSiteVpn`| update
Ssid| Update the attributes of an SSID| `/networks/{networkId}/wireless/ssids/{number}`| update
Storm control| Update the storm control configuration for a switch network| `/networks/{networkId}/switch/stormControl`| update
Switch port| Cycle a set of switch ports| `/devices/{serial}/switch/ports`| cycle
Switch port| Update a switch port| `/devices/{serial}/switch/ports/{portId}`| update
Switch port schedule| Update a switch port schedule| `/networks/{networkId}/switch/portSchedules/{portScheduleId}`| update
Switch profile port| Update a switch profile port| `/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}`| update
Switch stacks l3 interface| Create a layer 3 interface for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/interfaces`| create
Switch stacks l3 interface| Delete a layer 3 interface from a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/interfaces/{interfaceId}`| destroy
Switch stacks l3 interface| Update a layer 3 interface for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/interfaces/{interfaceId}`| update
Switch stacks l3 interface dhcp| Update a layer 3 interface DHCP configuration for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp`| update
Switch stacks l3 static route| Create a layer 3 static route for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/staticRoutes`| create
Switch stacks l3 static route| Delete a layer 3 static route for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| destroy
Switch stacks l3 static route| Update a layer 3 static route for a switch stack| `/networks/{networkId}/switch/switchStacks/{switchStackId}/routing/staticRoutes/{staticRouteId}`| update
Traffic shaping settings| Update the traffic shaping settings for an MX network| `/networks/{networkId}/appliance/trafficShaping/rules`| update
Traffic shaping settings| Update the traffic shaping settings for an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules`| update
Uplink selection settings| Update uplink selection settings for an MX network| `/networks/{networkId}/appliance/trafficShaping/uplinkSelection`| update
VLAN| Add a VLAN| `/networks/{networkId}/appliance/vlans`| create
VLAN| Delete a VLAN from a network| `/networks/{networkId}/appliance/vlans/{vlanId}`| destroy
VLAN| Update a VLAN| `/networks/{networkId}/appliance/vlans/{vlanId}`| update
Warm spare| Swap MX primary and warm spare appliances| `/networks/{networkId}/appliance/warmSpare`| swap
Warm spare| Update MX warm spare settings| `/networks/{networkId}/appliance/warmSpare`| update
Wireless alternate management interface| Update alternate management interface and device static IP| `/networks/{networkId}/wireless/alternateManagementInterface`| update
Wireless l7 firewall| Update the L7 firewall rules of an SSID on an MR network| `/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules`| update
Wireless settings| Update the wireless settings for a network| `/networks/{networkId}/wireless/settings`| update
