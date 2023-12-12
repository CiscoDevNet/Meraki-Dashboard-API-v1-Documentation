# Query Parameters

Interacting with the Meraki Dashboard API often requires the inclusion of query parameters in your URL request string. These parameters, added to the end of the URL, are essential for filtering, sorting, or specifying the data you wish to retrieve. They refine your API request for more precise data handling.

## Basic Structure
Query parameters are attached to the URL following a `?` symbol, with each parameter separated by the `&` symbol. The structure typically looks like this:

```
https://api.meraki.com/api/v1/resource?parameter1=value1&parameter2=value2
```

## Using `array[]` Parameters
To specify multiple values for a parameter such as `serials`, append `[]` to the parameter name, resulting in `serials[]`. Assign a value using `=`, for example, `serials[]=foo`. Repeat this format for each item in the array, separating them with `&`.

**Example:**

```
https://api.meraki.com/api/v1/devices?serials[]=1234&serials[]=5678
```

This URL filters devices by the serial numbers `1234` and `5678`.

#### Encoding Query Parameters
Special characters in query parameters must be percent-encoded to ensure correct URL interpretation. This is crucial for characters like spaces, ampersands (`&`), and others with special meanings in URLs.

**Example:**

```
https://api.meraki.com/api/v1/devices?tags=Office%20A&tags=Building%202
```

In this example, the spaces in `Office A` and `Building 2` are encoded as `%20`.

#### Guidelines and Best Practices
- **Check Parameter Names**: Always consult the official documentation to verify correct parameter names and formats, especially for parameters like `serials[]`.
- **Limit the Number of Parameters**: Be aware of the API's limitations regarding the compatibility of parameters and their values.
- **Encode Special Characters**: Employ percent-encoding for special characters to prevent request errors.
- **Regular Documentation Updates**: Regularly check the API documentation for updates or changes in query parameter handling.
- **Testing**: Use tools like Postman or cURL to test your URLs with query parameters, ensuring they are constructed correctly and function as intended.

