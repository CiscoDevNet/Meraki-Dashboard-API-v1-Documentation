### Per Organization
* The Dashboard API is limited to **5 requests per second**, per organization.
* A burst of 5 additional requests are allowed in the first second, so a maximum of 15 requests in the first 2 seconds.
* The rate limiting technique is based off of the [token bucket model](https://en.wikipedia.org/wiki/Token_bucket).
* Furthermore, a concurrency limit of **10 concurrent requests per IP** is enforced

### Response Codes
* A `429` status code will be returned when the rate limit has been exceeded, with the `Retry-After` header.

* When an application exceeds the rate limit, the following message will be returned in the response body:
```
{
    "errors": [
        "API rate limit exceeded for organization"
    ]
}
```

### Common Causes

Rate limiting can occur for a variety of reasons, but some of the common causes are the following:

* Running high-volume API monitoring tasks in realtime can overthrottle the system and lead to `429` errors
* Scripts that run with little to no maintenance can degrade the performance of your organization's API requests and use up quota

### Tips to avoid being Rate Limited

Utilize the `Retry-After` header and backoff to minimize compounded rate limit issues. Ensure that if the limit is being exceeded, appropriate action is being taken to handle `429` responses.


#### Handling Limiting Gracefully
​
If the defined rate limit is exceeded, Dashboard API will reply with the `429` (rate limit exceeded) error code. This response will also return a `Retry-After` header indicating how long the client should wait before making a follow-up request.

* The `Retry-After` key contains the number of seconds the client should wait.


* Expect to backoff for 1 - 2 seconds if the limit has been exceeded. You may have to wait potentially longer if a large number of requests were made within this timeframe.
​
A simple example which minimizes rate limit errors:

```
response = requests.request("GET", url, headers=headers)
​
if response.status_code == 200:
	# Success logic
elif response.status_code == 429:
	time.sleep(int(response.headers["Retry-After"]))
else:
	# Handle other response codes
```


#### Best Practices

1. If you require device information and are making a request for each device using the device-scope endpoint, or the network-scope endpoint:

	``/networks/{networkId}/devices/{serial}``
	
	``/networks/{networkId}/devices``
	
	It is more effecient with respect to the rate limit to instead use the organization-scope devices endpoint, which returns all devices in a performant manner.
	
	``/organizations/{organizationId}/devices ``
	
2. Similarly utilize the network-wide clients endpoint to retrieve information on all clients that have used a network:
	
	``/networks/{networkId}/clients``
	
3. Use **Action Batches** for bulk constructive/destructive operations (``PUT``, ``POST``, ``DELETE``). To read more about Action Batches, visit the [Meraki Blog](https://meraki.cisco.com/blog/2019/06/action-batches-a-recipe-for-success/) or [Github Demo](https://developer.cisco.com/codeexchange/github/repo/shiyuechengineer/action-batches/). Action Batches are a perfect tool for submitting batched configuration requests in a single synchronous or asynchronous transaction.


> If you have further questions or concerns around the API rate limit, please contact Meraki [support](support@meraki.com) about your use case.