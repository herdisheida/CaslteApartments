from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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
    return render(request, 'profile/profile.html')


def seller_index(request):
    return render(request, 'authentication/seller.html')
