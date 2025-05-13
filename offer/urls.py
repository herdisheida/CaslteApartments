from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('display-submitted', views.display_submitted_offers, name='submitted-offer-index'),

    path('display-received', views.display_received_offers, name='received-offer-index'),


    # accept offer (by seller)
    # path('<int:offer_id>/accept', views.accept_offer, name='accept-offer'),

    # finalize offer (by user)
    path('payment/', views.payment, name='payment-index'),

    path('<int:property_id>/submit-offer/', views.submit_offer_prop, name='submit-offer'),
    ]
