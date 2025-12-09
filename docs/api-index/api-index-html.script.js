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

let currentOpFilter = null;
let opFilterPanelVisible = false;

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
        var matchesColumns = filterValues.every((terms, index) => {
            // Check if all terms match for this column
            return terms.every(term => {
                try {
                    // Support for wildcard "*" by creating a regex (.* for 0 or more characters)
                    let regex = new RegExp(term.replace(/\*/g, '.*'));
                    // +1 to skip the leading clear-filters column
                    return regex.test((cells[index + 1]?.textContent || '').toLowerCase());
                } catch (e) {
                    // If regex fails, ignore this term
                    return true;
                }
            });
        });
        const opId = (row.dataset.operationId || '').toLowerCase();
        const matchesOpFilter = !currentOpFilter || currentOpFilter.size === 0 || currentOpFilter.has(opId);
        // Display the row if all filters matched, otherwise hide it
        row.style.display = matchesColumns && matchesOpFilter ? '' : 'none';
    });
    updateCounts();
}

function clearFilters() {
    // Clear all column filter inputs
    var filterInputs = document.querySelectorAll('.scrollable-table thead input[type="text"]');
    filterInputs.forEach(input => input.value = '');

    // Reapply filters to update the table view
    filterTable();
}

function applyOpFilter() {
    var textarea = document.getElementById('opFilterInput');
    if (!textarea) {
        return;
    }
    var ops = textarea.value.split(/[\s,]+/).filter(Boolean).map(op => op.toLowerCase());
    currentOpFilter = ops.length > 0 ? new Set(ops) : null;
    filterTable();
}

function clearOpFilter() {
    var textarea = document.getElementById('opFilterInput');
    if (textarea) {
        textarea.value = '';
    }
    currentOpFilter = null;
    filterTable();
}

function toggleOpFilterPanel() {
    var panel = document.getElementById('opFilterPanel');
    var toggleBtn = document.getElementById('opFilterToggle');
    if (!panel) return;
    opFilterPanelVisible = !opFilterPanelVisible;
    panel.style.display = opFilterPanelVisible ? 'block' : 'none';
    if (toggleBtn) {
        toggleBtn.textContent = opFilterPanelVisible ? '▲' : '▼';
        toggleBtn.title = opFilterPanelVisible ? 'Hide advanced operation filter' : 'Show advanced operation filter';
    }
}

function clearAllFilters() {
    clearOpFilter();
    clearFilters();
}

function updateCounts() {
    var totalSpan = document.getElementById('totalCount');
    var methodSpan = document.getElementById('methodCounts');
    if (!totalSpan || !methodSpan) return;

    var visibleRows = Array.from(document.querySelectorAll('.scrollable-table tbody tr'))
        .filter(row => window.getComputedStyle(row).display !== 'none');

    var methodCounts = visibleRows.reduce((acc, row) => {
        var m = (row.dataset.method || '').toUpperCase();
        if (m) acc[m] = (acc[m] || 0) + 1;
        return acc;
    }, {});

    totalSpan.textContent = `Total operations: ${visibleRows.length}`;
    methodSpan.textContent = `GET: ${methodCounts.GET || 0} | POST: ${methodCounts.POST || 0} | PUT: ${methodCounts.PUT || 0} | DELETE: ${methodCounts.DELETE || 0}`;
}

function stripHtml(value) {
    return value.replace(/<[^>]+>/g, '');
}

function exportFilteredCsv() {
    // Match the full CSV columns
    var headers = ["releaseStage","operationId","summary","apiDocsUrl","method","path","pathParams","requestBodyParams","responseParams","tags","pythonOperation","oauthScopes"];

    var visibleRows = Array.from(document.querySelectorAll('.scrollable-table tbody tr'))
        .filter(row => window.getComputedStyle(row).display !== 'none');

    var csvRows = [headers];
    visibleRows.forEach(row => {
        var cells = headers.map(h => {
            // data-* attributes were set in kebab-case and map to camelCase in dataset
            var value = row.dataset[h] || '';
            var text = value.replace(/"/g, '""');
            return `"${text}"`;
        });
        csvRows.push(cells);
    });

    var csvContent = csvRows.map(r => r.join(',')).join('\n');
    var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'meraki-api-index.filtered.csv';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize the table view by running the filter once on page load
    filterTable();
    updateCounts();
});

