from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('', views.redirect_to_home, name="redirect"),
]