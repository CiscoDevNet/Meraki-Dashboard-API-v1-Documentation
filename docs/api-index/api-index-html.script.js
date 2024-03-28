// function filterTable(input, columnIndex) {
//     // Get all filter input values as an array
//     var filterValues = Array.from(document.querySelectorAll('.scrollable-table thead input[type="text"]'))
//                             .map(input => input.value.toLowerCase());

//     // Select all the table rows in the body
//     var rows = document.querySelectorAll('.scrollable-table tbody tr');

//     // Iterate over each row of the table
//     rows.forEach(row => {
//         var cells = row.querySelectorAll('td');
//         var match = filterValues.every((filter, index) => {
//             return filter === '' || cells[index].textContent.toLowerCase().includes(filter);
//         });
//         // If all filters matched, display the row; otherwise, hide it
//         row.style.display = match ? '' : 'none';
//     });
// }

// function clearFilters() {
//     // Clear all filter inputs
//     var filterInputs = document.querySelectorAll('.scrollable-table thead input[type="text"]');
//     filterInputs.forEach(input => input.value = '');

//     // Reapply filters to update the table view
//     filterTable(filterInputs[0], 0); // The actual parameters don't matter here as filterTable() will read all inputs
// }


// document.addEventListener('DOMContentLoaded', () => {
//     // Add the filter event listener to all filter inputs
//     document.querySelectorAll('.scrollable-table thead input[type="text"]').forEach(input => {
//         input.addEventListener('keyup', () => filterTable(input, 0));
//     });

//     // Initialize the table view by running the filter once on page load
//     filterTable(document.querySelector('.scrollable-table thead input[type="text"]'), 0);
// });

function filterTable(input, columnIndex) {
    // Get all filter input values and split by spaces for multi-term filtering
    var filterValues = Array.from(document.querySelectorAll('.scrollable-table thead input[type="text"]'))
                            .map(input => {
                                // Split by space and remove empty strings
                                return input.value.toLowerCase().split(' ').filter(Boolean);
                            });

    // Select all the table rows in the body
    var rows = document.querySelectorAll('.scrollable-table tbody tr');

    // Iterate over each row of the table
    rows.forEach(row => {
        var cells = row.querySelectorAll('td');
        var match = filterValues.every((terms, index) => {
            // Check if all terms match for this column
            return terms.every(term => {
                // Support for wildcard "*" by creating a regex (.* for 0 or more characters)
                let regex = new RegExp(term.replace(/\*/g, '.*'));
                return regex.test(cells[index].textContent.toLowerCase());
            });
        });
        // Display the row if all filters matched, otherwise hide it
        row.style.display = match ? '' : 'none';
    });
}

function clearFilters() {
    // Clear all filter inputs
    var filterInputs = document.querySelectorAll('.scrollable-table thead input[type="text"]');
    filterInputs.forEach(input => input.value = '');

    // Reapply filters to update the table view
    filterTable(filterInputs[0], 0); // The actual parameters don't matter here as filterTable() will read all inputs
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize the table view by running the filter once on page load
    filterTable(document.querySelector('.scrollable-table thead input[type="text"]'), 0);
});

