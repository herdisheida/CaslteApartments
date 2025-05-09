from django.shortcuts import render

from user_profile.models import UserProfile, SellerProfile


# Create your views here.
def index(request):
    return render(request, 'profile/profiles.html', {
        'profiles': UserProfile.objects.all(),
    })

def get_profile_by_id(request):
    offer = [x for x in UserProfile.objects.all() if x['id'] == id][0]
    return render(request, 'profile/profile_details.html', {
        'profile': profiles
    })