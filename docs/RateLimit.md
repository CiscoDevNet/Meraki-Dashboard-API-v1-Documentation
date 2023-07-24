# Call budgets

## Purpose and importance

API call budgets define the number of API calls that an API client can make in a given amount of time and are a safeguard against runaway applications and malicious behavior. Call budgets (or rate limits) are a standard feature of high performance APIs across industries and working within the provided call budget is table stakes for any developer building an application that consumes the API. The best practice is for applications manage API call budgets effectively and avoid making API calls in excess of the limit.

## Per organization

Each Meraki organization has a call budget of **10 requests per second**, regardless of the number of API applications interacting with that organization.
* A burst of 10 additional requests are allowed in the first second, yielding a maximum of 30 requests in the first 2 seconds.
* The rate limiting technique is based off of the [token bucket model](https://en.wikipedia.org/wiki/Token_bucket).

This budget is shared across all API applications in the organization that leverage [API authentication](https://developer.cisco.com/meraki/api-v1/authorization/). You can [check the recent API activity](https://developer.cisco.com/meraki/api-v1/get-organization-api-requests-overview-response-codes-by-interval/) for the given organization to understand if you are sharing the budget with other applications.

## Per source IP address

Each source IP address making API requests has a call budget of **100 requests per second**, regardless of the number of API clients working from that IP address.

## Response codes

* A `429` status code will be returned when the rate limit has been exceeded, with the `Retry-After` header.
* When an application exceeds the rate limit, the following message will be returned in the response body:

```JSON
{
    "errors": [
        "API rate limit exceeded for organization"
    ]
}
```

## Best practices and tips for managing call budgets

### Handle limiting gracefully

If the defined budget is exceeded, the dashboard API will reply with the `429` (rate limit exceeded) error code. This response also returns a `Retry-After` header indicating how long the client should wait before making a follow-up request. Ensure that appropriate action is being taken to handle `429` responses if you incur them. Utilize the `Retry-After` header and backoff to minimize compounded rate limit issues.

* The `Retry-After` header contains the number of seconds the client should wait.
* Expect to backoff for 1 - 2 seconds if the limit has been exceeded. You may have to wait potentially longer if a large number of requests were made within this timeframe.

If you are using Python, [the official Meraki Python library](https://github.com/meraki/dashboard-api-python) handles retries and automatic backoff for you so you can focus elsewhere in your application.​

A simple Python script example which minimizes rate limit errors:

```Python
response = requests.request("GET", url, headers=headers)
​
if response.status_code == 200:
    # Success logic
elif response.status_code == 429:
    time.sleep(int(response.headers["Retry-After"]))
else:
    # Handle other response codes
```

### Monitoring

Strategize your data polling. The most common cause of `429` responses is unnecessarily frequent polling of information that changes infrequently after day 1 of a network deployment, such as the list of [networks](https://developer.cisco.com/meraki/api-v1/get-organization-networks/) or [policy objects](https://developer.cisco.com/meraki/api-v1/get-organization-policy-objects/) in an organization.

### Use the most efficient endpoints for your use case

evelop your application using the most efficient API calls available for your use case, especially if your application provides monitoring features. 

#### Examples

##### Retrieving network topology information including LLDP/CDP

Call the network-wide [getNetworkTopologyLinkLayer](https://developer.cisco.com/meraki/api-v1/get-network-topology-link-layer/), which provides the complete topology for the network, instead of the less efficient single-device endpoint [getDeviceLldpCdp](https://developer.cisco.com/meraki/api-v1/get-device-lldp-cdp/).

##### Retrieving device uplink information (IP addressing)

Call the organization-wide [getOrganizationDevicesUplinksAddressesByDevice](https://developer.cisco.com/meraki/api-v1/get-organization-devices-uplinks-addresses-by-device/) instead of looking for IP information in per-device endpoints.

##### Retrieving device hardware details

Call the organization-wide [getOrganizationDevices](https://developer.cisco.com/meraki/api-v1/get-organization-devices/), which provides the information for hundreds devices at a time in a paginated list, instead of the less efficient single-device endpoint [getDevice](https://developer.cisco.com/meraki/api-v1/get-device/) or the network-wide endpoint [getNetworkDevices](https://developer.cisco.com/meraki/api-v1/get-network-devices/).

##### Monitoring device availability (status)

Call the organization-wide [getOrganizationDevicesAvailabilitiesChangeHistory](https://community.meraki.com/t5/Developers-APIs/Now-GA-Device-Availability-Change-History/m-p/202186#M8657) to catch up on availability (status) changes since your last org-wide poll of [getOrganizationDevicesAvailabilities](https://developer.cisco.com/meraki/api-v1/get-organization-devices-availabilities/) or [getOrganizationDevicesStatuses](https://developer.cisco.com/meraki/api-v1/get-organization-devices-statuses/), rather than re-polling the information for all devices all over again.

##### Retrieving network clients

Call the network-wide API call [getNetworkClients](https://developer.cisco.com/meraki/api-v1/get-network-clients/) once for the network, instead of calling the less efficient single-device API endpoint [getDeviceClients](https://developer.cisco.com/meraki/api-v1/get-device-clients/).

### Provisioning

#### Use action batches

[**Action Batches**](https://developer.cisco.com/meraki/api-v1/action-batches-overview/#action-batches) are a perfect tool for submitting batched configuration requests in a single synchronous or asynchronous transaction. Leverage them for bulk constructive/destructive operations (`POST`, `PUT`, `DELETE`). To read more about Action Batches, visit [our overview](https://developer.cisco.com/meraki/api-v1/action-batches-overview/#action-batches), the [GitHub Demo](https://developer.cisco.com/codeexchange/github/repo/shiyuechengineer/action-batches/), or the [Meraki Blog](https://meraki.cisco.com/blog/2019/06/action-batches-a-recipe-for-success/).

#### Configuration sync and "golden template" enforcement

Once you are confident that an organization is configured correctly, leverage [getOrganizationConfiguarationChanges](https://developer.cisco.com/meraki/api-v1/get-organization-configuration-changes/) to identify deviations from the last known intended configuration. This is more efficient than re-polling every configuration setting and then running diffs in your application.

#### Use configuration templates

[Meraki configuration templates](https://documentation.meraki.com/General_Administration/Templates_and_Config_Sync/Managing_Multiple_Networks_with_Configuration_Templates) are an easy way to ensure a highly consistent configuration is deployed across networks. 

## Troubleshooting

If your application is rate limited, your application or another application in the organization, or from your application's source IP address, may not be managing the call budget effectively.

1. Ensure your application is following [our best practices](#best-practices-and-tips-for-managing-call-budgets).
2. You can [check the recent API activity](https://developer.cisco.com/meraki/api-v1/get-organization-api-requests-overview-response-codes-by-interval/) for the given organization to understand if you are sharing the budget with other applications.
3. Scripts that run with little to no maintenance can degrade the performance of your organization's API requests and use up your budget unnecessarily. Audit your organization's API consumption

You can find more answers about call budgets in [our developer community](https://community.meraki.com/t5/Developers-APIs/bd-p/api).