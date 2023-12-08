

# Callbacks

## Introduction

### What is a Callback?

A "Callback" is an advanced programming feature that provides notifications upon the completion of a long-running operation. Unlike standard API calls that return immediately, callbacks issue results via a webhook when they become available. This aligns with the OpenAPI v3 specification, promoting standardized asynchronous operations.

### What is a Webhook?

A webhook is an outbound API request that Meraki will send to a 3rd party service. Callbacks leverage the Meraki webhook system, supporting both pre-configured receivers and dynamic URLs. In addition, webhook templates can format the HTTP message body and headers for customized integrations.

[Meraki Webhooks Guide](https://meraki.io/webhooks)


### When and Why to Use Callbacks

Callbacks are a feature designed to handle operations that require time to process. They are particularly useful in scenarios where immediate feedback is not essential, but timely notification upon completion is critical. By using callbacks, you optimize resource usage, reduce the need for continuous polling, and streamline workflows. 

- **Bulk Configuration**: When pushing configuration changes to hundreds or thousands of devices, waiting for each action batch to respond synchronously can be time-consuming or rate-limit challenging. With callbacks, you initiate the asynchronous requests and receive updates as each job completes its configurations.

- **Monitoring**: In large networks, continuously polling each request for status can be inefficient and can generate significant API usage. Callbacks enable an event-driven approach, where results can be sent to a group messaging service or database as they are available. 

- **Event-Driven Automation**: Use callbacks to trigger other processes or workflows within your system. For example, once a request has completed and a webhook has been sent, an automated system can continue its next operation using those results.

## Callbacks vs. Alerts

"Alerts" and "Callbacks" are distinct features within the Meraki API, each serving a different purpose and following different data schemas.

### Alerts

Webhook Alerts are event-driven notifications for situations such as a device going offline, sensor detections or a security event.

#### Example Webhook for Alerts

```json
{
  "version": "0.1",
  "sharedSecret": "secret",
  "sentAt": "2022-09-07T14:14:14.591941Z",
  "organizationId":"123",
  "organizationName":"Org in Company",
  "alertType": "APs went down",
  "alertLevel": "critical",
  "alertData": {
  ...
  }
}
```

### Callbacks

Callbacks deliver the outcomes of specific asynchronous API operations such as with Live Tools or Action Batches.

#### Example Webhook for Callbacks

```json
{
  "callbackId": "643451796760560204",
  "organization": {
    "id": "123",
    "name": "Org in Company"
  },
  "message": {
    "pingId": "643451796835419513",
    "status": "complete",
	...
  }
}
```

### Key Differences

- **Alerts**: Identified by the `alertId` and containing the dynamic data in the `alertData` property.

- **Callbacks**: Identified by the `callbackId` and containing the dynamic data in the `message` property.

### Handling in Webhook Service

Differentiate between alerts and callbacks in your service, possibly using tailored webhook templates for each.

#### Liquid Template Example

Here's an example Liquid template to handle the difference in wehbhook payload types:

```liquid
{% if callbackId %}
  {# Handle as Callback #}

{% elsif alertId %}
  {# Handle as Webhook Alert #}

{% else %}
  {# Unknown payload type #}
{% endif %}
```

Learn more about customizing the shape and security of your callback webhooks. 

[Webhook Payload Templates Guide](https://developer.cisco.com/meraki/webhooks/payload-templates-overview/)

### Callback Status

This endpoint provides detailed status information about a specific callback, including its current state, any errors encountered, the initiating user, and the related webhook details.

[API Docs](https://developer.cisco.com/meraki/api-v1/get-organization-webhooks-callbacks-status/)

##### Response Schema

- **callbackId**: Unique identifier of the callback.
- **status**: Current status of the callback. Possible values are:
  - `completed`: Indicates the callback operation has successfully concluded.
  - `failed`: Signifies an error or failure in the callback process.
  - `running`: The callback is still in progress.
- **errors**: Array of error messages, if any, encountered during the callback process.
- **createdBy**: Information about the user who initiated the callback, including their admin ID.
- **webhook**: Detailed information about the webhook used for the callback, including:
  - **url**: The receiver URL for the callback results.
  - **httpServer**: Information about the HTTP server that receives the callback data.
  - **payloadTemplate**: Details about the payload template used for the callback.
  - **sentAt**: Timestamp indicating when the callback was dispatched to the webhook receiver.

##### Example Response

An example JSON response from the `/callbacks/statuses` endpoint:

```json
{
  "callbackId": "1284392014819",
  "status": "completed",
  "errors": ["Callback failed"],
  "createdBy": {
    "adminId": "212406"
  },
  "webhook": {
    "url": "https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031",
    "httpServer": {
      "id": "aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20vd2ViaG9va3M="
    },
    "payloadTemplate": {
      "id": "wpt_2100"
    },
    "sentAt": "2018-02-11T00:00:00.090210Z"
  }
}
```

### Endpoints Supporting Callbacks

#### Live Tools

The following endpoints are examples within the Meraki Dashboard API that support callbacks, enabling asynchronous operations:

1. **Ping**: `POST /devices/{serial}/liveTools/ping`
   - [Ping Endpoint Documentation](https://developer.cisco.com/meraki/api-v1/create-device-live-tools-ping/)
2. **Ping Device**: `POST /devices/{serial}/liveTools/pingDevice`
   - [Ping Device Endpoint Documentation](https://developer.cisco.com/meraki/api-v1/create-device-live-tools-ping-device/)
3. **Wake on LAN**: `POST /devices/{serial}/liveTools/wakeOnLan`
   - [Wake on LAN Endpoint Documentation](https://developer.cisco.com/meraki/api-v1/create-device-live-tools-wake-on-lan/)

#### Bulk Action Jobs

- **Action Batches**: `POST /organizations/{organizationId}/actionBatches`
  - [Action Batches Endpoint Documentation](https://developer.cisco.com/meraki/api-v1/create-organization-action-batch/)

## Example Usage

### Ping Example with Callback

This example demonstrates initiating a ping operation with the result being sent to a specified callback URL:

**Endpoint**: `POST /devices/{serial}/liveTools/ping`

**Request Body**:

```json
{
  "target": "8.8.8.8",
  "count": 4,
  "callback": {
    "url": "https://webhook.site/your-custom-url"
  }
}
```

#### Callback Webhook Example Payload

An example JSON payload from a webhook callback following a ping operation:

```json
{
  "callbackId": "643451796760560204",
  "organization": {
    "id": "321321",
    "name": "My Laboratory"
  },
  "network": {
    "id": "643451796760500000",
    "name": "Branch 1"
  },
  "sentAt": "2023-09-15T06:46:17-07:00",
  "message": {
    "pingId": "643451796835419513",
    "url": "/devices/Q2BX-9QRR-XXXX/liveTools/ping/64345179683500000",


    "request": {
      "serial": "Q2BX-9QRR-XXXX",
      "target": "8.8.8.8",
      "count": "3"
    },
    "status": "complete",
    "results": {
      // Results of the ping operation...
    }
  }
}
```
Demo in action
<img src="./livetools-callbacks-demo.gif" width="800px">

### Example: Action Batches with Callbacks

This example illustrates the use of callbacks in conjunction with an Action Batch operation. Action Batches in the Meraki Dashboard API allow for the execution of multiple actions in a single API call, which can be significantly enhanced with the use of callbacks for asynchronous processing and status updates.

#### Scenario

Suppose we want to update the settings of multiple networks in an organization. Given the potentially long processing time, we'll use a callback to receive status updates on the batch operation.

#### Endpoint: Action Batches

**Endpoint**: `POST /organizations/{organizationId}/actionBatches`

[Action Batches Endpoint Documentation](https://developer.cisco.com/meraki/api-v1/create-organization-action-batch/)

#### Request Body

```json
{
  "organizationId": "123456",
  "confirmed": true,
  "synchronous": false,
  "actions": [
    {
      "resource": "/networks/{networkId1}/ssids/0",
      "operation": "update",
      "body": {
        "name": "New SSID Name 1",
        "enabled": true
      }
    },
    {
      "resource": "/networks/{networkId2}/ssids/1",
      "operation": "update",
      "body": {
        "name": "New SSID Name 2",
        "enabled": false
      }
    }
  ],
  "callback": {
    "url": "https://webhook.site/your-custom-callback-url"
  }
}
```

- **organizationId**: The identifier of the organization.
- **confirmed**: Indicates whether the action batch is confirmed for execution.
- **synchronous**: Set to `false` to indicate the operation is asynchronous and will utilize callbacks.
- **actions**: An array of actions to be executed. Each action specifies a resource to modify, an operation (like "update"), and the body with the new settings.
- **callback**: Object containing the callback URL where status updates will be sent.

#### Callback Webhook Example Payload

When the action batch is processed, a callback is sent to the specified URL with the following example payload:

```json
{
  "callbackId": "874399285760560205",
  "organization": {
    "id": "123456",
    "name": "Global Tech Inc."
  },
  "actionBatchId": "874399285760580000",
  "sentAt": "2023-10-01T09:30:00-07:00",
  "message": {
    "status": "completed",
    "results": {
      "actionsCompleted": 2,
      "actionsFailed": 0,
      "details": [
        {
          "networkId": "networkId1",
          "resource": "/networks/{networkId1}/ssids/0",
          "operation": "update",
          "status": "success"
        },
        {
          "networkId": "networkId2",
          "resource": "/networks/{networkId2}/ssids/1",
          "operation": "update",
          "status": "success"
        }
      ]
    }
  }
}
```

- **callbackId**: The unique identifier for the callback.
- **organization**: Details of the organization.
- **actionBatchId**: Identifier of the action batch.
- **sentAt**: Timestamp of when the callback was sent.
- **message**: Contains the status of the action batch and detailed results.



## Troubleshooting Callbacks

### Monitoring Tools

To aid in troubleshooting, utilize the following monitoring tools and endpoints:

- **Callback Status Endpoint**: As previously mentioned, use the [/callbacks/statuses](https://developer.cisco.com/meraki/api-v1/get-organization-webhooks-callbacks-status/) endpoint to check the delivery status of callbacks.
- **Webhook Logs**: Review the [webhook logs](https://developer.cisco.com/meraki/api-v1/get-organization-webhooks-logs/) for detailed information on the delivery and any errors encountered.

- **Postman**: Setup a [mock server](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock/) to test your webhooks.



### Common Issues and Solutions

#### 1. Callbacks not received
- **Verify Endpoint Configuration**: Ensure the callback URL is correct and the server is capable of receiving POST requests.
- **Check for Typos**: Review the callback URL and payload for any typographical errors.
- **Inspect Firewall Settings**: Confirm that your network allows inbound connections on the port used by your webhook receiver.

#### 2. Callbacks received but with unexpected data
- **Validate Payload**: Check if the payload structure matches the expected schema.
- **Check for Payload Changes**: Ensure there haven't been changes in the payload template structure.

#### 3. Callbacks received with errors
- **Interpret Error Messages**: Use the error messages received in the callbacks to understand what went wrong.
- **Consult Documentation**: Refer to the API documentation of the specific endpoint for detailed error descriptions.

#### 4. Callbacks taking too long to arrive
- **Network Latency**: Test your network for latency issues.
- **Service Overload**: Verify if the receiving server is not overwhelmed with requests.

#### 5. Callbacks received but not processed
- **Server Log Analysis**: Check the server logs to identify processing issues.
- **Code Review**: Look over the code handling the callbacks to find logical errors or exceptions.

### Asking for Help

If after troubleshooting you are still facing issues:

- **[Meraki Community](https://meraki.io/community)**: Engage with the Meraki community for insights and advice.
- **[Support Tickets](https://meraki.cisco.com/meraki-support)**: Open a support ticket with Meraki, providing detailed information about the issue and the steps already taken.

## **Additional Resources**

* [Meraki Webhooks Guide](https://meraki.io/webhooks)
* [OpenAPI v3 Callbacks Specification](https://swagger.io/docs/specification/callbacks/)




