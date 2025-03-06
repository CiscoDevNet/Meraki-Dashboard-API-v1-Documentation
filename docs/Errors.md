The error responses from the API generally use standard HTTP status codes. Some examples:

**Response Code**|**Description**
 :-------------: |:-------------:
200 - OK| 	Everything worked as expected.
400 - Bad Request| 	The request was unacceptable, often due to missing a required parameter.
401 - Unauthorized| Incorrect API key
403 - Forbidden| You don't have permissions to do that.
404 - Not Found|	The requested resource doesn't exist.
429 - Too Many Requests|	Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500, 502, 503, 504 - Server Errors|	Meraki was unable to process the request.


If the response code is not specific enough to determine the cause of the issue, error messages will be included in the response in JSON format, for example:

```
{
    "errors": [
       "VLANs are not enabled for this network"
    ]
}
```

## Error Handling

The API will raise exceptions in the event something failed, such as missing or invalid parameters. 
We recommend writing code that gracefully handles all possible API exceptions.

**Absence of 5xx errors in certain API responses**

When interacting with the Meraki dashboard via API, the [apiRequests](https://developer.cisco.com/meraki/api-v1/search/?q=api%20requests) operations offer customer-facing telemetry that includes helpful detail about requests that successfully reached the Meraki dashboard. This includes API calls to known API operations with response codes >= 200 and <= 500. This telemetry can inform most issues that might affect the API client experience.

In some cases, API clients may receive response codes outside of this range, such as 502 or 504, which are not captured in the customer-facing telemetry. This happens usually if the requests did not successfully reach Meraki dashboard. This could indicate an issue between the API client and Meraki dashboard.

Occasional API errors should not materially interfere with the operation of a well developed application. However, if you are encountering a substantial proportion of API errors with response codes >= 500, then please contact Meraki Support for assistance.
