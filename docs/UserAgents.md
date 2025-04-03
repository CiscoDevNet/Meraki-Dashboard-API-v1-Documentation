<seotitle>Guide: User agents</seotitle>
<seodescription>developers must send unique user agent strings with every API request. In this guide, the basics of formatting and implementation are described.
</seodescription>

# User agents

When you invoke dashboard API, it's best practice to provide a [custom user agent string](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) with each API request. This helps your customers and Meraki administrators monitor API interactions with their environments and helps build their trust. In brief, here are some Dos and Don'ts with user agent strings.

## Dos

1.	Provide the user agent string in the user agent header of every API request.
2.	Follow the prescribed format below, which differs minimally from standard practices.
3.	Include only the requested information in your user agent string.
4.	Use only slashes ("/") when you optionally provide application version information.



## Don'ts

1.	Do not provide inconsistent or incorrect user agent strings across your application.
2.	Do not omit the user agent string from any of your requests.
3.	Do not add unnecessary information or special characters to your user agent string.
4.	Do not mix the forward slash (/) with the backward slash (\).

## Formatting

Format your user agent strings as follows:

``` Template
ApplicationName VendorName
```

Include version information as follows:

``` Template with version string
ApplicationName/1.0 VendorName
```

Regardless of your branding guidelines, your application name and vendor name must omit all spaces, hyphens, and special characters. When you provide a custom user agent string in API calls, ensure that the information is typically exclusively useful to Meraki dashboard admins, so it's not necessary to include sometimes arcane information, as is common practice amongst web browsers.

### Examples

#### Example 1

If your vendor name is _Lunar Commander_, and your application name is _Planet Craft Lite_, then use:

``` Example 1
PlanetCraftLite LunarCommander
```

or, if you want to include a version string:

``` Example 1 with version string
PlanetCraftLite/0.8b LunarCommander
```

#### Example 2: Hyphenated names

If your vendor name is _Happy-Rabbit Productions_, and your application name is _Burrow Finder_, then use: 

``` Example 2
BurrowFinder HappyRabbitProductions
```

or, if you want to include a version string:

``` Example 2 with version string
BurrowFinder/2.5 HappyRabbitProductions
```

## In practice

It's usually trivial to add user agent headers to your API requests. All HTTP request libraries offer some means of appending the user agent header to your requests.
### Python library

If you use the Meraki [Python library](pythonLibrary.md), then simply pass the kwarg `caller` in your session definition.

``` Python
import meraki
dashboard = meraki.DashboardAPI(caller='PlanetCraftLite/0.8b LunarCommander')
```

Alternatively, you can modify the library's config.py file to set this globally. For more information, see [Official Dashboard API library (SDK) for Python](https://github.com/meraki/dashboard-api-python)

### PowerShell

If you use the `Invoke-WebRequest` method, then provide the `-UserAgent` flag in each of your requests:

``` PowerShell
$userAgent = 'ApplicationName VendorName'
$apiCallExample = Invoke-WebRequest -URI $uri -Headers $headers -UserAgent $userAgent
```

### Java

If you use the `HttpURLConnection` module, then use `setRequestProperty` to send the user agent:

``` Java
import java.net.HttpURLConnection;
String userAgent = "ApplicationName VendorName"

HttpURLConnection connectionExample = null;
urlExample = new URL(exampleStringUrl); // appropriate operation URL here
connection = (HttpURLConnection) urlExample.openConnection();
// other setRequestProperties here, e.g. Bearer Auth, etc.
connection.setRequestProperty("User-Agent", userAgent);
```
