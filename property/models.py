from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from user_profile.models import SellerProfile
from django.utils.text import slugify


def property_image_path(instance, filename):
    """Generates upload-path based on property address,
    for Property.preview_pic"""
    street = slugify(instance.street_name)
    house = slugify(instance.house_nr)      # convert "123A" to "123a"
    return f'property_images/{street}_{house}/preview/{filename}'

def property_gallery_path(instance, filename):
    """Matches a specific Property model's upload-path,
    for PropertyImages.image"""
    street = slugify(instance.property.street_name)
    house = slugify(instance.property.house_nr)
    return f'property_images/{street}_{house}/gallery/{filename}'


class BuildingTypes(models.TextChoices):
   APARTMENT = 'APARTMENT', 'Apartment'
   HOUSE = 'HOUSE', 'House'
   VILLA = 'VILLA', 'Villa'
   TOWNHOUSE = 'TOWNHOUSE', 'Townhouse'
   AREA = 'AREA', 'Area'

class Property(models.Model):
   street_name = models.CharField(max_length=100)
   house_nr = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   postal_code = models.CharField(max_length=100)
   seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
   building_type = models.CharField(
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
           MaxValueValidator(timezone.now().year)
       ]
   )
   size = models.DecimalField(max_digits=10, decimal_places=2)
   bedrooms = models.IntegerField()
   bathrooms = models.IntegerField()
   toilets = models.IntegerField()
   preview_pic = models.ImageField(upload_to=property_image_path)
   is_sold = models.BooleanField(default=False)
   listing_date = models.DateField(default=timezone.now, editable=False)

   def __str__(self):
       return f"{self.street_name} {self.house_nr} ({self.pk})"


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to=property_gallery_path)

    def __str__(self):
        return f"Image for {self.property}"