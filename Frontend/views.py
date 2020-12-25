from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink as Urllinks
from Backend.models import SiteDescription
from Backend.models import SiteTitle


# Create your views here.


def home_view(request):
    if (
        SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
        and Urllinks.objects.filter(extra="main").exists()
    ):
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/home/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Home"},
        )

    elif not Urllinks.objects.filter(extra="main").exists():
        return redirect("/back/url-edit/")

    elif (
        not SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
    ):
        return redirect("/back/title-and-slogan-edit/")


def redirect_to_home(request):
    if (
        SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
        and Urllinks.objects.filter(extra="main").exists()
    ):
        return redirect("/home/")

    elif not Urllinks.objects.filter(extra="main").exists():
        return redirect("/back/url-edit/")

    elif (
        not SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
    ):
        return redirect("/back/title-and-slogan-edit/")


def donation(request):
    if (
        SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
        and Urllinks.objects.filter(extra="main").exists()
    ):
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/donate/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Donate"},
        )

    elif not Urllinks.objects.filter(extra="main").exists():
        return redirect("/back/url-edit/")

    elif (
        not SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
    ):
        return redirect("/back/title-and-slogan-edit/")


def blog(request):
    if (
        SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
        and Urllinks.objects.filter(extra="main").exists()
    ):
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        urls = Urllinks.objects.get(extra="main")
        return render(
            request,
            "front/blog/index.html",
            {"urls": urls, "title": title, "slogan": slogan, "site_header": "Blog"},
        )
    elif not Urllinks.objects.filter(extra="main").exists():

        return redirect("/back/url-edit/")

    elif (
        not SiteTitle.objects.filter(extra="title").exists()
        and SiteDescription.objects.filter(extra="description").exists()
    ):
        return redirect("/back/title-and-slogan-edit/")
