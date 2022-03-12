from unicodedata import name
from django.urls import path
from . import views


app_name = "App"

urlpatterns = [
    path("", views.loginpage, name="loginpage"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("singup/", views.signup, name="signup"),
    path("logout/", views.logoutuser, name="logoutuser")
]
