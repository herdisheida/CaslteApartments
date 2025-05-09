from django.contrib import admin

from user_profile.models import UserProfile, SellerProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(SellerProfile)