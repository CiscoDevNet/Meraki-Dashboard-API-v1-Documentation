# Interactive API Doc Configuration
```json-LoadRemoteFile
{
  "title": "Pet Store",
  "content": "https://petstore.swagger.io/v2/swagger.json",
  "type": "oas"
}
```
```json-LoadLocalFile
{
  "title": "Network API",
  "content": "api.json",
  "type": "oas"
}
```

## Swagger content
 You can use `content` key to config the API location. The `content` can be remote file or local file.
> If the remote files is updated, please rebuid the documentation again to trigger update

## Configuration
All other config will be under `config` key.
```json
{
  "title": "Network API",
  "content": "api.json",
  "type": "oas",
  "config": {
  
  }   
}
```
### `exampleAsDefault`
The `exampleAsDefault` will display the example data tab by default
```json
{
  "title": "Network API",
  "content": "api.json",
  "type": "oas",
  "config": {
    "exampleAsDefault":true
  }   
}
```

### `overview`
The `overview` can specify the additional content you can add to API overview section. Please refer to [Add additional content to API overview](docs/overview.md)
```json
{
  "title": "Pet Store",
  "content": "https://petstore.swagger.io/v2/swagger.json",
  "type": "oas",
  "config":{
    "overview":"./config/overview.md"
  }
}
```
### `groupBy`
You can custom how the API grouped by specifying the grouping role. Please refer to [Custom API grouping](docs/group.md)

### `apiKey`
You can custom the API key for the `Try it out` function. Please refer to [Custom API key](docs/apikey.md)

### other config
You can define other config keys and values in the `config` key, and you can use that in the `apiKeyGenerator` or `groupBy` function

