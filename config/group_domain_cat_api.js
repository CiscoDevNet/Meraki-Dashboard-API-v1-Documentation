
// Order by Tags array

// domain/category/serviceGroup/serviceGroup


const groupBy = function (operation, meta) {
    let path = ""
    let tags = operation.tags;
    let scopes = ['administered', 'organizations', 'networks', 'devices'];
    if(scopes.find(s => tags[0] === s)){
        path = "GENERAL/";
    }else{
        path = "PRODUCTS/";
    }
    tags.forEach((t,i) => {
        if (i > 3){return} // limit total Tags
        if( i == 1){t = t.toUpperCase()} // capitalize Use Case (Configure/Monitor)
        path += t + "/";
        
    });
    path = path.replace(/\/$/, "");
    return path;
}

module.exports = groupBy;

// ********************
// testing
// ********************


// let productTest = {
//     tags: [ 'switch', 'monitor', 'devices', 'ports', 'statuses']
// }
// let scopeTest = {
//     tags: [ 'networks', 'configure', 'floorPlans']
// }


// console.log("productTest", productTest, groupBy(productTest));
// // PRODUCTS/switch/MONITOR/devices/ports

// console.log("scopeTest", scopeTest, groupBy(scopeTest));
// // GENERAL/networks/CONFIGURE/floorPlans
