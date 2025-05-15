from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user_profile.forms import ProfileForm, SellerProfileForm
from user_profile.models import UserProfile


def register(request):
    # logged-in user can't access sign-up-page
    if request.user.is_authenticated:
        return redirect("property-index")

    # create a new user
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # save user and get user

            # create UserProfile and connect it to the new user
            UserProfile.objects.create(
                user=user, name=user.username  # Set name to username
            )

            return redirect("property-index")  # newly registered users go to homepage
    else:
        form = UserCreationForm()

    return render(request, "authentication/register.html", {"form": form})


def display_profile(request):
    return render(request, "profile/profile.html", context={})

def edit_profile(request):
    profile_instance, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect("display-profile")
    else:
        form = ProfileForm(instance=profile_instance)
    return render(request, "profile/edit_profile.html", {"form": form})

def create_seller_profile(request):
    if request.method == "POST":
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user.userprofile
            seller.save()
            return redirect("property-create")
    else:
        form = SellerProfileForm()

    return render(
        request,
        "authentication/seller.html",
        {
            "form": form,
            "user_profile": request.user.userprofile,
        },
    )


