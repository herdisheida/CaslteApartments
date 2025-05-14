from django.contrib import admin

import offer.models

admin.site.register(offer.models.Offer)
admin.site.register(offer.models.Transaction)