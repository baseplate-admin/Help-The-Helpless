from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse

from Backend.models import Backend

# Create your views here.


@gzip_page
def home_view(request):
    if request.method == "GET":
        if (
            not Backend.objects.filter(extra="backend").exists()
        ):

            Backend.objects.create(extra='backend').save()

        elif (
            Backend.objects.filter(extra="backend").exists()
        ):
            backend = Backend.objects.get(extra="backend")


        return render(
            request,
            "front/home/index.html",
            {
                "backend": backend,
                "site_header": "Home",
            },
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


def redirect_to_home(request):
    return redirect("/home/")


@gzip_page
def donation(request):
    if request.method == "GET":
        if (
            not Backend.objects.filter(extra="backend").exists()
        ):
            Backend.objects.create(extra='backend').save()

        elif (
            Backend.objects.filter(extra="backend").exists()
        ):
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/donate/index.html",
            {
                "site_header": "Donate",
                "backend":backend,
            },
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog(request):
    if request.method == "GET":
        if (
            not Backend.objects.filter(extra="backend").exists()
        ):
            backend = 'backend'
        elif (
            Backend.objects.filter(extra="backend").exists()
        ):
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/blog/index.html",
            {
                "backend": backend,
                "site_header": "Blog",

            },
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog_create(request):
    backend = Backend.objects.get(extra="backend")
    return render(
        request, "front/blog-create/index.html", {"backend":backend}
    )
