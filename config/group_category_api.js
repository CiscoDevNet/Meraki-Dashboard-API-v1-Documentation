// catrgory : tag: title mapping

var tree = {
    "General" : {
        'devices':'Devices',
        'networks':'Networks',
        'organizations':'Organizations'
    },
    "Product" : {
        'appliance':'Appliance',
        'camera':'camera',
        'cellularGateway':'CellularGateway',
        'insight':'Insight',
        'sm':'SM',
        'switch':'Switch',
        'wireless':'Wireless'
    }
}

module.exports = function groupBy(operation, meta) {
    var firstTag = operation.tags[0];
    var category = Object.keys(tree).find(x=>tree[x][firstTag])
    return category? category +'/'+ tree[category][firstTag] : firstTag; 
};