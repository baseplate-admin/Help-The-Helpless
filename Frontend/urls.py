from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"api/v1", views.BlogReadOnly, basename="json")
urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("", views.redirect_to_home, name="redirect"),
    path("donate/", views.donation, name="donate"),
    path("blog/", views.blog, name="blog"),
    path("blog/<int:pk>/", views.blog_details, name="blog-details"),
    path("comment-handler/<int:pk>/", views.comment_handler, name="comment-handler"),
]
urlpatterns += router.urls
