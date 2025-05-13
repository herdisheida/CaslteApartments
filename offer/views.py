from django.shortcuts import render
from offer.models import Offer
# Create your views here.

def index(request):
    user_offers = Offer.objects.filter(buyer=request.user.userprofile)
    return render(request, 'offer/submitted_offer/offers.html', {
        'offers': user_offers,
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })