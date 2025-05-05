from django.shortcuts import render


# Create your views here.

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

def index(request):
    return render(request, 'user_profile/profiles.html', {
        'profiles': profiles
    })

def get_profile_by_id(request):
    offer = [x for x in profile if x['id'] == id][0]
    return render(request, 'user_profile/profile_details.html', {
        'profile': profile
    })