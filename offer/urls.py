from django.urls import path
from . import views

urlpatterns = [
    path('display-submitted', views.display_submitted_offers, name='submitted-offer-index'),

    path('display-received', views.display_received_offers, name='received-offer-index'),

    # submit offer (by user)
    path('<int:property_id>/submit-offer/', views.submit_offer, name='submit-offer'),

    # accept offer (by seller)
    path('<int:offer_id>/update/', views.respond_to_offer, name='update-offer-state'),

    # finalize offer (by user)
    path('<int:offer_id>/payment/', views.payment, name='payment-index'),
]
