from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='offer-index'),

    # http://localhost:8000/id
    path('<int:id>', views.get_offer_by_id, name='offer-by-id'),
]
