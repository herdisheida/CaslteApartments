from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='submitted-offer-index'),


    # accept offer (by seller)
    # path('<int:offer_id>/accept', views.accept_offer, name='accept-offer'),

    # finalize offer (by user)
    path('payment/', views.payment, name='payment-index'),
]
