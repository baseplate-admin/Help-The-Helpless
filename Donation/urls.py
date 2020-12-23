from django.urls import path
from . import views

urlpatterns = [
    path("donate/", views.donation, name="donate")
]