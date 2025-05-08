from django.db import models
from property.models import Property
from user_profile.models import UserProfile, SellerProfile


class States(models.TextChoices):
   PENDING = 'PEND', 'Pending'
   ACCEPTED = 'ACCE', 'Accepted'
   REJECTED = 'REJ', 'Rejected'
   CONTINGENT = 'CONT', 'Contingent'


class Offer(models.Model):
   price = models.DecimalField(decimal_places=2, max_digits=20)
   expiration_date = models.DateField()
   state = models.CharField(
       max_length=4,
       choices=States.choices,
       default=States.PENDING
   )
   seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
   property = models.ForeignKey(Property, on_delete=models.CASCADE)


   def __str__(self):
       return f"{self.property_id} {self.price} ({self.id})"

