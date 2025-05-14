from user_profile.models import UserProfile, SellerProfile
from django.forms import ModelForm
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'image']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'profile_image': forms.FileInput(attrs={
        #         'accept': 'image/*',
        #         'class': 'form-control',
        #     }),
        # }


class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        exclude = ('user',)
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'write your bio here...'}),
        }
