# Using Postman for Meraki API 

Use Postman to explore and interact with the Meraki API.  

**Before you begin**: Ensure that you have Postman installed and your Bearer token ready. 
Follow these steps to use Postman:

- **Step 1:** Go to [Postman and our Postman collection](https://documenter.getpostman.com/view/897512/SzYXYfmJ).
- **Step 2:** Import the collection by clicking the 'Run in Postman' button.
- **Step 3:** Use your Bearer token for authorization. (comment: add link to the authorization section)
- **Step 4:** Explore the endpoints available in the collection.

**Result:** You can now interact with Meraki networks using Postman. 

# Using Python library for Meraki API 

Use the Meraki Python library to interact with the API programmatically.  

**Before you begin**: Ensure Python and pip are installed on your system.  

Follow these steps to use the Python library:

- **Step 1:** Install the library using the command `pip install meraki`.
- **Step 2:** Import the library in your Python script with `import meraki`.
- **Step 3:** Initialize the Dashboard API with `dashboard = meraki.DashboardAPI(BEARER_TOKEN)`.

**Result:** You can now perform API operations within your Python scripts.

# Country-specific base URI  
In most parts of the world, every API request will begin with the following **base URI**:

> `https://api.meraki.com/api/v1`

For organizations hosted in the following country dashboard, please specify the respective base URI instead:

|  Country         |  URI                              |
|------------------|-----------------------------------|
| Canada           | `https://api.meraki.ca/api/v1`    |
| China            | `https://api.meraki.cn/api/v1`    |
| India            | `https://api.meraki.in/api/v1`    |
| United States FedRAMP | `https://api.gov-meraki.com/api/v1` |


For more information about path schema, see [here](PathSchema.md). 
