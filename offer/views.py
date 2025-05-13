
from offer.models import Offer
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property
from user_profile.models import SellerProfile
from .forms import OfferForm
# Create your views here.

def display_submitted_offers(request):
    user_offers = Offer.objects.filter(buyer=request.user.userprofile)
    return render(request, 'offer/submitted_offer/offers.html', {
        'offers': user_offers,
    })


def display_received_offers(request):
    user_seller_profile = request.user.userprofile.sellerprofile
    offers = Offer.objects.filter(seller=user_seller_profile)
    return render(request, 'offer/received_offer/offers.html', {
        'received_offers': offers,
    })

def payment(request):
    return render(request, 'payment/payment.html', {
        'payment': payment
    })

def submit_offer_prop(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    seller = property_obj.seller
    buyer_profile = request.user.userprofile

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.seller = seller
            offer.buyer = buyer_profile
            offer.property = property_obj
            offer.save()
            return redirect('payment-index')  # or any success page
    else:
        form = OfferForm()

    return render(request, 'offer/submit_offer.html', {
        'form': form,
        'property': property_obj
    })