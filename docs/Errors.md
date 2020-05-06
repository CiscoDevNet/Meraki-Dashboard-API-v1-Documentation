Error responses from the API generally use standard HTTP status codes. Some examples:

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

