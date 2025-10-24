## Action batches
An action batch is a configuration mechanism that
* groups multiple write actions (create, update, destroy) into a single batch
* executes all actions atomically (all or nothing, no partial success), and
* supports synchronous or asynchronous processing.

Action batches are ideal for applying changes across multiple devices or networks. They ensure consistent configuration by processing the entire batch as a single unit—either all changes apply or none do. This mechanism helps you avoid exceeding the API rate limit. For example, with a single POST operation, you can add a switch to a network, configure all 48 ports, and set the switch’s management interface at the same time.

## Synchronous and asynchronous execution modes
Action batches can run in either **synchronous** or **asynchronous** mode, depending on the number of actions and the desired execution behavior.
| Mode            | Description                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------|
| **Synchronous** | Executes the batch immediately and waits for completion. Limited to **20 actions**.          |
| **Asynchronous**| Submits the batch and returns immediately. The system processes the batch in the background. Supports up to **100 actions**. |

### Key differences
- **Synchronous** batches are suitable for smaller updates that need immediate feedback.
- **Asynchronous** batches allow larger operations to be queued and processed by the system.
- Only **five concurrent** batches (regardless of mode) may run at any given time.

Synchronous batches provide a faster feedback loop, while asynchronous batches allow for greater scale and deferred processing.

### Other key points
- Different types of resources and operations can be combined in a batch.
- The actions in a batch are executed in the order that they are defined.

### Restrictions
- An action batch must be explicitly confirmed before execution by setting the confirmed property. Once confirmed, it cannot be deleted. If a batch is defined but not confirmed, it is automatically deleted after one week. This mechanism helps prevent accidental or stale configuration updates.

## How action batches work 
The key components involved in the process are:
* **Action batch**: is the container of multiple API actions.
* **API client**: is the external system or user submitting the batch.
* **Execution mode**: defines whether a batch runs synchronously or asynchronously.

The process involves these stages:
* **Batch creation**: The client defines a list of actions to be executed and sets configuration flags such as `confirmed` and `synchronous`.
* **Batch submission**: The batch is submitted through a POST request to the API.
* **Confirmation**: The batch must be marked as `confirmed` to execute. If not, it is stored temporarily and deleted after one week.
* **Execution**: The system executes the batch in the order defined. All actions must succeed, or the batch fails.
* **Result handling**: A status object returns completion, failure, or error details. For synchronous batches, this occurs immediately. For asynchronous, the client must poll for completion.

**Result**:
This mechanism ensures that batches of configuration requests are executed together. They either fully succeed or fail.

## Create an action batch
**Purpose**: Submit multiple configuration changes in a single transaction.  

1. Send a `POST` request to `/organizations/{organizationId}/actionBatches`.  
2. Use the following parameters:  
   * `confirmed`: Set to `true` for immediate execution, or `false` to preview before executing.  
   * `synchronous`: Run the batch synchronously if it includes no more than 20 actions.  
   * `actions`: A set of changes to be made as a part of this action. Each action includes:  
     - `resource`: the unique identifier for the resource to be acted on,  
     - `operation`: the action to perform on resource such as (`create`, `update`, `destroy`, etc.),  
     - `body`: the JSON object with attributes to apply. Example: `{"tags": tags, "type": "access", "vlan": vlan}`
3. Include the required headers in your request, such as the API key and content type.  
4. Submit the request.  

**Result**:  
If successful, the response returns a batch ID, confirmation setting, and a status object with details such as whether the batch completed, failed, and any errors.  
**Monitoring**:  
Use the Dashboard API operations (GET, PUT, and DELETE) to return a list of action batches, retrieve a specific batch, update it, or delete it.  

## API operations for action batches
These API operations are available to manage action batches:

