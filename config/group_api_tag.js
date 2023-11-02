const groupBy = function (operation, meta) {
    let path = "";
    operation.tags.forEach((t, i) => {
        // build path
        path += t + "/";
    });
    path = path.replace(/\/$/, "");
    return path;
};

module.exports = groupBy;

// ********************
// testing
// ********************


const testData = {
    "tags": ["Posture Profile", "Browser"]
}
console.log(groupBy(testData))
// Posture Profile/Browser