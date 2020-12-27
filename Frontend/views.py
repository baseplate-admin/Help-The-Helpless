from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink as Urllinks
from Backend.models import SiteDescription
from Backend.models import SiteTitle
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse


# Create your views here.


@gzip_page
def home_view(request):
    if request.method == "GET":
        if (
            not SiteTitle.objects.filter(extra="title").exists()
            and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
            SiteTitle.objects.filter(extra="title").exists()
            and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")

        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/home/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Home"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


def redirect_to_home(request):
    return redirect("/home/")


@gzip_page
def donation(request):
    if request.method == "GET":
        if (
            not SiteTitle.objects.filter(extra="title").exists()
            and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
            SiteTitle.objects.filter(extra="title").exists()
            and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")
        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/donate/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Donate"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog(request):
    if request.method == "GET":
        if (
            not SiteTitle.objects.filter(extra="title").exists()
            and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
            SiteTitle.objects.filter(extra="title").exists()
            and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")
        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/blog/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Blog"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog_create(request):
    pass
