Paginated GET endpoints only return a subset of the results in the first response. You must execute subsequent requests to the endpoint with slightly different parameters in order to get the rest of the data. This functionality is important for API endpoints that could theoretically return some obscenely large number of results.


## How does pagination work in the Dashboard API?

A paginated endpoint in the API accepts in 3 special query parameters:



*   `perPage`: The number of entries to be returned in the page (the current request)
*  ` startingAfter`: A token used by our server to indicate the starting "identifier" of the page (i.e. the data we return in this request will start immediately after the entry with this "identifier")
*   `endingBefore`: A token used by our server to indicate the ending "identifier" of the page (i.e. the data we return in this request will end immediately before the entry with this "identifier")

The actual types of the startingAfter and endingBefore identifiers will vary depending on the API endpoint. However, they typically fall into 2 categories:



*   **Timestamps**: The values of `startingAfter` and `endingBefore` are timestamps if we're paginating based on time. In other words, each entry returned in the response has some timestamp value associated with it, and each request returns a fixed number of these entries based on the value of the perPage parameter. We use timestamps as the "boundaries" between pages.
    *   For example, the current page might contain entries with timestamps ranging from exactly 2 days ago to exactly 1 day ago. The previous page might be referred to by `{ endingBefore: <2 days ago> }`, and the next page might be referred to by `{ startingAfter: <1 day ago> }`
*   **Integer IDs**: The values of `startingAfter` and `endingBefore` could instead be integer IDs if we're paginating purely based on the number of records. In other words, each entry returned in the response has some integer ID associated with it, and each request returns a fixed number of these entries based on the value of the `perPage` parameter. We use the ID values as the "boundaries" between pages.
    *   For example, the current page might contain 5 entries with integer IDs ranging from `101` to `105 ` inclusive. The previous page might be referred to by `{ endingBefore: 101 }`, and the next page might be referred to by `{ startingAfter: 105 }`

When you send an API request to a paginated endpoint, the number of records that are actually queried in the database is equal to the value of perPage. Then, the HTTP response will contain a custom header named Link. The Link header is a comma-separated list of **up to** 4 links: `first`, `prev`, `next`, and `last`. These links represent subsequent requests that can be used to navigate the paginated records. These links will include appropriate values for the startingAfter or endingBefore parameters in order to achieve this navigation. The exact format of the Link header might look something like:
```
<www.example.com?perPage=5&startingAfter=0>; rel=first, <www.example.com?perPage=5&endingBefore=6>; rel=prev, <www.example.com?perPage=5&startingAfter=10>; rel=next, <www.example.com?perPage=5&endingBefore=0>; rel=last
```

In other words, each of these 4 links contains the request path + appropriate values for some combination of `perPage`, `startingAfte`r, and `endingBefore` in order to retrieve a specific page in the data. For instance, making the API request specified in the next link will give you the subsequent page of data. Alternatively, making the API request specified in the first link will bring you back to the first page of data.


## Example

Still unsure how this pagination process works in practice? Let's walk through a simplified version of our "bluetooth clients" API endpoint. If you instead want to play around with some real paginated endpoints of ours, you could check out the [real bluetooth clients API endpoint](../api/#/http/api-endpoints/bluetooth-clients/get-network-bluetooth-clients) or the [client events API endpoint](../api/#/http/api-endpoints/clients/get-network-client-events).

Suppose an end user makes an API request to get the list of bluetooth clients seen by APs in their network. This is an API endpoint that is paginated by **integer ID**. The end user only wants to display 5 records per page, so they set the `perPage` parameter to 5 in the initial request. `startingAfter` and `endingBefore` are not specified in the first request.

The end user makes the initial request: 
`GET https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5`



*   Link header in response: 
```
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=0>; rel=first, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=105>; rel=next, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=0>; rel=last
```
*   Response Body: 
```
[ { id: 101 }, { id: 102 }, { id: 103 }, { id: 104 }, { id: 105 } ]
```

The end user makes a second request to get the next page of data (i.e. using the next link from the last request's Link response header): GET https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=105



*   Link header in response: 
```
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=0>; rel=first, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=110>; rel=next, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=0>; rel=last
```
*   Response Body: 
\
```
[ { id: 106 }, { id: 107 }, { id: 108 }, { id: 109 }, { id: 110 } ]
```

The end user now decides they're sick of paginating. They decide to jump right to the last page of data (i.e. using the last link from the last request's Link response header): `GET https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=0`



*   Link header in response: 
```
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&startingAfter=0>; rel=first, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=146>; rel=prev, 
<https://api.meraki.com/api/v0/networks/N_1234/bluetoothClients?perPage=5&endingBefore=0>; rel=last
```
*   Response Body:
```
 [ { id: 146 }, { id: 147 }, { id: 148 }, { id: 149 }, { id: 150 } ]
```

Notice that the first and last links stayed consistent throughout all of the requests, and in the final request, the next link transformed into a `prev` link (since there is no next set of data). Also notice that this particular endpoint only ever included 3 links at a time in the response rather than all 4 (a unidirectional pagination iteration process). This behaviour is completely implementation-specific.