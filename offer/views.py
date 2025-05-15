from django.contrib import messages
from offer.models import Offer, States
from django.shortcuts import render, redirect, get_object_or_404
from property.models import Property
from offer.forms import OfferForm, TransactionForm
from django.utils import timezone


def clear_messages(request):
    """clear any existing messages before processing"""
    storage = messages.get_messages(request)
    storage.used = True

def display_submitted_offers(request):
    submitted_offers = Offer.objects.filter(
        buyer=request.user.userprofile,
    )
    return render(
        request,
        "offer/submitted_offer/offers.html",
        {"offers": submitted_offers, "now": timezone.now()},
    )


def display_received_offers(request):
    received_offers = Offer.objects.filter(
        seller=request.user.userprofile.sellerprofile,
    )
    return render(
        request,
        "offer/received_offer/offers.html",
        {"offers": received_offers, "now": timezone.now()},
    )


def submit_offer(request, property_id):
    """Buyers (all users) can submit a purchase offer to a specific property."""
    property_obj = get_object_or_404(Property, id=property_id)
    seller_obj = property_obj.seller
    buyer_profile_obj = request.user.userprofile

    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.seller = seller_obj
            offer.buyer = buyer_profile_obj
            offer.property = property_obj
            offer.save()

            return redirect("submit-offer-success")
    else:
        form = OfferForm()

    return render(
        request, "offer/submit_offer.html", {"form": form, "property": property_obj}
    )

def submit_offer_success(request):
    return render(request, "offer/submitted_offer/_submit_success.html")

def respond_to_offer(request, offer_id):
    """Sellers responding to submitted offers"""
    clear_messages(request)

    offer = get_object_or_404(Offer, id=offer_id)

    # permission check - only the seller can update
    if offer.seller != request.user.userprofile.sellerprofile:
        messages.error(request, "You don't have permission to update this offer")
        return redirect("received-offer-index")

    if request.method == "POST":
        try:
            new_state = request.POST.get("offer-state")
            contingent_msg = request.POST.get("contingent-reason", "").strip()
            reject_msg = request.POST.get("reject-reason", "").strip()

            if new_state == "accept":
                offer.state = States.ACCEPTED
                offer.contingent_msg = None

                # property is considered sold
                offer.property.is_sold = True
                offer.property.save()
                messages.success(request, "Offer accepted successfully")

            elif new_state == "reject":
                offer.state = States.REJECTED
                offer.contingent_msg = reject_msg if reject_msg else None
                messages.success(request, "Offer rejected successfully")

            elif new_state == "contingent":
                if not contingent_msg:
                    messages.error(request, "Please provide a reason for contingency")
                    return render(
                        request,
                        "offer/received_offer/offers.html",
                        {
                            "offers": [offer],
                            "now": timezone.now(),
                            "show_contingent": True,
                        },
                    )
                offer.state = States.CONTINGENT
                offer.contingent_msg = contingent_msg

                # property is considered sold
                offer.property.is_sold = True
                offer.property.save()
                messages.success(request, "Offer marked as contingent")

            offer.save()
            return render(
                request,
                "offer/received_offer/offers.html",
                {
                    "offers": [offer],
                    "now": timezone.now(),
                },
            )
        except Exception as e:
            messages.error(request, f"Error updating offer: {str(e)}")
            return redirect("received-offer-index")
    return redirect("received-offer-index")


def payment(request, offer_id):
    """Buyers (all users) can finalize their purchase offers after sellers accept them"""
    clear_messages(request)
    current_offer = get_object_or_404(Offer, id=offer_id)

    # user who finalizes has to be the same as the one who submitted
    if current_offer.buyer != request.user.userprofile:
        messages.error(request, "You don't have permission to update this offer")
        return redirect("submitted-offer-index")

    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            try:
                transaction = form.save(commit=False)
                transaction.offer = current_offer
                transaction.save()

                current_offer.state = States.FINALIZED
                current_offer.save()

                return redirect("payment-success")

            except Exception as e:
                messages.error(request, f"Error creating transaction: {str(e)}")
    else:
        form = TransactionForm()
    return render(
        request, "payment/payment.html", {"form": form, "offer": current_offer}
    )

def payment_success(request):
    return render(request, "payment/_payment_success.html")
