from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.auth_page, name="login"),
    path("login/", views.login_view, name="do_login"),
    path("register/", views.register_view, name="do_register"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("profile/", views.profile_view, name="profile"),
]
