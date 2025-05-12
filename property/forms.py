from django import forms
import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone
from property.models import Property, BuildingTypes, PropertyImages
from user_profile.models import SellerProfile


class PropertyImageForm(forms.ModelForm):

    class Meta:
        model = PropertyImages
        fields = '__all__'

class PropertyForm(forms.ModelForm):

    # TODO: þegar við bætum user við í kerfið
    # def __init__(self, *args, **kwargs): # get curr user
    #     self.user = kwargs.pop('user', None)
    #     super(PropertyForm, self).__init__(*args, **kwargs)
    #
    #     # user is found
    #     if self.user:
    #         self.fields['seller'].initial = self.user.sellerprofile
    #         # Make the field read-only
    #         self.fields['seller'].widget.attrs['readonly'] = True
    #         self.fields['seller'].widget.attrs['disabled'] = True


    # listing_date = forms.DateField(
    #     widget=forms.DateInput(attrs={'readonly': True}),
    #     initial=timezone.now().date()
    # )
    class Meta:
        model = Property
        exclude = ['is_sold', 'listing_date']
        # exclude = ['is_sold', 'seller'] # TODO add the seller later
        fields = '__all__'
        widgets = {
            'building_type': forms.Select(choices=BuildingTypes.choices),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write your description here...',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'min': 0,
                'placeholder': '0.00'
            }),
            'year_built': forms.NumberInput(attrs={
                'min': 1800,
                'max': datetime.datetime.now().year,
            }),
            'size': forms.NumberInput(attrs={
                'min': 0,
                'placeholder': '0.00'
            }),
            'bedrooms': forms.NumberInput(attrs={'min': 0}),
            'bathrooms': forms.NumberInput(attrs={'min': 0}),
            'toilets': forms.NumberInput(attrs={'min': 0}),
            'preview_pic': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def clean_year_built(self):
        year_built = self.cleaned_data.get('year_built')
        current_year = timezone.now().year
        if year_built < 1800:
            raise forms.ValidationError("Year built cannot be before 1800")
        if year_built > current_year:
            raise forms.ValidationError("Year built cannot be in the future")
        return year_built

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be positive")
        return price


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].queryset = SellerProfile.objects.all()
        self.fields['building_type'].initial = BuildingTypes.AREA


