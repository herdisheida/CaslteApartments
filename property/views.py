from offer.models import Offer
from property.forms import PropertyForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from property.models import Property, PropertyImages


def index(request):
    properties = Property.objects.all()

    # SEARCH
    search_query = request.GET.get("search")
    if search_query:
        properties = properties.filter(
            Q(street_name__icontains=search_query) | Q(city__icontains=search_query)
        )

    # FILTER
    postal_code = request.GET.get("postal_code")
    property_type = request.GET.get("building_type")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    availability = request.GET.getlist("availability")

    # Apply filters
    if postal_code and postal_code != "all":
        properties = properties.filter(postal_code=postal_code)
    if property_type and property_type != "all":
        properties = properties.filter(building_type=property_type)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if availability:
        status_filter = Q()
        if "for-sale" in availability:
            status_filter |= Q(is_sold=False)
        if "is-sold" in availability:
            status_filter |= Q(is_sold=True)
        properties = properties.filter(status_filter)

    # Get unique values for filter dropdowns
    unique_postal_codes = (
        Property.objects.values_list("postal_code", flat=True)
        .distinct()
        .order_by("postal_code")
    )
    unique_types = (
        Property.objects.values_list("building_type", flat=True)
        .distinct()
        .order_by("building_type")
    )

    # SORTING
    sort = request.GET.get("sort")
    if sort == "price_asc":
        properties = properties.order_by("price")
    elif sort == "price_desc":
        properties = properties.order_by("-price")
    elif sort == "street_asc":
        properties = properties.order_by("street_name")
    elif sort == "street_desc":
        properties = properties.order_by("-street_name")

    context = {
        "properties": properties,
        "unique_postal_codes": unique_postal_codes,
        "unique_types": unique_types,
        "current_sort": sort,
        "search_query": search_query,
    }
    return render(request, "property/properties.html", context)


def get_property_by_id(request, id):
    property_obj = get_object_or_404(Property, pk=id)

    # Get user's submitted offers
    user_submitted_offer_ids = []
    if request.user.is_authenticated:
        try:
            user_profile = request.user.userprofile
            user_submitted_offer_ids = Offer.objects.filter(
                buyer=user_profile
            ).values_list("property_id", flat=True)
        except Exception as e:
            print(f"An error occurred: {e}")
            user_submitted_offer_ids = []  # Default to an empty list if error occurs

    return render(
        request,
        "property/property_details.html",
        {
            "property": property_obj,
            "user_submitted_offer_ids": user_submitted_offer_ids,
        },
    )


def get_seller_by_property_id(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    seller = property_obj.seller
    properties = Property.objects.filter(seller=seller)

    return render(
        request,
        "profile/seller_profile.html",
        {"seller": seller, "properties": properties},
    )


def create_property(request):
    try:
        seller_profile = request.user.userprofile.sellerprofile
    except AttributeError:
        return redirect("become-seller")

    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save(commit=False)

            # get SellerProfile through UserProfile through User
            new_property.seller = seller_profile
            new_property.save()

            # handle multiple images
            for image in request.FILES.getlist("images"):
                PropertyImages.objects.create(property=new_property, image=image)
            return redirect("property-by-id", id=new_property.id)
    else:
        form = PropertyForm()
    return render(
        request,
        "property/create/create_property.html",
        {
            "form": form,
            "is_seller": hasattr(request.user.userprofile, "sellerprofile"),
        },
    )


def seller_profile(request, seller_id):
    seller = get_object_or_404(seller_profile, id=seller_id)
    return render(request, "profile/seller_profile.html", {"seller": seller})


def submit_offer(request):
    return render(request, "offer/submit_offer.html")
