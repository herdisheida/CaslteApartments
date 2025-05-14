import os.path

from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.db import models
from django.utils.text import slugify


def profile_pic_path(instance, filename):
    """
    Generates upload paths for:
    - UserProfile.image = SellerProfile.cover_img -> profile_pics/{user_id}/profile_img/{filename}
    - SellerProfile.logo -> profile_pics/{user_id}/logo/{filename}
    """
    user_profile = instance if isinstance(instance, UserProfile) else instance.user
    subfolder = "logo" if hasattr(instance, 'logo') else "profile_pic"

    user_name =  slugify(user_profile.name)
    user_id =  slugify(user_profile.id)
    return f'profile_pics/{user_name}_{user_id}/{subfolder}/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(default="../static/images/default_profile_pic.png", upload_to=profile_pic_path)

    def __str__(self):
        return f"{self.name} ({self.pk}) {self.user}"

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
    bio = models.TextField(max_length=600)
    logo = models.ImageField(upload_to=profile_pic_path)

    def __str__(self):
        return f"{self.user.name} ({self.pk})"
