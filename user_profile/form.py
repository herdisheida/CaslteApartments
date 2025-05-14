from user_profile.models import SellerProfile
from django import forms

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        exclude = ('user',)
        widgets = {
            'bio': forms.Textarea(attrs={'placeholder': 'write your bio here...'}),
        }
