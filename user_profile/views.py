from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'user_profile/profiles.html', {
        'profiles': profiles
    })

def get_profile_by_id(request):
    offer = [x for x in profile if x['id'] == id][0]
    return render(request, 'user_profile/profile_details.html', {
        'profile': profile
    })