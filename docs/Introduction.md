# Meraki Dashboard APIs

The Meraki Dashboard API (referred to as Meraki API) is a RESTful API interface that allows you to programmatically manage and monitor Meraki networks at scale.

<img src="../images/cloud-code.png" width="200px">


Meraki APIs provide a range of operations to

- Add new organizations, administrators, networks, devices, VLANs, and more
- Configure thousands of networks in minutes
- On-board and Off-board new employees’ teleworker setup automatically, and
- Build custom dashboards for store managers, field technicians, or other unique use cases. 


Checkout out the [Explore](https://developer.cisco.com/meraki/explore/) section for open source projects, or browse the [Marketplace](https://apps.meraki.io/) for partner solutions.

## Resources

A resource is an entity or component within the Meraki ecosystem.  Resources represent the various elements of a network.  Here are some examples of Meraki resources:

- **Organizations**: A collection of networks, representing the top-level structure in the Meraki hierarchy.
- **Networks**: Specific networks within an organization, which contain devices and configurations.
- **Devices**: Individual hardware units such as routers, switches, or access points within a network.
- **VLANs**: Virtual local area networks configured within a network for segmenting traffic.
- **SSIDs**: Wireless network identifiers that can be configured and managed.

Each resource is typically represented by a unique URL. You can use APIs to configure or retrieve information about these resources.

## Services

A service is a functionality or a set of API operations that interact with the resources of a Meraki product. (These operations are specific actions performed on a resource, such as GET, POST, PUT, or DELETE.) Services perform specific actions on resources such as:

- CONFIGURE service: Manage cloud configurations.
- MONITOR service: Return status and history information.
- LIVE TOOL service: Directly interact with devices.

## Meraki Products

A Meraki product refers to the hardware and software solutions offered by Cisco Meraki that are used to build and manage network infrastructure. These products include wireless access points, switches, or security appliances.

## Resource URLs

The resource URL or path contains the name of the Meraki product to reduce ambiguity when working with similar yet unique functionality. 

The format of the path is 'product/service'.

> **Examples of a Path:**
>
> `/appliance/ports`
>
> `/switch/ports`

## Base URI 

A base URI is the root address or endpoint that serves as the starting point for accessing the API's resources. The base URI includes the protocol, domain, and base path. All API requests append specific resource paths to this base URI.

For most regions, the base URI for API requests is `https://api.meraki.com/api/v1`.


Different countries may have different base URIs, see the [respective base URI section](https://developer.cisco.com/meraki/api-v1/getting-started/#base-uri).


## Reference to Open Source Projects and Solutions

Visit the [Explore](https://developer.cisco.com/meraki/explore/) section for open-source projects, or browse the [Marketplace](https://apps.meraki.io/) for partner solutions.
