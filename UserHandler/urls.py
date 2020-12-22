from django.urls import path
from . import views
urlpatterns = [
    path('sign-up/', views.register, name="userRegister"),
    path('log-in/', views.login, name="log-in"),
]