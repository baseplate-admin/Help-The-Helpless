from django.urls import path
from . import views

urlpatterns = [
    path("back/url-edit/", views.url_edit, name="url-edit"),
    path("back/url-edit-create/", views.url_edit_create, name="url-edit-create"),
    path(
        "back/title-and-slogan-edit/",
        views.slogan_and_title_edit,
        name="title-and-slogan-edit",
    ),
    path(
        "back/title-and-slogan-edit-create/",
        views.slogan_and_title_edit_create,
        name="title-and-slogan-edit-create",
    ),
    path("back/github-user-id/", views.github_user_id, name="github-user-id"),
    path(
        "back/github-user-id-handle/",
        views.github_user_id_handle,
        name="github-user-id-handle",
    ),
]
