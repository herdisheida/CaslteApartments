from django import forms
import datetime
from property.models import Property, BuildingTypes, PropertyImages


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields = "__all__"


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ["is_sold", "listing_date", "seller"]
        widgets = {
            "building_type": forms.Select(choices=BuildingTypes.choices),
            "description": forms.Textarea(
                attrs={"placeholder": "Write your description here...", "rows": 4}
            ),
            "price": forms.NumberInput(
                attrs={
                    "min": 0,
                    "max": 999999999999,
                    "placeholder": "0.00"
                }
            ),
            "year_built": forms.NumberInput(
                attrs={
                    "min": 1800,
                    "max": datetime.datetime.now().year,
                }
            ),
            "size": forms.NumberInput(attrs={"min": 0, "placeholder": "0.00"}),
            "bedrooms": forms.NumberInput(attrs={"min": 0}),
            "bathrooms": forms.NumberInput(attrs={"min": 0}),
            "toilets": forms.NumberInput(attrs={"min": 0}),
            "preview_pic": forms.FileInput(attrs={"accept": "image/*"}),
        }
