// Handle popup visibility
function showFilterPopup() {
    document.getElementById('filter-popup').style.display = 'flex';
}





/* SORT | ORDER BY */
// Initialize sorting state
let currentSortField = null;
let currentSortDirection = 'asc';

document.querySelectorAll('.sort-arrow-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        const target = e.currentTarget;
        const parentGroup = target.closest('.sort-group-order');
        const isPriceGroup = parentGroup.querySelector('.sort-label-order').textContent === 'Price Range';

        // Remove active class and reset other direction buttons
        document.querySelectorAll('.sort-arrow-btn').forEach(btn => {
            btn.classList.remove('active-order');
            const btnParent = btn.closest('.sort-group-order');
            if (btnParent !== parentGroup && (btn.textContent === '↑' || btn.textContent === '↓')) {
                btn.textContent = '↑↓'; // Reset inactive groups
            }
        });

        target.classList.add('active-order');

        // Update sort field
        currentSortField = isPriceGroup ? 'price' : 'name';

        // Check if the clicked button is a direction button
        const isDirectionButton = ['↑', '↓', '↑↓'].includes(target.textContent);

        if (isDirectionButton) {
            // Toggle direction
            currentSortDirection = currentSortDirection === 'asc' ? 'desc' : 'asc';
        } else {
            // Reset to ascending when switching fields
            currentSortDirection = 'asc';
        }

        // Update active group's direction button
        const directionBtn = parentGroup.querySelector('.sort-arrow-btn:not(.sort-label-order)'); // Adjust selector as needed
        if (directionBtn) {
            directionBtn.textContent = currentSortDirection === 'asc' ? '↑' : '↓';
        }

        sort(); // Call your sort function
    });
});

// Sort function
const sort = () => {
    const propertyElements = [...document.querySelectorAll('[data-price][data-name]')]; // Use correct selector
    const container = document.querySelector('.property-container'); // Changed to actual container

    if (!propertyElements.length || !container) {
        console.error('No properties or container found');
        return;
    }

    propertyElements.sort((a, b) => {
        const isPriceSort = currentSortField === 'price';
        const modifier = currentSortDirection === 'asc' ? 1 : -1;

        try {
            const valueA = isPriceSort ?
                parseInt(a.dataset.price) :
                a.dataset.name.toLowerCase();

            const valueB = isPriceSort ?
                parseInt(b.dataset.price) :
                b.dataset.name.toLowerCase();

            if (isPriceSort) {
                return (valueA - valueB) * modifier;
            }
            return valueA.localeCompare(valueB) * modifier;

        } catch (error) {
            console.error('Sorting error:', error);
            return 0;
        }
    });

    // Clear and re-insert sorted elements
    container.innerHTML = '';
    const row = document.createElement('div');
    row.className = 'row row-cols-1 row-cols-md-2 g-4'; // Create single row

    propertyElements.forEach((element, index) => {
        const col = document.createElement('div');
        col.className = 'col mb-4'; // Create column with bottom margin
        col.appendChild(element.cloneNode(true));
        row.appendChild(col);
    });
    container.appendChild(row); // add the complete row to container
};