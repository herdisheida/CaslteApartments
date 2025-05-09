from django.urls import path
from . import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='property-index'),
    path('<int:id>', views.get_property_by_id, name='property-by-id'),
    path('property/<int:property_id>/seller/', views.get_seller_by_property_id, name='seller-by-property'),


    path('create/', views.create_property, name='property-create-index'),
    path('create/success/', views.property_create_success, name='property-create-success'),

    # TODO: seller_profile link index
    # path('<int:id>/seller', views.get_seller_by_property_id, name='seller-profile-index'),
]