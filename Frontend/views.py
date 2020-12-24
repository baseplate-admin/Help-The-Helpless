from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink as Urllinks

# Create your views here.

def home_view(request):
    if Urllinks.objects.filter(extra="main").exists():
        urls = Urllinks.objects.get(extra="main")
        return render(request, "front/home/index.html", {"urls": urls})
    else:
        return redirect("/back/url-edit/")


def redirect_to_home(requst):
    if Urllinks.objects.filter(extra="main").exists():
        return redirect("/home/")
    else:
        return redirect("/back/url-edit/")

def donation(request):
    if Urllinks.objects.filter(extra="main").exists() is False:
        urls = Urllinks.objects.get(extra="main")
        return render(request, 'front/donate/index.html', {"urls": urls})
    else:
        return redirect("/back/url-edit/")