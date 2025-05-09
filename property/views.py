from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from property.models import Property, PropertyForm
from django.db.models import Q

from django.shortcuts import get_object_or_404, render
from property.models import Property
from user_profile.models import Seller


def index(request):
    properties = Property.objects.all()

    # FILTER
    # Get filter parameters from URL
    postal_code = request.GET.get('postal_code')
    property_type = request.GET.get('building_type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    availability = request.GET.getlist('availability')

    # Apply filters
    if postal_code and postal_code != 'all':
        properties = properties.filter(postal_code=postal_code)
    if property_type and property_type != 'all':
        properties = properties.filter(building_type=property_type)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    if availability:
        status_filter = Q()
        if 'for-sale' in availability:
            status_filter |= Q(is_sold=False)
        if 'is-sold' in availability:
            status_filter |= Q(is_sold=True)
        properties = properties.filter(status_filter)

    # Get unique values for filter dropdowns
    unique_postal_codes = Property.objects.values_list('postal_code', flat=True).distinct()
    unique_types = Property.objects.values_list('building_type', flat=True).distinct()

    # SORTING
    sort = request.GET.get('sort')
    if sort == 'price_asc':
        properties = properties.order_by('price')
    elif sort == 'price_desc':
        properties = properties.order_by('-price')
    elif sort == 'street_asc':
        properties = properties.order_by('street_name')
    elif sort == 'street_desc':
        properties = properties.order_by('-street_name')

    context = {
        'properties': properties,
        'unique_postal_codes': unique_postal_codes,
        'unique_types': unique_types,
        'current_sort': sort,
    }
    return render(request, 'property/properties.html', context)


def get_property_by_id(request, id):
    # Get by database ID (proper way)
    property_obj = get_object_or_404(Property, pk=id)
    return render(request, 'property/property_details.html', {
        'property': property_obj
    })


def get_seller_by_property_id(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    seller = property_obj.seller
    properties = Property.objects.filter(seller=seller)

    return render(request, 'profile/_seller_profile.html', {
        'seller': seller,
        'properties': properties
    })


def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property-create-success')
    else:
        form = PropertyForm()
    return render(request, 'property/create/create_property.html', {'form': form})

def property_create_success(request):
    return render(request, 'property/create/success.html')

def seller_profile(request, seller_id):
    seller = get_object_or_404(seller_profile, id=seller_id)
    return render(request, 'profile/_seller_profile.html', {'seller': seller})

