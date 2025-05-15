from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path(
        "login",
        LoginView.as_view(
            template_name="authentication/login.html",
            redirect_authenticated_user=True,  # logged-in users cant go to log-in/register-page
        ),
        name="login",
    ),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("display-profile", views.display_profile, name="display-profile"),
    path('edit-profile', views.edit_profile, name="edit-profile"),
    path("seller-signup/", views.create_seller_profile, name="become-seller"),
]