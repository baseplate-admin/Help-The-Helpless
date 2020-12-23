from django.shortcuts import render
from django.shortcuts import redirect
from Backend.models import UrlLink as Urllinks
from django.contrib.auth.decorators import login_required
# Create your views here


@login_required(login_url="log-in")
def url_edit(request):
    return render(request, 'back/url-edit/index.html')