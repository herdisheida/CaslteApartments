from user_profile.models import UserProfile
from django.forms import ModelForm
from django import forms
from user_profile import models

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'id')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'form-control',
            }),
        }