from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("", views.redirect_to_home, name="redirect"),
    path("api/v1/blog", views.blog_queryset, name="blog-api"),
    path("donate/", views.donation, name="donate"),
    path("blog/", views.blog, name="blog"),
    path("blog/<int:pk>/", views.blog_details, name="blog-details"),
    path("comment-handler/<int:pk>/", views.comment_handler, name="comment-handler"),
]
