from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models


def profile_pic_path(instance, filename):
    """
    Upload paths for:
    - UserProfile.image → `profile_pics/user_<ID>/profile_pic/<filename>`
    - SellerProfile.cover_img → `profile_pics/user_<ID>/cover_img/<filename>`
    - SellerProfile.logo → `profile_pics/user_<ID>/logo/<filename>`
    """
    user_profile = instance if isinstance(instance, UserProfile) else instance.user
    user_id = user_profile.id

    if hasattr(instance, 'logo'):
        subfolder = "logo"
    elif hasattr(instance, 'cover_img'):
        subfolder = "cover_img"
    else:
        subfolder = "profile_pic"
    return f"profile_pics/user_{user_id}/{subfolder}/{filename}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(
        default="../static/images/default_profile_pic.png", upload_to=profile_pic_path
    )

    def __str__(self):
        return f"{self.name} ({self.pk}) {self.user}"


class SellerType(models.TextChoices):
    INDIVIDUAL = "Individual", "Individual"
    AGENCY = "Real Estate Agency", "Agency"


class SellerProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    cover_img = models.ImageField(upload_to=profile_pic_path)
    type = models.CharField(choices=SellerType.choices, default=SellerType.INDIVIDUAL)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    bio = models.TextField(max_length=600)
    logo = models.ImageField(upload_to=profile_pic_path)

    def __str__(self):
        return f"{self.user.name} ({self.pk})"
