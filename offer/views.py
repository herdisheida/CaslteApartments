from django.shortcuts import render
from offer.models import Offer
# Create your views here.

def index(request):
    return render(request, 'offer/offers.html', {
        'offers': Offer.objects.all(),
    })

def get_offer_by_id(request):
    offer = [x for x in Offer.objects.all() if x['id'] == id][0]
    return render(request, 'offer/offer_details.html', {
        'offer': offer
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })