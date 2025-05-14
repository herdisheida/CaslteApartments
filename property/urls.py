from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='property-index'),

    path('<int:id>', views.get_property_by_id, name='property-by-id'),

    path('<int:property_id>/seller/', views.get_seller_by_property_id, name='seller-by-property'),

    path('create/', views.create_property, name='property-create'),
]
