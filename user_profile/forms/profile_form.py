from user_profile.models import UserProfile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'id')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),

        }