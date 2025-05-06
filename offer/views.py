from django.shortcuts import render
import datetime

# Create your views here.

offers = [
    {
        'id': 1,
        'price': 100000,
        'expiration_date': '29.12.2024',
        'state': ['pending'],
        'property_id': 1
    },
    {
        'id': 2,
        'price': 85000,
        'expiration_date': '15.01.2025',
        'state': ['accepted'],
        'property_id': 2
    },
    {
        'id': 3,
        'price': 120000,
        'expiration_date': '01.03.2025',
        'state': ['contingent', 'I want it at a higher price'],
        'property_id': 3
    },
    {
        'id': 4,
        'price': 95000,
        'expiration_date': '10.11.2024',
        'state': ['rejected'],
        'property_id': 4
    },
    {
        'id': 5,
        'price': 75000,
        'expiration_date': '05.02.2025',
        'state': ['finalized'],
        'property_id': 2
    },
    {
        'id': 6,
        'price': 110000,
        'expiration_date': '20.12.2024',
        'state': ['contingent', 'Waiting for financing approval'],
        'property_id': 5
    },
    {
        'id': 7,
        'price': 135000,
        'expiration_date': '14.04.2025',
        'state': ['pending'],
        'property_id': 6
    }
]


def index(request):
    return render(request, 'offer/offers.html', {
        'offers': offers
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