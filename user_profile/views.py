from django.shortcuts import render

from user_profile.models import UserProfile, SellerProfile
from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, 'profile/profiles.html', {
        'profiles': UserProfile.objects.all(),
    })


def get_profile_by_id(request, id):
    profile = get_object_or_404(UserProfile, id=id)
    return render(request, 'profile/profile_details.html', {
        'profile': profile
    })

