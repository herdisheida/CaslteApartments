from django.shortcuts import render
from offer.models import Offer
# Create your views here.

def index(request):
    return render(request, 'offer/submitted_offer/offers.html', {
        'offers': Offer.objects.all(),
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })