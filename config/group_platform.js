
   

// Order by Tags array

//  "tags": [
//         "appliance",
//         "configure",
//         "uplinks",
//         "settings"
//  ],
//  "x-release-stage": "beta"

// domain/category/serviceGroup/serviceGroup


const groupBy = function (operation, meta) {
    let path = ""
    let tags = [...[],...operation.tags]
   // let releaseStage = operation["x-release-stage"] || ""
    let scopes = ['organizations', 'networks', 'devices','administered'];
    if(scopes.find(s => tags[0] === s)){
        path = "Platform/";
    }else{
        path = "Products/";
    }
    
        
    // Build Folder Tree, make adjustments
    console.log('tags',tags)
    if(tags.length == 2){tags.push(tags[0])}// add scope as a service folder
    tags.forEach((t,i) => {
      
        if(i == 1 && t === 'liveTools' && tags[0] === 'devices'){
            path += "liveTools/";
        }else if(i === 1 && tags[0] === 'administered'){
            path += t + "/administered/";
        
        }else if(i == 0 && scopes.find(s => tags[0] === s)){
            // skip scope
        }
        else{    
            // build path
            path += t + "/";
        }
        
    });    
    path = path.replace(/\/$/, ""); 
    return path;
}

module.exports = groupBy;

// ********************
// testing
// ********************


let productTest = {
    "x-release-stage":"beta",
    tags: [ 'switch', 'monitor', 'devices', 'ports', 'statuses']
}
let scopeTest = {
    tags: [ 'networks', 'configure']
}


//console.log("productTest", productTest, groupBy(productTest));
// PRODUCTS/switch/MONITOR/devices/ports

console.log("scopeTest", scopeTest, groupBy(scopeTest));
// Platform/networks/CONFIGURE/floorPlans
