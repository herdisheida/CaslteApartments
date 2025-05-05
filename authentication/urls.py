from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='authentication-index'),

    # http://localhost:8000/id
    path('<int:id>', views.get_authentication_by_id, name='authentication-by-id'),
]