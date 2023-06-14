const sortBy = function (operationA, operationB) {
    const order = ['post', 'get', 'put', 'delete'];
    return order.indexOf(operationA.method) - order.indexOf(operationB.method);
  };
  
  module.exports = sortBy;