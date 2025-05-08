from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

# Create your models here.
class Property(models.Model):
    street_name = models.CharField(max_length=100)
    house_nr = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    building_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    description = models.TextField()
    year_built = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            # TODO: MaxValueValidator(datetime.now().year)
        ]
    )
    size = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    toilets = models.IntegerField()


class PropertyForm(forms.Form):
    street_name = forms.CharField(label='street_name')
    house_nr = forms.CharField(label='house_nr')
    city = forms.CharField(label='city')
    postal_code = forms.CharField(label='postal_code')

    building_type = forms.CharField(label='Type of building')

    price = forms.DecimalField(
        label='Price',
        max_digits=12,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'min': 0,
            'max': 100000000000000,
            'step': 100000,
            'placeholder': '0.00'
        }),
        validators=[MinValueValidator(0)]
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your description here...',
            'rows': 4
        })
    )

    year_built = forms.IntegerField(
        label='Built Year',
        widget=forms.NumberInput(attrs={
            'min': 1800,
            'max': datetime.datetime.now().year,
        }),
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )

    size = forms.DecimalField(
        label='Size (m²)',
        max_digits=7,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'min': 0,
            'step': 0.1,
            'placeholder': '0.00'
        }),
        validators=[MinValueValidator(0)]
    )

    bedrooms = forms.IntegerField(
        label='Bedrooms',
        widget=forms.NumberInput(attrs={'min': 0}),
        validators=[MinValueValidator(0)],
    )

    bathrooms = forms.IntegerField(
        label='Bathrooms',
        widget=forms.NumberInput(attrs={'min': 0}),
        validators=[MinValueValidator(0)],
    )

    toilets = forms.IntegerField(
        label='Toilets',
        widget=forms.NumberInput(attrs={'min': 0}),
        validators=[MinValueValidator(0)],
    )

