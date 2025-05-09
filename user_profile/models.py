from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')

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
    logo = models.ImageField(default='images/default_profile_pic.png', upload_to='images/')

    def __str__(self):
        return self.user.name
