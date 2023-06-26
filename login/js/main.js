// Get the search input and search button elements
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');

// Get the table body element
const tableBody = document.querySelector('#vacataire-table tbody');

// Add event listener to the search button
searchButton.addEventListener('click', () => {
    const searchText = searchInput.value.toLowerCase();

    // Loop through each table row and hide/show based on the search text
    for (const row of tableBody.rows) {
        const firstName = row.cells[0].textContent.toLowerCase();
        const lastName = row.cells[1].textContent.toLowerCase();

        if (firstName.includes(searchText) || lastName.includes(searchText)) {
            row.style.display = ''; // Show the row
        } else {
            row.style.display = 'none'; // Hide the row
        }
    }
});
document.getElementById('menu-btn').addEventListener('click', function() {
    document.querySelector('.container').classList.toggle('menu-open');
});
