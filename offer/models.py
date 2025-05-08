from django.db import models


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
   property_id = models.IntegerField()
