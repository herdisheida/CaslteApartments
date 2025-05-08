from django.shortcuts import render
# from offer.models import Offer
# Create your views here.

sellers = [
   {"name": "Alice Johnson", "type": "individual"},
   {"name": "BrightHome Realty", "type": "real estate agent"},
   {"name": "John Smith", "type": "individual"},
   {"name": "DreamSpace Agency", "type": "real estate agent"},
   {"name": "Linda Tran", "type": "individual"},
   {"name": "UrbanNest Realtors", "type": "real estate agent"},
   {"name": "Michael Brown", "type": "individual"},
   {"name": "Elite Realty Group", "type": "real estate agent"},
]

import  random
# Shuffle the sellers list to assign randomly
random.shuffle(sellers)


offers = [
   {
       'id': 1,
       'price': 100000,
       'expiration_date': '29.12.2024',
       'state': ['pending'],
       'property_id': 1,
       'seller': sellers[0],
       'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Katsura_Imperial_Villa_in_Spring.jpg/1920px-Katsura_Imperial_Villa_in_Spring.jpg",
   },
   {
       'id': 2,
       'price': 85000,
       'expiration_date': '15.01.2025',
       'state': ['accepted'],
       'property_id': 2,
       'seller': sellers[1],
       'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/8A%2C_Bulevardul_Aviatorilor_%2C_Bucharest_%28Romania%29.jpg/1920px-8A%2C_Bulevardul_Aviatorilor_%2C_Bucharest_%28Romania%29.jpg"
   },
   {
       'id': 3,
       'price': 120000,
       'expiration_date': '01.03.2025',
       'state': ['contingent', 'I want it at a higher price'],
       'property_id': 3,
       'seller': sellers[2],
       'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/16%2C_Calea_Doroban%C8%9Bilor%2C_Bucharest_%28Romania%29_1.jpg/1920px-16%2C_Calea_Doroban%C8%9Bilor%2C_Bucharest_%28Romania%29_1.jpg"
   },
   {
       'id': 4,
       'price': 95000,
       'expiration_date': '10.11.2024',
       'state': ['rejected'],
       'property_id': 4,
       'seller': sellers[3],
       'image': "https://upload.wikimedia.org/wikipedia/commons/6/6a/248_Ashley_Ave_-_2017.jpg"
   },
   {
       'id': 5,
       'price': 75000,
       'expiration_date': '05.02.2025',
       'state': ['finalized'],
       'property_id': 2,
       'seller': sellers[4],
       'image': "https://upload.wikimedia.org/wikipedia/commons/f/f7/Casa_Assan_1.jpg"
   },
   {
       'id': 6,
       'price': 110000,
       'expiration_date': '20.12.2024',
       'state': ['contingent', 'Waiting for financing approval'],
       'property_id': 5,
       'seller': sellers[5],
       'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Cam0492_Habitation_de_Pouss.jpg/2560px-Cam0492_Habitation_de_Pouss.jpg"
   },
   {
       'id': 7,
       'price': 135000,
       'expiration_date': '14.04.2025',
       'state': ['pending'],
       'property_id': 6,
       'seller': sellers[6],
       'image': "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bamboo_House_in_Sambava_Madagascar.JPG/1920px-Bamboo_House_in_Sambava_Madagascar.JPG"
   }
]


def index(request):
    return render(request, 'offer/offers.html', {
        #'offers': Offer.objects.all(),
        'offers': offers,
    })

def get_offer_by_id(request):
    offer = [x for x in offers if x['id'] == id][0]
    return render(request, 'offer/offer_details.html', {
        'offer': offer
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })