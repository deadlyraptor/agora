// sort table
const table = document.getElementById('sortable-table');
const headers = table.querySelectorAll('th:not(#actions)');
const tableBody = table.querySelector('tbody');
const rows = tableBody.querySelectorAll('tr');

// Track sort directions
const directions = Array.from(headers).map(function (header) {
    return '';
});

const sortColumn = function (index) {
    // Get the current direction
    const direction = directions[index] || 'asc';

    // A factor based on the direction
    const multiplier = direction === 'asc' ? 1 : -1;

    // Clone the rows
    const newRows = Array.from(rows);

    // Sort rows by the content of cells
    newRows.sort(function (rowA, rowB) {
        // Get the content of cells
        const cellA = rowA.querySelectorAll('td')[index].innerHTML;
        const cellB = rowB.querySelectorAll('td')[index].innerHTML;

        switch (true) {
            case cellA > cellB:
                return 1 * multiplier;
            case cellA < cellB:
                return -1 * multiplier;
            case cellA == cellB:
                return 0;
        }
    });

    // Remove old rows
    rows.forEach(function (row) {
        tableBody.removeChild(row);
    });

    // Reverse the direction
    directions[index] = direction === 'asc' ? 'desc' : 'asc';

    // Append new row
    newRows.forEach(function (newRow) {
        tableBody.appendChild(newRow);
    });
};

headers.forEach(function (header, index) {
    header.addEventListener('click', function () {
        sortColumn(index);
    });
});