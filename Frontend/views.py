from __future__ import unicode_literals
from django.http.response import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse
from rest_framework import serializers

from Backend.models import Backend
from Frontend.models import Blog
from Frontend.models import Comments


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            "username",
            "date_time",
            "header",
            "content_1",
            "content_2",
            "content_3",
            "content_4",
            "content_5",
            "image_1_title",
            "image_2_title",
            "image_3_title",
            "image_4_title",
            "image_1_url",
            "image_2_url",
            "image_3_url",
            "image_4_url",
        )


from rest_framework.response import Response
from rest_framework.decorators import api_view


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


# class BlogReadOnly(viewsets.ReadOnlyModelViewSet):
#     """
#     Lists information related to the current user.
#     """

#     serializer_class = BlogSerializer

#     def get_queryset(self):
#         next = self.request.GET["next"]
#         next = int(next)
#         return Blog.objects.all().order_by("-id")[:next]


@api_view(["GET"])
def blog_queryset(request):
    next = request.GET["next"]
    next = int(next)
    data = Blog.objects.all().order_by("-id")[:next]
    serializers = BlogSerializer(data, many=True)
    return Response(serializers.data)


# Create your views here.


@gzip_page
def home_view(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():

            Backend.objects.create(extra="backend").save()

        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/home/index.html",
            {"backend": backend, "site_header": "Home"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


def redirect_to_home(request):
    return redirect("/home/")


def index(request):
    return render(request, "front/index/index.html")


@gzip_page
def donation(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            Backend.objects.create(extra="backend").save()

        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/donate/index.html",
            {"site_header": "Donate", "backend": backend},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            backend = "backend"
        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/blog/index.html",
            {"backend": backend, "site_header": "Blog"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog_details(request, pk):
    blog_database = Blog.objects.get(pk=pk)
    comments = Comments.objects.filter(blog_id=pk)
    backend = Backend.objects.get(extra="backend")
    return render(
        request,
        "front/blog-details/index.html",
        {
            "blog": blog_database,
            "backend": backend,
            "comments": comments,
            "site_header": f"{blog_database.header}",
            "site_pk": f"{blog_database.pk}",
        },
    )


def comment_handler(request, pk):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        database = Comments.objects.create(blog_id=pk)
        database.email = email
        database.comments = comment
        database.name = name
        database.save()
        return redirect(f"/blog/{pk}/")
    elif request.method == "GET":
        return redirect("/blog/")

