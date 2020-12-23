from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def home_view(request):
    return render(request, "front/home/index.html")

def redirect_to_home(requst):
    return redirect("/home/")