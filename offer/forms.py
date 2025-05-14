from django import forms
from .models import Offer

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ('state', 'seller', 'property', 'buyer')
        widgets = {
            'expiration_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d'
            ),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['expiration_date'].input_formats = ['%Y-%m-%d']
        self.fields['creation_date'].input_formats = ['%Y-%m-%d']
