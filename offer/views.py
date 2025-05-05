from django.shortcuts import render


# Create your views here.
offers = [
    {
        'id': 1,
        'price': 100000,
        'expiration_date':
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