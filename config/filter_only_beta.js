const deepFindBeta = (schema) => {
    if (!schema) return false;
    return Object.keys(schema).map((key) => {
      if (key === 'x-release-stage' && schema[key] === 'beta') {
        return true;
      }
      if (typeof schema[key] === 'object') {
        return deepFindBeta(schema[key]);
      }
      return false;
    }).reduce((p, c) => p || c, false);
  }
  
  module.exports = function (operation, meta) {
    return deepFindBeta(operation);
  };