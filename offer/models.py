from django.db import models


class Offer(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=20)
    expiration_date = models.DateField()
    state = models.TextField()
    property_id = models.IntegerField()
    seller = models.IntegerField()
    image = models.ImageField()
