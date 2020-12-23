from django.shortcuts import render
from django.shortcuts import redirect
from UrlHandler.models import UrlLink as Urllinks

# Create your views here.

def home_view(request):
    urls = Urllinks.objects.get(extra="main")
    return render(request, "front/home/index.html", {"urls": urls})

def redirect_to_home(requst):
    return redirect("/home/")