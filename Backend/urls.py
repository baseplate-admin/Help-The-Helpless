from django.urls import path
from . import views

urlpatterns = [
    path("back/url-edit/", views.url_edit, name="url-edit"),
    path(
        "back/url-edit-create/<int:pk>/", views.url_edit_create, name="url-edit-create"
    ),
]
