from django.shortcuts import render


# Create your views here.

def get_profile_by_id(request):
    offer = [x for x in offers if x['id'] == id][0]
    return render(request, 'profile/profile_details.html', {
        'profile': profile
    })