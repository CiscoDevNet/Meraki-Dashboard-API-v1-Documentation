module.exports = function groupBy(operation, meta) {
    //return operation.path.split("/").slice(0,4).map(tag=>tag.charAt(0).toUpperCase() + tag.slice(1)).join("/");
    return operation.tags[0].sort(function (a, b) {
        if (a > b) {
            return -1;
        }
        if (b > a) {
            return 1;
        }
        return 0;
    });
};
