# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
#
# from user_profile.forms.profile_form import ProfileForm
# from user_profile.models import UserProfile
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'authentication/signup.html', {
#         'form': form
#     })
#
# def profile(request):
#     user_profile = UserProfile.objects.get(user=request.user).first()
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=user_profile)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('profile')
#
#     return render(request, 'profile/profile.html', {
#         'form': ProfileForm(instance=user_profile),
#     })
#
#
# def seller_index(request):
#     return render(request, 'authentication/seller.html')
