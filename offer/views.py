from django.contrib import messages

from offer.models import Offer, States
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property
from .forms import OfferForm
from django.utils import timezone


def display_submitted_offers(request):
    now = timezone.now()
    submitted_offers = Offer.objects.filter(
        buyer=request.user.userprofile,
        expiration_date__gte=now, # don't display expired offers
    )
    return render(request, 'offer/submitted_offer/offers.html', {
        'offers': submitted_offers,
    })

def display_received_offers(request):
    now = timezone.now()
    received_offers = Offer.objects.filter(
        seller=request.user.userprofile.sellerprofile,
        expiration_date__gt=now # don't display expired offers
    )
    return render(request, 'offer/received_offer/offers.html', {
        'offers': received_offers,
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
            return redirect('submitted-offer-indexu')
    else:
        form = OfferForm()

    return render(request, 'offer/submit_offer.html', {
        'form': form,
        'property': property_obj
    })


def update_offer_state(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)

    if offer.seller != request.user.userprofile.sellerprofile:
        messages.error(request, "You don't have permission to update this offer")
        return redirect('received-offer-index')

    if request.method == 'POST':
        new_state = request.POST.get('offer-state')
        contingent_msg = request.POST.get('contingent-reason', '').strip()

        if new_state == 'accept':
            offer.state = States.ACCEPTED
            offer.contingent_msg = None
            messages.success(request, "Offer accepted successfully")



        elif new_state == 'contingent':
            if not contingent_msg:
                messages.error(request, "Please provide a reason for contingency")
                return redirect('received-offer-index') # go back if no contingent msg was input
            offer.state = States.CONTINGENT
            offer.contingent_msg = contingent_msg
            messages.success(request, "Offer marked as contingent")

        offer.save()
        return redirect('received-offer-index')

    return redirect('received-offer-index')