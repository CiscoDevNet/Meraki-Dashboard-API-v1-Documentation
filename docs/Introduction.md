# Meraki Dashboard API

A RESTful API to programmatically manage and monitor Meraki networks at scale.

<img src="../images/cloud-code.png" width="200px">

## What can you do with it?

- Add new organizations, admins, networks, devices, VLANs, and more
- Configure thousands of networks in minutes
- On-board and off-board new employees’ teleworker setup automatically
- Build your own dashboard for store managers, field techs, or unique use cases

Checkout out the [Explore](https://developer.cisco.com/meraki/explore/) section for open source projects, or browse the [Marketplace](https://apps.meraki.io/) for partner solutions.

## What's New in v1 

The Dashboard API has evolved significantly, providing hundreds of endpoints to manage your Meraki networks!

We want to do so much more. But in order for us to include many of these new features or improvements, we need to break a few things. 

The focus of this **major** version is on **Simplicity** and **Scale**, by providing an enjoyable developer experience. 

The API documentation, Postman collection, and Python library will remain synced and up-to-date with improved navigation and features.

In addition, several improvements and new endpoints have been included with this major release.


### API Documentation

The API Endpoint documentation and complimenting Postman Collection have a new folder structure for navigating the API. 



#### Categories

The services are grouped into categories, providing a collection of endpoints that behave in a similar way. 

**CONFIGURE** endpoints  are for managing cloud configurations

**MONITOR** endpoints will return status and history information

**LIVE TOOL** endpoints will directly interact with the device

### Resource Path changes

The endpoint URL paths will always contain the Meraki product if required, reducing ambiguity when working with resources that have similar yet unique functionality. 

> **Examples of a product and service**
>
> `/appliance/ports`
>
> `/switch/ports`

### Base URI

In most parts of the world, every API request will begin with the following **base URI**: 

> `https://api.meraki.com/api/v1`

For organizations hosted in different country dashboards, please refer to their [respective base URI](https://developer.cisco.com/meraki/api-v1/getting-started/#base-uri)

### See all the changes

Visit the [Changelog](https://developer.cisco.com/meraki/whats-new/#!v1-0-0-beta-0) for all the details.

### SDKs

Going forward, the custom Meraki [Python library](pythonLibrary.md) will be the recommended SDK for simplified API scripting. The previously auto-generated Python, Node.js, and Ruby SDKs for **v0** will remain in the Meraki GitHub but will no longer be maintained. 

#### Python

The Meraki [Python Library](pythonLibrary.md) has been updated to take advantage of all the new API enhancements plus many custom features to help both beginners and experienced programmers.
