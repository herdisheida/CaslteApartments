from django.db import models
from property.models import Property
from user_profile.models import UserProfile, SellerProfile


class States(models.TextChoices):
   PENDING = 'pending', 'Pending'
   ACCEPTED = 'accepted', 'Accepted'
   REJECTED = 'rejected', 'Rejected'
   CONTINGENT = 'contingent', 'Contingent'


class Offer(models.Model):
   price = models.DecimalField(decimal_places=2, max_digits=20)
   creation_date = models.DateTimeField(auto_now_add=True)
   expiration_date = models.DateField()
   state = models.CharField(
       max_length=10,
       choices=States.choices,
       default=States.PENDING
   )
   seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
   property = models.ForeignKey(Property, on_delete=models.CASCADE)
   buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


   def __str__(self):
       return f"{self.state} {self.price} ({self.id}) - Seller: {self.seller.user.name}- Buyer: {self.user.name}"

