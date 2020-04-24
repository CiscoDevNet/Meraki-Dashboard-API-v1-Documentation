# Path Schema

The Meraki API resources are organized by scope, and then by the product and its related service groups.

`baseURI/scope/:id/product/serviceGroup/:id/service/:id`

## Base URI

Every API endpoint will begin with the following URL to the Meraki cloud. 

> `https://api.meraki.com/api/v1`

## Scopes

The API mirrors the structure of the Meraki Dashboard.

 **Organizations** consist of **Networks**, which then contain **Devices**. 

![](../images/Meraki_OrgNetDevice_structure_300x370.png)

## Service Groups

Each Meraki product and scope will then have relative services which will be grouped together

`/appliance/firewall/`


## Examples

**Resource**

`/networks/L_646829496481100388/appliance/firewall/l3FirewallRules`

**URL**

`https://api.meraki.com/api/v1/networks/L_646829496481100388/appliance/firewall/l3FirewallRules`

**cURL**

```bash
curl -LX GET 'https://api.meraki.com/api/v1/networks/L_646829496481100388/appliance/firewall/l3FirewallRules' \
--header 'Authorization: Bearer 093b24e85df15a3e66f1fc359f4c48493eaa1b73'
```