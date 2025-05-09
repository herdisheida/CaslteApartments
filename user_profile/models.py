from django.db import models
from django.utils.text import slugify

def profile_pic_path(instance, filename):
    """Generates upload-path based on users name and id"""
    name = slugify(instance.name)
    return f'profile_pics/{name}/{filename}'


# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to=profile_pic_path)

    def __str__(self):
        return f"{self.name} {self.image}"

class SellerType(models.TextChoices):
   INDIVIDUAL = 'Individual', 'Individual'
   AGENCY = 'Real Estate Agency', 'Agency'

class SellerProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    type = models.CharField(
        choices=SellerType.choices,
        default=SellerType.INDIVIDUAL
    )
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    logo = models.ImageField(upload_to=profile_pic_path)

    def __str__(self):
        return self.user.name

from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # possibly more fields like phone, profile_image, etc.

    def __str__(self):
        return self.name