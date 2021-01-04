from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("", views.redirect_to_home, name="redirect"),
    path("donate/", views.donation, name="donate"),
    path("blog/", views.blog, name="blog"),
    path("blog-create/", views.blog_create, name="blog-create"),
    path("blog-create-handler/", views.blog_create_handler, name="blog-create-handler"),
]
