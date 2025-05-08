/* POP UP WINDOWS */
const displayFilters = () => {
    document.getElementById('filter-popup').style.display = 'flex';
}
const displayOrderBy = () => {
    document.getElementById('order-by-popup').style.display = 'flex';
}

const hidePopupWindows = () => {
    document.getElementById('order-by-popup').style.display = 'none';
    document.getElementById('filter-popup').style.display = 'none';
}

const showError = (message) => {
    const errorContainer = document.getElementById('error-container');
    errorContainer.innerHTML = `
        <div class="alert alert-danger">
            ${message}
        </div>
    `;
    errorContainer.classList.remove('d-none');
}




/* FILTERING */
const filter = () => {
    hidePopupWindows(); // close filter popup window

    // get filter values
    const postalCode = document.getElementById('postal-code').value.replace('postal-code-', '');
    const propertyType = document.getElementById('type').value.replace('type-', '');
    const minPrice = document.getElementById('minimum').value || 0;
    const maxPrice = document.getElementById('maximum').value || Infinity;
    const availabilityCheckboxes = document.querySelectorAll('[name="availability"]:checked');
    const availability = Array.from(availabilityCheckboxes).map(cb => cb.value);


    if (!(minPrice < maxPrice)) {
        showError("❌ Maximum price cannot be less than minimum price")
        return;  // Stop further execution
    }


    // clear previous errors
    document.getElementById('error-container').classList.add('d-none');
    // filter properties
    const filteredProperties = properties.filter(property => {
        const postalMatch = postalCode === 'all' ? true : property.postal_code === parseInt(postalCode);
        const typeMatch = propertyType === 'all' ? true : property.type === propertyType;
        const priceMatch = property.price >= minPrice && property.price <= maxPrice;
        const availabilityMatch = availability.length === 0 ? true :
            availability.includes(property.is_sold ? 'is-sold' : 'for-sale');

        return postalMatch && typeMatch && priceMatch && availabilityMatch; // inclusive filter
    });

    displayFilteredProperties(filteredProperties);
}

const displayFilteredProperties = (filteredProperties) => {
    const container = document.querySelector('.properties-container');
    container.innerHTML = '';

    if (filteredProperties.length === 0) {
        showError("No properties found!");
        return;
    }

    // Create Bootstrap grid container
    const row = document.createElement('div');
    row.className = 'row row-cols-1 row-cols-md-2 g-4'; // Bootstrap grid classes

    filteredProperties.forEach(property => {
        // Create column
        const col = document.createElement('div');
        col.className = 'col';

        // Create card
        const card = document.createElement('div');
        card.className = 'card h-100'; // h-100 for equal height

        // Create image section
        const imgDiv = document.createElement('div');
        imgDiv.className = 'card-img-top';
        imgDiv.style.cssText = 'height: 200px; background: url(' + property.image + ') center / cover no-repeat;';

        const badge = document.createElement('span');
        badge.className = 'badge bg-dark text-white m-2';
        badge.textContent = property.is_sold ? 'Sold' : 'For Sale';
        imgDiv.appendChild(badge);

        // Create card body
        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';

        // Header section
        const header = document.createElement('div');
        header.className = 'd-flex justify-content-between align-items-center mb-1';

        const title = document.createElement('h5');
        title.className = 'mb-0';
        title.textContent = property.street_name + ' ' + property.house_nr;

        const price = document.createElement('span');
        price.className = 'text-primary fw-bold';
        price.textContent = '$' + property.price.toLocaleString();

        header.appendChild(title);
        header.appendChild(price);

        // City text
        const city = document.createElement('small');
        city.className = 'text-muted d-block mb-2';
        city.textContent = property.city;

        // Link/description
        let bottomContent;
        if (window.location.pathname.includes('/properties/')) { // Check if detail page
            const description = document.createElement('p');
            description.textContent = property.description;
            bottomContent = description;
        } else {
            const link = document.createElement('a');
            link.className = 'btn btn-outline-primary btn-sm';
            link.href = `/property/${property.id}`; // Update with your actual URL pattern
            link.textContent = 'See More';
            bottomContent = link;
        }

        // Assemble card
        cardBody.appendChild(header);
        cardBody.appendChild(city);
        cardBody.appendChild(bottomContent);

        card.appendChild(imgDiv);
        card.appendChild(cardBody);

        col.appendChild(card);
        row.appendChild(col);
    });
    container.appendChild(row);
};




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