from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField()


class SellerType(models.TextChoices):
   INDIVIDUAL = 'INDIVIDUAL', 'Individual'
   AGENCY = 'AGENCY', 'Agency'

class SellerProfile(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=10,
        choices=SellerType.choices,
        default=SellerType.INDIVIDUAL
    )
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    logo = models.ImageField()