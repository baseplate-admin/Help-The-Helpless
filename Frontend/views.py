from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse

from Backend.models import Backend
from Frontend.models import Blog
from Frontend.models import Comments


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
        # print(name)
        # print(email)
        # print(comment)
        database = Comments.objects.create(blog_id=pk)
        database.email = email
        database.comments = comment
        database.name = name
        database.save()
        return redirect(f"/blog/{pk}/")
    elif request.method == "GET":
        return redirect("/blog/")
