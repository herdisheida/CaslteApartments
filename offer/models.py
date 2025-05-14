from django.core.validators import MinValueValidator
from django.db import models
from property.models import Property
from user_profile.models import UserProfile, SellerProfile

class States(models.TextChoices):
   PENDING = 'pending', 'Pending'
   ACCEPTED = 'accepted', 'Accepted'
   REJECTED = 'rejected', 'Rejected'
   CONTINGENT = 'contingent', 'Contingent'
   FINALIZED = 'finalized', 'Finalized'

class Offer(models.Model):
   price = models.DecimalField(
       max_digits=12,
       decimal_places=2,
       validators=[MinValueValidator(0)]
   )
   creation_date = models.DateField(auto_now_add=True)
   expiration_date = models.DateField()
   state = models.CharField(
       max_length=10,
       choices=States.choices,
       default=States.PENDING
   )
   seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
   property = models.ForeignKey(Property, on_delete=models.CASCADE)
   buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
   contingent_msg = models.TextField(blank=True, null=True, default=None)

   class Meta:
       ordering = ['-creation_date']

   def __str__(self):
       return f"{self.state} ({self.id}) | Property: {self.property.street_name} → Seller: {self.seller.user.name} → Buyer: {self.buyer.name}"



class Transaction(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.PROTECT)
    street_name = models.CharField(max_length=100)
    house_nr = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    national_id = models.IntegerField() # isl. kennitala

    class Meta:
        ordering = ['-creation_date']

    def __str__(self):
        return f"TX-{self.id} | {self.offer.property.street_name} → {self.offer.seller} (${self.offer.price})"
