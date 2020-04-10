# Meraki Dashboard API

A RESTful API to programmatically manage and monitor Meraki networks at scale.

<img src="../images/cloud-code.png" width="200px">

## What's New in v1 

The Dashboard API has evolved significantly, providing hundreds of endpoints to manage your Meraki networks. With this growth, it started to become challenging to find resources quickly. Meraki prides itself on simplicity and to that end, the API has been restructured to provide a more intuitive experience for working with the API. 

In addition, several improvements and new endpoints have been included with this major release.

## Highlights

- The API documentation and complimenting Postman Collection, will structure the API based on General and Product service groups, which will contain the related resources.

```
General
    devices
    networks
    organizations
Products
    appliance
    camera
    switch
    wireless
    ...
```

- Each product or scope will have a **CONFIGURE** and/or **MONITOR** folder, to indicate the types of endpoints that are available and the permissions likely required. 

```
Products
    appliance
        CONFIGURE
            firewall
              
        MONITOR
            performance
            

```


- The endpoint URL paths will always contain the Meraki product, reducing ambiquity when working with resources. 

    *Examples*

    `/appliance/ports`

    `/switch/ports`



- Authorization has been adjusted to use industry standard Bearer headers. 

    *New header*

    ```json
    {
        "Authorization": Bearer <Meraki_API_Key>
    }
    ```

See the [Changelog](https://developer.cisco.com/meraki/whats-new/#!v1-0-0-beta-0) for all the details.



## What can the Dashboard API be used for?

- Add new organizations, admins, networks, devices, VLANs, and more
- Configure thousands of networks in minutes
- On-board and off-board new employees’ teleworker setup automatically
- Build your own dashboard for store managers, field techs, or unique use cases

Checkout out the [Explore](https://developer.cisco.com/meraki/explore/) section for open source projects, or browse the [Marketplace](https://apps.meraki.io/) for partner solutions.