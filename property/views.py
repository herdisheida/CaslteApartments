from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from property.models import Property, PropertyForm




def index(request):
    return render(request, 'property/properties.html', {
        'properties': Property.objects.all(),
    })

def get_property_by_id(request, id):
    # Get by database ID (proper way)
    property_obj = get_object_or_404(Property, pk=id)
    return render(request, 'property/property_details.html', {
        'property': property_obj
    })


# TODO: virkar ekki
def get_seller_by_property_id(request, property_id):
    try:
        # get the property object
        property_obj = get_property_by_id(request, property_id)

        # get seller_id from the property
        seller_id = property_obj['seller_id']

        # find matching seller
        seller = next(s for s in sellers if s['id'] == seller_id)

    except (KeyError, StopIteration) as e:
        raise Http404("Seller not found for this property") from e

    return render(request, 'profile/_seller_profile.html', {
        'seller': seller
    })


def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            save_property = form.save()
            return redirect('property_detail', pk=save_property.pk)
    else:
        form = PropertyForm()
    return render(request, 'property/create_property.html', {'form': form})