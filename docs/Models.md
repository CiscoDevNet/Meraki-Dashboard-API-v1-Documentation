When submitting a `PUT` or `POST` it is best to import the **model** for the resource you are going to modify, commonly named the same as the resource, without the leading verb. 

 The model is simply a dictionary/object that contains the available parameters (i.e. **duration**, **period**, etc), their **type** (i.e. **string**, **number**, .etc) and available value options. Altnernativley, the data can be submitted using the JSON structure defined in the docs. 
 
 
### Python Example
*With Model*

```python
meraki = Meraki(x_cisco_meraki_api_key)
from meraki_dashboard_api.models.update_network_model import UpdateNetworkModel

collect = {}
network_id = "N_1234567890"
collect["network_id"] = network_id

update_network = UpdateNetworkModel()
update_network.name = "New Network Name"
update_network.tags = "viaAPI"
update_network.disable_remote_status_page = True
collect["update_network"] = update_network

result = meraki.networks.update_network(collect)
print(result)
```
*Without Model*


```python
meraki = Meraki(x_cisco_meraki_api_key)

collect = {}
network_id = "N_1234567890"
collect["network_id"] = network_id

update_network = {
    name: "New Network Name",
    tags: "viaAPI",
    disable_remote_status_page: True,
}
collect["update_network"] = update_network
result = meraki.networks.update_network(collect)
print(result)
``` 
 
### JavaScript Example
 *With Model*
 
 ```js
let input = [];
let networkId = 'N_1234567890';
input['networkId'] = networkId;

let updateNetwork = new meraki.UpdateNetworkModel();
updateNetwork.name = 'New Network Name';
updateNetwork.tags = 'viaAPI';
updateNetwork.disableRemoteStatusPage = true;
input['updateNetwork'] = updateNetwork;

meraki.updateNetwork(input).then((response) => console.log(response))
 ```
 *Without Model*
 
  ```js
let input = [];
input['networkId'] = 'N_1234567890';

let updateNetwork = {
	name: "New Network Name",
	tags: "viaAPI"
	disableRemoteStatusPage: true
}
input['updateNetwork'] = updateNetwork;

meraki.updateNetwork(input).then((response) => console.log(response))
 ```