from django.urls import path
from . import views

urlpatterns = [
    path("back/url-edit/", views.url_edit, name="url-edit"),
    path(
        "back/url-edit-create/<int:pk>/", views.url_edit_create, name="url-edit-create"
    ),
    path(
        "back/title-and-slogan-edit/",
        views.slogan_and_title_edit,
        name="title-and-slogan-edit",
    ),
    path(
        "back/title-and-slogan-edit-create/<int:title_pk>/<int:description_pk>/",
        views.slogan_and_title_edit_create,
        name="title-and-slogan-edit-create",
    ),
]