| Operation                                  | Method | Endpoint                                             |
| ------------------------------------------ | ------ | ---------------------------------------------------- |
| Create an action batch                     | POST   | `/organizations/{organizationId}/actionBatches`      |
| List all action batches in an organization | GET    | `/organizations/{organizationId}/actionBatches`      |
| Return a specific action batch             | GET    | `/organizations/{organizationId}/actionBatches/{id}` |
| Delete an unconfirmed action batch         | DELETE | `/organizations/{organizationId}/actionBatches/{id}` |
| Update an unconfirmed action batch         | PUT    | `/organizations/{organizationId}/actionBatches/{id}` |

## Sample request for an action batch
```bash
curl -X POST https://api.meraki.com/api/v0/organizations/1234567890/actionBatches \
-L \
-H 'Content-Type: application/json' \
-H 'X-Cisco-Meraki-API-Key: <API_KEY>' \
-d '{
"confirmed": true,
"synchronous": true,
"actions": [
     {
      "resource": "/devices/QXXX-XXXX-XXXX/switchPorts/3",
      "operation": "update",
      "body": {
        "enabled": true
      }
    }
]
}'
```
## Sample response for an action batch
The response to a successful batch submission includes batch status and details:
Successful HTTP Status: *201*

```json
 {
   "id": "173869674715420",
    "status": {
        "completed": true,
        "failed": false,
        "errors": [],
        "createdResources": []
    }
   "confirmed": true,
   "actions": [
     {
       "resource": "/devices/QXXX-XXXX-XXXX/switchPorts/3",
       "operation": "update",
       "body": {
         "enabled": false
       }
     }
   ]
 }
```
## Response errors
### Unsupported operation
When you have attempted to use an API operation that is not a supported resource as listed above.

```json
{
    "errors": [
        "Unsupported operation"
    ]
}
```
### Execution error
If the batch fails because one of the resources had an error, the `status` parameter will contain additional information.

```json
"status": {
        "completed": false,
        "failed": true,
        "errors": [
            "Error occurred while executing create /networks/L_643451796760561416/vlans/ with {\"id\":111,\"name\":\"New-VLAN\",\"applianceIp\":\"172.16.111.1\",\"subnet\":\"172.16.111.0/24\"}: Validation failed: Vlan has already been taken"
        ],
        "createdResources": []
    }
```

## Example script
This example Python script will create a new VLAN on a Meraki MX Security Appliance. It will then update multiple switches with new tags. Finally, several ports will be updated to leverage the new VLAN settings.

```python
# actionBatch-VlanUpdate.py

import requests

# Environment Variables
API_KEY = "aaaaaaaaaaaaaaaaaaabbbbbbbcccccccc"
org_id = 1234567
vlan = 99
net_id = "L_000000000000000"
switch_a = "AAAA-BBBB-CCCC"
switch_b = "DDDD-EEEE-FFFF"
tags = "APIness"

url = f"https://api.meraki.com/api/v1/organizations/{org_id}/actionBatches"

payload = {
    "confirmed": True,
    "synchronous": True,
    "actions": [
        {
            "resource": f"/networks/{net_id}/vlans",
            "operation": "create",
            "body": {
                "id": vlan,
                "name": "API-VLAN",
                "applianceIp": f"172.16.{vlan}.1",
                "subnet": f"172.16.{vlan}.0/24",
            },
        },
        {
            "resource": f"/networks/{net_id}/devices/{switch_a}",
            "operation": "update",
            "body": {"tags": tags},
        },
        {
            "resource": f"/networks/{net_id}/devices/{switch_b}",
            "operation": "update",
            "body": {"tags": tags},
        },
        {
            "resource": f"/devices/{switch_a}/switchPorts/1",
            "operation": "update",
            "body": {"tags": tags, "type": "access", "vlan": vlan},
        },
        {
            "resource": f"/devices/{switch_b}/switchPorts/1",
            "operation": "update",
            "body": {"tags": tags, "type": "access", "vlan": vlan},
        },
    ],
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)

```

```bash
$ python3 actionBatch-VlanUpdate.py 
{"id":"643451796760559653","organizationId":"1234567","confirmed":true,"synchronous":true,"status":{"completed":true,"failed":false,"errors":[]},"actions":[{"resource":"/networks/L_00000000000000/vlans/","operation":"create","body": ....
```
