from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from Backend.models import UrlLink
from Backend.models import SiteDescription
from Backend.models import SiteTitle

from htmlmin.decorators import minified_response


# Create your views here

@minified_response
@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "GET":
        if not UrlLink.objects.filter(extra="main").exists():
            UrlLink.objects.create(extra="main").save()
        database_pk = UrlLink.objects.get(extra="main").pk
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        return render(
            request,
            "back/url-edit/index.html",
            {
                "site_header": "Url Edit",
                "title": title,
                "slogan": slogan,
                "pk": database_pk,
            },
        )

    else:
        return redirect("/home/")


@minified_response
@login_required(login_url="log-in")
def url_edit_create(request, pk):
    if request.method == "POST":
        database = UrlLink.objects.get(pk=pk)

        facebook_url = request.POST.get("facebook_url")
        youtube_url = request.POST.get("youtube_url")
        email_url = request.POST.get("email_url")

        database.facebook_url = facebook_url
        database.youtube_url = youtube_url
        database.email_url = email_url
        database.save()

        return redirect("/home/")
    elif request.method == "GET":
        return redirect("/home/")

@minified_response
@login_required(login_url="log-in")
def slogan_and_title_edit(request):
    if (
        not SiteTitle.objects.filter(extra="title").exists()
        and not SiteDescription.objects.filter(extra="description").exists()
    ):
        SiteTitle.objects.create(extra="title").save()
        SiteDescription.objects.create(extra="description").save()
    SiteTitle_pk = SiteTitle.objects.get(extra="title").pk
    SiteDescription_pk = SiteDescription.objects.get(extra="description").pk

    title = SiteTitle.objects.get(extra="title")
    slogan = SiteDescription.objects.get(extra="description")

    return render(
        request,
        "back/title-and-slogan-edit/index.html",
        {
            "site_header": "Title and Slogan Edit",
            "title": title,
            "slogan": slogan,
            "TitlePK": SiteTitle_pk,
            "DescriptionPK": SiteDescription_pk,
        },
    )

@minified_response
@login_required(login_url="log-in")
def slogan_and_title_edit_create(request, title_pk, description_pk):
    title_database = SiteTitle.objects.get(pk=title_pk)
    description_database = SiteDescription.objects.get(pk=description_pk)

    if request.method == "POST":
        title = request.POST.get("title")
        slogan = request.POST.get("slogan")
        # SiteDescription == slogan
        # SiteTitle == title

        title_database.site_title = title
        description_database.site_description = slogan

        description_database.save()
        title_database.save()
        return redirect("/back/title-and-slogan-edit/")
    elif request.method == "GET":
        return redirect("/back/title-and-slogan-edit/")
