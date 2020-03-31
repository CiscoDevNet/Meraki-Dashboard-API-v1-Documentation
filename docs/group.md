# Custom API grouping

You can custom how the API grouped by specifying the grouping role. The grouping role will be defined in the separate JS file which will export the grouping method. Here is the `operation object` definition which you can use in the js file.

### Config
```json
{
          "title": "Pet Store",
          "content": "https://petstore.swagger.io/v2/swagger.json",
          "type": "oas",
          "config":{
            "groupBy": {
              "$remoteModule": "config/group_api.js"
            }
          }
        }
```

### Example for the group_api.js
```js
module.exports = function groupBy(operation, meta) {
    return operation.path.split("/").slice(0,4).map(tag=>tag.charAt(0).toUpperCase() + tag.slice(1)).join("/");
    //return operation.tags[0]
};
```

### Operation object definition
```js
export interface Operation {
  operationId: string;
  tags?: string[];
  path: string;
  method: Http.Method;
  summary?: string;
  description?: string;
  produces?: [Http.ContentType];
  consumes?: [Http.ContentType];
  parameters?: [Parameter];
  responses?: {
    [statusCode: string]: Response;
  };
  security?: Security;
}
```
