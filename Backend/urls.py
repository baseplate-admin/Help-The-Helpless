from django.urls import path
from . import views

urlpatterns = [
    path("back/url-edit/", views.url_edit, name="url-edit"),
]