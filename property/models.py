
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator, validate_image_file_extension
import datetime

from user_profile.models import SellerProfile


class BuildingTypes(models.TextChoices):
   APARTMENT = 'APARTMENT', 'Apartment'
   HOUSE = 'HOUSE', 'House'
   VILLA = 'VILLA', 'Villa'
   TOWNHOUSE = 'TOWNHOUSE', 'Townhouse'
   AREA = 'AREA', 'Area'



# Create your models here.
class Property(models.Model):
   street_name = models.CharField(max_length=100)
   house_nr = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   postal_code = models.CharField(max_length=100)
   building_type = models.CharField(
       max_length=9,
       choices=BuildingTypes.choices,
       default=BuildingTypes.AREA
   )

   price = models.DecimalField(
       max_digits=12,
       decimal_places=2,
       validators=[MinValueValidator(0)]
   )
   description = models.TextField()
   year_built = models.IntegerField(
       validators=[
           MinValueValidator(1800),
           # MaxValueValidator(datetime.now().year)
       ]
   )
   size = models.DecimalField(max_digits=10, decimal_places=2)
   bedrooms = models.IntegerField()
   bathrooms = models.IntegerField()
   toilets = models.IntegerField()
   image = models.ImageField(
       default='images/no_image.jpg',
       upload_to='properties/',  # Changed from static/images/
   )
   seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
   is_sold = models.BooleanField(default=False)

   def __str__(self):
       return f"{self.street_name} {self.house_nr} ({self.pk})"


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'  # Or specify fields explicitly
        widgets = {
            'building_type': forms.Select(choices=BuildingTypes.choices),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write your description here...',
                'rows': 4
            }),
            'price': forms.NumberInput(attrs={
                'min': 0,
                'step': 100000,
                'placeholder': '0.00'
            }),
            'year_built': forms.NumberInput(attrs={
                'min': 1800,
                'max': datetime.datetime.now().year,
            }),
            'size': forms.NumberInput(attrs={
                'min': 0,
                'step': 0.1,
                'placeholder': '0.00'
            }),
            'bedrooms': forms.NumberInput(attrs={'min': 0}),
            'bathrooms': forms.NumberInput(attrs={'min': 0}),
            'toilets': forms.NumberInput(attrs={'min': 0}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['seller'].queryset = SellerProfile.objects.all()
        self.fields['building_type'].initial = BuildingTypes.AREA