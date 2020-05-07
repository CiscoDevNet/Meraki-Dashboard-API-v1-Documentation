
**Group**|**Summary**|**Resource**|**operation** 
:-------------:|:-------------:|:-------------:|:-------------:
Bluetooth device setting| Update the bluetooth settings for a wireless device| `/devices/{serial}/wireless/bluetooth/settings`| update
Camera video settings| Update video settings for the given camera| `/devices/{serial}/camera/video/settings`| update
Cellular gateway connectivity monitoring destination| Update the connectivity testing destinations for an MG network| `/networks/{networkId}/cellularGateway/settings/connectivityMonitoringDestinations`| update
Cellular gateway device lan| Update the LAN Settings for a single MG.| `/devices/{serial}/cellularGateway/settings`| update
Cellular gateway dhcp setting| Update common DHCP settings of MGs| `/networks/{networkId}/cellularGateway/settings/dhcp`| update
Cellular gateway port forwarding rules| Updates the port forwarding rules for a single MG.| `/devices/{serial}/cellularGateway/settings/portForwardingRules`| update
Cellular gateway subnet pool| Update the subnet pool and mask configuration for MGs in the network.| `/networks/{networkId}/cellularGateway/settings/subnetPool`| update
Cellular gateway uplink setting| Updates the uplink settings for your MG network.| `/networks/{networkId}/cellularGateway/settings/uplink`| update
Device| Claim devices into a network| `/networks/{networkId}/devices`| claim
Device| Remove a single device| `/networks/{networkId}/devices/{serial}`| remove
Device| Update the attributes of a device| `/networks/{networkId}/devices/{serial}`| update
Dhcp server policy| Update the DHCP server policy| `/networks/{networkId}/switch/settings/dhcpServerPolicy`| update
Dscp cos mapping| Update the DSCP to CoS mappings| `/networks/{networkId}/switch/settings/dscpToCosMappings`| update
Floor plan| Destroy a floor plan| `/networks/{networkId}/floorPlans/{floorPlanId}`| destroy
Floor plan| Update a floor plan's geolocation and other meta data| `/networks/{networkId}/floorPlans/{floorPlanId}`| update
Group policy| Delete a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| destroy
Group policy| Update a group policy| `/networks/{networkId}/groupPolicies/{groupPolicyId}`| update
Group policy| Create a group policy| `/networks/{networkId}/groupPolicies`| create
License| Move licenses to another organization. This will also move any devices that the licenses are assigned to| `/organizations/{organizationId}/licenses`| move
License| Assign SM seats to a network. This will increase the managed SM device limit of the network| `/organizations/{organizationId}/licenses`| assignSeats
License| Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license| `/organizations/{organizationId}/licenses`| renewSeats
License| Update a license| `/organizations/{organizationId}/licenses/{licenseId}`| update
License| Move SM seats to another organization| `/organizations/{organizationId}/licenses`| moveSeats
Link aggregation| Split a link aggregation group into separate ports| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| destroy
Link aggregation| Update a link aggregation group| `/networks/{networkId}/switch/linkAggregations/{linkAggregationId}`| update
Link aggregation| Create a link aggregation group| `/networks/{networkId}/switch/linkAggregations`| create
MTU configuration| Update the MTU configuration| `/networks/{networkId}/switch/settings/mtu`| update
MX connectivity monitoring destination| Update the connectivity testing destinations for an MX network| `/networks/{networkId}/connectivityMonitoringDestinations`| update
MX l7 firewall| Update the MX L7 firewall rules for an MX network| `/networks/{networkId}/l7FirewallRules`| update
MX port| Update the per-port VLAN settings for a single MX port.| `/networks/{networkId}/appliancePorts/{appliancePortId}`| update
MX uplink setting| Updates the uplink settings for your MX network.| `/networks/{networkId}/uplinkSettings`| update
Management interface settings| Update the management interface settings for a device| `/networks/{networkId}/devices/{serial}/managementInterfaceSettings`| update
Monitored media server| Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers`| create
Monitored media server| Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| destroy
Monitored media server| Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.| `/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}`| update
Multicast| Update multicast settings for a network| `/networks/{networkId}/switch/settings/multicast`| update
Network| Delete a network| `/networks/{networkId}`| destroy
Network| Update a network| `/networks/{networkId}`| update
Network| Combine multiple networks into a single network| `/organizations/{organizationId}/networks`| combine
Network| Create a network| `/organizations/{organizationId}/networks`| create
Network| Split a combined network into individual networks for each type of device| `/networks/{networkId}`| split
Qos rule| Update the order in which the rules should be processed by the switch| `/networks/{networkId}/switch/settings/qosRules/order`| update_order
Qos rule| Add a quality of service rule| `/networks/{networkId}/switch/settings/qosRules`| create
Qos rule| Update a quality of service rule| `/networks/{networkId}/switch/settings/qosRules/{qosRuleId}`| update
Qos rule| Delete a quality of service rule| `/networks/{networkId}/switch/settings/qosRules/{qosRuleId}`| destroy
Quality and retention setting| Update quality and retention settings for the given camera| `/devices/{serial}/camera/qualityAndRetentionSettings`| update
RF profile| Creates new RF profile for this network| `/networks/{networkId}/wireless/rfProfiles`| create
RF profile| Delete a RF Profile| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| destroy
RF profile| Updates specified RF profile for this network| `/networks/{networkId}/wireless/rfProfiles/{rfProfileId}`| update
Radio settings| Update the radio settings of a device| `/networks/{networkId}/devices/{serial}/wireless/radioSettings`| update
STP configuration| Updates STP settings| `/networks/{networkId}/switch/settings/stp`| update
Site to site vpn| Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.| `/networks/{networkId}/siteToSiteVpn`| update
Ssid| Update the attributes of an SSID| `/networks/{networkId}/ssids/{number}`| update
Storm control| Update the storm control configuration for a switch network| `/networks/{networkId}/switch/settings/stormControl`| update
Switch port| Cycle a set of switch ports| `/devices/{serial}/switch/ports`| cycle
Switch port| Update a switch port| `/devices/{serial}/switchPorts/{number}`| update
Switch port schedule| Update a switch port schedule| `/networks/{networkId}/switch/portSchedules/{portScheduleId}`| update
Traffic shaping settings| Update the traffic shaping settings for an SSID on an MR network| `/networks/{networkId}/ssids/{number}/trafficShaping`| update
Traffic shaping settings| Update the traffic shaping settings for an MX network| `/networks/{networkId}/trafficShaping`| update
VLAN| Add a VLAN| `/networks/{networkId}/vlans`| create
VLAN| Delete a VLAN from a network| `/networks/{networkId}/vlans/{vlanId}`| destroy
VLAN| Update a VLAN| `/networks/{networkId}/vlans/{vlanId}`| update
Warm spare| Swap MX primary and warm spare appliances| `/networks/{networkId}/swapWarmSpare`| swap
Warm spare| Update MX warm spare settings| `/networks/{networkId}/warmSpareSettings`| update
Wireless settings| Update the wireless settings for a network| `/networks/{networkId}/wireless/settings`| update
