from django.shortcuts import render
from django import forms

# Create your views here.
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
        'is_sold': True,
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
        'is_sold': False,
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
        'is_sold': True,
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
        'is_sold': False,
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
        'is_sold': True,
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
        'is_sold': False,
        'seller_id': 1,
        'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bamboo_House_in_Sambava_Madagascar.JPG/1920px-Bamboo_House_in_Sambava_Madagascar.JPG",
        'bed': '5',
        'bath': '3',
        'size': '230m²',
        'when': '2002'
    }
]

def index(request):
    return render(request, 'property/properties.html', {
        'properties': properties
    })

def get_property_by_id(request, id):
    property = [x for x in properties if x['id'] == int(id)][0]
    return render(request, 'property/property_details.html', {
        'property': property
    })




class PropertyForm(forms.Form):
    street_name = forms.CharField(label='street_name')
    house_nr = forms.CharField(label='house_nr')
    city = forms.CharField(label='city')
    postal_code = forms.CharField(label='postal_code')

    building_type = forms.CharField(label='Type of building')
    price = forms.CharField(label='Price')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your description here...'}))
    year_built = forms.CharField(label='Built year')
    size = forms.CharField(label='Size')
    bedrooms = forms.CharField(label='Bedrooms')
    bathrooms = forms.CharField(label='Bathrooms')
    toilets = forms.CharField(label='Toilets')

def create_property(request):
    form = PropertyForm()
    return render(request, 'property/create_property.html', {'form': form})