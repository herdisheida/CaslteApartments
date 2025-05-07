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

properties = [
    {
        'id': 1,
        'street_name': 'Baker Street',
        'house_nr': '221B',
        'city': 'London',
        'postal_code': 3000,
        'description': 'Historic apartment with classic British charm',
        'type': 'Apartment',
        'listing_price': 5000000,
        'listing_date': '30.12.2025',
        'is_sold': false,
        'seller_id': 1,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Katsura_Imperial_Villa_in_Spring.jpg/1920px-Katsura_Imperial_Villa_in_Spring.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002',
    },
    {
        'id': 2,
        'street_name': 'Fifth Avenue',
        'house_nr': '1001',
        'city': 'New York',
        'postal_code': 10001,
        'description': 'Luxury penthouse with Central Park views',
        'type': 'Penthouse',
        'listing_price': 15000000,
        'listing_date': '15.01.2026',
        'is_sold': true,
        'seller_id': 2,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/16%2C_Calea_Doroban%C8%9Bilor%2C_Bucharest_%28Romania%29_1.jpg/1920px-16%2C_Calea_Doroban%C8%9Bilor%2C_Bucharest_%28Romania%29_1.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'

    },
    {
        'id': 3,
        'street_name': 'Champs-Élysées',
        'house_nr': '72',
        'city': 'Paris',
        'postal_code': 75008,
        'description': 'Elegant Haussmannian-style villa',
        'type': 'Villa',
        'listing_price': 9000000,
        'listing_date': '10.03.2025',
        'is_sold': false,
        'seller_id': 3,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/8A%2C_Bulevardul_Aviatorilor_%2C_Bucharest_%28Romania%29.jpg/1920px-8A%2C_Bulevardul_Aviatorilor_%2C_Bucharest_%28Romania%29.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    },
    {
        'id': 4,
        'street_name': 'Shibuya Crossing',
        'house_nr': '5-6',
        'city': 'Tokyo',
        'postal_code': 1500041,
        'description': 'Modern high-rise condo with smart home tech',
        'type': 'Condo',
        'listing_price': 3500000,
        'listing_date': '22.09.2024',
        'is_sold': true,
        'seller_id': 1,
        'image': "https://upload.wikimedia.org/wikipedia/commons/6/6a/248_Ashley_Ave_-_2017.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    },
    {
        'id': 5,
        'street_name': 'Palm Jumeirah',
        'house_nr': 'Villa 12',
        'city': 'Dubai',
        'postal_code': 00000,
        'description': 'Private beachfront mansion with infinity pool',
        'type': 'Mansion',
        'listing_price': 25000000,
        'listing_date': '05.05.2025',
        'is_sold': false,
        'seller_id': 2,
        'image': "https://upload.wikimedia.org/wikipedia/commons/f/f7/Casa_Assan_1.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    },
    {
        'id': 6,
        'street_name': 'Bondi Beach',
        'house_nr': '42',
        'city': 'Sydney',
        'postal_code': 2026,
        'description': 'Beachside cottage with ocean views',
        'type': 'House',
        'listing_price': 4200000,
        'listing_date': '18.07.2024',
        'is_sold': true,
        'seller_id': 3,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Cam0492_Habitation_de_Pouss.jpg/2560px-Cam0492_Habitation_de_Pouss.jpg",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    },
    {
        'id': 7,
        'street_name': 'Unter den Linden',
        'house_nr': '77',
        'city': 'Berlin',
        'postal_code': 10117,
        'description': 'Industrial-chic loft in city center',
        'type': 'Loft',
        'listing_price': 2800000,
        'listing_date': '01.11.2025',
        'is_sold': false,
        'seller_id': 1,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bamboo_House_in_Sambava_Madagascar.JPG/1920px-Bamboo_House_in_Sambava_Madagascar.JPG",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    }
]

    // TODO: tengja í data base
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


    // Clear previous errors
    document.getElementById('error-container').classList.add('d-none');

    // filter properties
    const filteredProperties = properties.filter(property => {
        const postalMatch = postalCode === 'all' ? true : property.postal_code === parseInt(postalCode);
        const typeMatch = propertyType === 'all' ? true : property.type === propertyType;
        const priceMatch = property.listing_price >= minPrice && property.listing_price <= maxPrice;
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
        showError("No properties found!")
        return;
    }

    filteredProperties.forEach(property => {
        const card = document.createElement('div');
        card.className = 'card';

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
        price.textContent = '$' + property.listing_price.toLocaleString();

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
            link.href = `/properties/${property.id}`; // Update with your actual URL pattern
            link.textContent = 'See More';
            bottomContent = link;
        }

        // Assemble card
        cardBody.appendChild(header);
        cardBody.appendChild(city);
        cardBody.appendChild(bottomContent);

        card.appendChild(imgDiv);
        card.appendChild(cardBody);

        container.appendChild(card);
    });
};






const sort = () => {

    hidePopupWindows()
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