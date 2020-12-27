from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.register, name="sign-up"),
    path("log-in/", views.login, name="log-in"),
    path("log-in-handle/", views.login_handle, name="log-in-handle"),
    path("reset-password/", views.reset_password, name="reset-password"),
    path("log-out/", views.logout, name="log-out"),
]
