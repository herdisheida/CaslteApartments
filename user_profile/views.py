# from django.shortcuts import render
#
# from user_profile.models import UserProfile, SellerProfile
# from django.shortcuts import render, get_object_or_404
# from .models import UserProfile
#
# # Create your views here.
# def index(request):
#     return render(request, 'profile/profile.html', {
#         'profiles': UserProfile.objects.all(),
#     })
#
#
# def get_profile_by_id(request, id):
#     profile = get_object_or_404(UserProfile, id=id)
#     return render(request, 'profile/profile_details.html', {
#         'profile': profile
#     })



from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user_profile.forms.profile_form import ProfileForm
from user_profile.models import UserProfile
from .form import SellerProfileForm


def register(request):
    # logged-in user can't access sign-up-page
    if request.user.is_authenticated:
        return redirect('property-index')

    # create a new user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {
        'form': form
    })

def profile(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            profile_instance = form.save(commit=False)
            profile_instance.user = request.user

            if not user_profile.name:
                profile_instance.name = request.user.username # default profile-name is user-username

            profile_instance.save()
            return redirect('profile')

    return render(request, 'profile/profile.html', {
        'form': ProfileForm(instance=user_profile),
    })

#
# def seller_index(request):
#     return render(request, 'authentication/seller.html')
#

def create_seller_profile(request):
    if request.method == 'POST':
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user.userprofile
            seller.save()
            return redirect('property-create')
    else:
        form = SellerProfileForm()

    return render(request, 'authentication/seller.html', {
        'form': form,
        'user_profile': request.user.userprofile,
    })

