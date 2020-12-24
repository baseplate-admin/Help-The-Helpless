from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink
from django.contrib.auth.decorators import login_required
from Backend.models import SiteName

# Create your views here


@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "GET":
        if not UrlLink.objects.filter(extra="main").exists():
            UrlLink.objects.create(extra="main").save()
            database_pk = UrlLink.objects.get(extra="main").pk
        elif UrlLink.objects.filter(extra="main").exists():
            database_pk = UrlLink.objects.get(extra="main").pk

        return render(request, "back/url-edit/index.html", {"pk": database_pk})

    else:
        return redirect("/home/")


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
    else:
        return redirect("/home/")


# @login_required(login_url="log-in")
# def create_site_name(request):
#     if site