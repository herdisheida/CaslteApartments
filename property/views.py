from django.shortcuts import render


# Create your views here.
properties = [
    {
        'id': 1,
    }
]

def index(request):
    return render(request, 'property/properties.html', {
        'properties': properties
    })

def get_property_by_id(request):
    property = [x for x in properties if x['id'] == id][0]
    return render(request, 'property/property_details.html', {
        'property': property
    })