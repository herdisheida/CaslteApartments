from django import forms
from django.utils import timezone
from offer.models import Offer, Transaction


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ('state', 'seller', 'property', 'buyer', 'contingent_msg')
        widgets = {
            'expiration_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                     'min': timezone.localdate().isoformat()
                },
                format='%Y-%m-%d'
            ),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': '0.00',
            }),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ('creation_date', 'offer')