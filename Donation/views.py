from django.shortcuts import render
from UrlHandler.models import UrlLink as Urllinks

# Create your views here.

def donation(request):
    urls = Urllinks.objects.get(extra="main")

    return render(request, 'front/donate/index.html', {"urls": urls})