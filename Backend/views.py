from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink
from django.contrib.auth.decorators import login_required

# Create your views here


@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "POST":
        database = UrlLink.objects.get(extra="main")

        facebook_url = request.POST.get("facebook_url")
        youtube_url = request.POST.get("youtube_url")
        email_url = request.POST.get("email_url")

        database.facebook_url = facebook_url
        database.youtube_url = youtube_url
        database.email_url = email_url
        database.save()

        return redirect("/back/url-edit/")

    elif request.method == "GET":
        return render(request, 'back/url-edit/index.html')

    else:
        return redirect("/home/")

