from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='offer-index'),

    # http://localhost:8000/id
    path('<int:id>', views.get_offer_by_id, name='offer-by-id'),

    # accept offer (by seller)
    # path('<int:offer_id>/accept', views.accept_offer, name='accept-offer'),

    # finalize offer (by user)
    path('payment/', views.payment, name='payment-index'),

path('<int:property_id>/submit-offer/', views.submit_offer_prop, name='submit-offer'),
]
