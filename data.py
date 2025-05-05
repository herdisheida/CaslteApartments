offers = [
    {
        'id': 1,
        'price': 100000,
        'expiration_date': '29.12.2024',
        'state': ['pending']
    },
    {
        'id': 2,
        'price': 85000,
        'expiration_date': '15.01.2025',
        'state': ['accepted']
    },
    {
        'id': 3,
        'price': 120000,
        'expiration_date': '01.03.2025',
        'state': ['contingent', 'I want it at a higher price']
    },
    {
        'id': 4,
        'price': 95000,
        'expiration_date': '10.11.2024',
        'state': ['rejected']
    },
    {
        'id': 5,
        'price': 75000,
        'expiration_date': '05.02.2025',
        'state': ['finalized']
    },
    {
        'id': 6,
        'price': 110000,
        'expiration_date': '20.12.2024',
        'state': ['contingent', 'Waiting for financing approval']
    },
    {
        'id': 7,
        'price': 135000,
        'expiration_date': '14.04.2025',
        'state': ['pending']
    }
]



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
        'is_sold': False,
        'seller_id': 1,
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
        'is_sold': True,
        'seller_id': 2,
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
        'is_sold': False,
        'seller_id': 3,
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
        'is_sold': True,
        'seller_id': 1,
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
        'is_sold': False,
        'seller_id': 2,
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
        'is_sold': True,
        'seller_id': 3,
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
        'is_sold': False,
        'seller_id': 1,
    }
]



users = [
    {
        'user_ID': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'password': 'SecurePass123!',
        'seller_ID': 1001  # Seller
    },
    {
        'user_ID': 2,
        'name': 'Alice Smith',
        'email': 'alice.smith@example.com',
        'password': 'AlicePass456!',
        'seller_ID': None  # Regular user
    },
    {
        'user_ID': 3,
        'name': 'Bob Johnson',
        'email': 'bob.johnson@example.com',
        'password': 'BobsPassword789!',
        'seller_ID': 1002  # Seller
    },
    {
        'user_ID': 4,
        'name': 'Emma Wilson',
        'email': 'emma.wilson@example.net',
        'password': 'EmmaPass321!',
        'seller_ID': None  # Regular user
    },
    {
        'user_ID': 5,
        'name': 'Michael Brown',
        'email': 'michael.b@example.org',
        'password': 'MikePass654!',
        'seller_ID': 1003  # Seller
    },
    {
        'user_ID': 6,
        'name': 'Sarah Davis',
        'email': 'sarah.davis@example.com',
        'password': 'SarahPass987!',
        'seller_ID': None  # Regular user
    },
    {
        'user_ID': 7,
        'name': 'David Lee',
        'email': 'david.lee@example.net',
        'password': 'DavidPass246!',
        'seller_ID': None  # Regular user
    }
]