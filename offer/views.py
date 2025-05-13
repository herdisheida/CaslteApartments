from django.shortcuts import render
from offer.models import Offer
# Create your views here.

def display_submitted_offers(request):
    user_offers = Offer.objects.filter(buyer=request.user.userprofile)
    return render(request, 'offer/submitted_offer/offers.html', {
        'offers': user_offers,
    })


def display_received_offers(request):
    user_seller_profile = request.user.userprofile.sellerprofile
    offers = Offer.objects.filter(seller=user_seller_profile)
    return render(request, 'offer/submitted_offer/offers.html', {
        'received_offers': offers,
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })