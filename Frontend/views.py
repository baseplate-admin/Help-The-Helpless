from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink as Urllinks
from Backend.models import SiteDescription
from Backend.models import SiteTitle
from django.views.decorators.gzip import gzip_page


# Create your views here.


@gzip_page
def home_view(request):
    if (
        not SiteTitle.objects.filter(extra="title").exists()
        and not SiteDescription.objects.filter(extra="description").exists()
    ):
        title = "title"
        slogan = "slogan"
        urls = "Help the helpless"
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


def redirect_to_home(request):
    return redirect("/home/")


@gzip_page
def donation(request):
    if (
        not SiteTitle.objects.filter(extra="title").exists()
        and not SiteDescription.objects.filter(extra="description").exists()
    ):
        title = "title"
        slogan = "slogan"
        urls = "Help the helpless"
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


@gzip_page
def blog(request):
    if (
        not SiteTitle.objects.filter(extra="title").exists()
        and not SiteDescription.objects.filter(extra="description").exists()
    ):
        title = "title"
        slogan = "slogan"
        urls = "Help the helpless"
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


@gzip_page
def blog_create(request):
    pass
