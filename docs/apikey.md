# Custom API key

You can custom the API key for the `Try it out` function. There are three different ways to specify the API key.

 - Config API key in the swagger JSON file
 - Config Static API Key in the `config.json`
 - Config & generate a dynamic API key from a js file

### Config Static API Key in the `config.json`
You can set the API key in the `config` key. Here is an example
```json
{
          "title": "Meraki Dashboard API (fixed API Key)",
          "content": "https://raw.githubusercontent.com/meraki/openapi/master/openapi/spec2.json",
          "type": "oas",
          "config":{
            "apiKey": {
              "X-Cisco-Meraki-API-Key": "Hello World"
            }
          }
        }
```

### Config & generate a dynamic API key from a js file
You can dynamically generate the API key from a js file, which will export a [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
**async function** can be used to generate API from remote with the for the current user, this can be very powerful.
```json
{
          "title": "Meraki Dashboard API (dynamic API Key)",
          "content": "https://raw.githubusercontent.com/meraki/openapi/master/openapi/spec2.json",
          "type": "oas",
          "config":{
            "apiKeyGenerator": {
              "$remoteModule": "config/api_key.js"
            }
          }
        }
```
### example for the API key generate file
```js
module.exports = async function(){
    return "remote key";
}
```
