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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/signup.html', {
        'form': form
    })

def profile(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')

    return render(request, 'profile/profile.html', {
        'form': ProfileForm(instance=user_profile),
    })


def seller_index(request):
    return render(request, 'authentication/seller.html')
