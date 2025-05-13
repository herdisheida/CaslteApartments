
from offer.models import Offer
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property
from .forms import OfferForm
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

def submit_offer_prop(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.property = property_obj
            offer.save()
            return redirect('payment-index')  # or any success page
    else:
        form = OfferForm()

    return render(request, 'offer/submit_offer.html', {
        'form': form,
        'property': property_obj
    })