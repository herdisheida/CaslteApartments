from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000 (root)
    path('', views.index, name='profile-index'),

    # http://localhost:8000/id
    path('<int:id>', views.get_property_by_id, name='profile-by-id'),
]
