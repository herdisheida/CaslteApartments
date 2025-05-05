from django.shortcuts import render


# Create your views here.
authentications = [
    {
        'id': 1
    }
]

def index(request):
    return render(request, 'authentication/authentications.html')

def get_authentication_by_id(request, id):
    authentication = [x for x in authentications if x['id'] == id][0]
    return render(request, 'authentication/login.html', {
        'authentication': authentication
    })