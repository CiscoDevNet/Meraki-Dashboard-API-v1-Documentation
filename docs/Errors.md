APIs return response codes that help you understand the status of the API operation.  The response codes use standard HTTP status codes. 

Examples of common response codes and their descriptions are:

## Common Response Codes and Descriptions

**Response Code**|**Description**
 :-------------: |:-------------:
200 - OK| 	Everything works as expected
400 - Bad Request| 	The request was unacceptable, often due to missing a required parameter
401 - Unauthorized| Incorrect API key
403 - Forbidden| You lack permission to perform the action
404 - Not Found|	The requested resource doesn't exist
429 - Too Many Requests|	Too many requests hit the API too quickly. We recommend an exponential backoff of your requests
500, 502, 503, 504 - Server Errors|	The request cannot be processed by Meraki

## Error Response Handling

**Recommendation**: Ensure that your code gracefully handles all possible API exceptions.

Some response codes indicate failures and missing or invalid parameters.

If the response code is unclear, check the JSON-format error messages in the response. For example, 

```
{
    "errors": [
       "VLANs are not enabled for this network"
    ]
}
```

##  Unknown 5xx response code

When you interact with the Meraki dashboard via API, you can track requests that successfully reached the Meraki dashboard using the [apiRequests](https://developer.cisco.com/meraki/api-v1/search/?q=api%20requests) operations. The telemetry information provides insight into most issues that can affect the API client experience.

The response codes of the [apiRequests](https://developer.cisco.com/meraki/api-v1/search/?q=api%20requests) operations generally range from 200 to 500. However, some codes, such as 502 or 504, may be outside this range. These are not part of the customer-facing telemetry. These response codes indicate that the request probably did not reach the Meraki dashboard, suggesting an issue between the API client and the Meraki dashboard. 

Occasional occurrences of such API errors (response code is higher than 500) do not interfere with the well-developed application's operation. However, if the number of such errors is high, contact Meraki Support for assistance.
