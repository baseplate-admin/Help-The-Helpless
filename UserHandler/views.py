from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from Backend.models import UrlLink as Urllinks
# Create your views here.

def register(request):
    urls = Urllinks.objects.get(extra="main")
    if request.method == "POST":
        firstName = request.POST.get("first_name")
        lastName = request.POST.get("last_name")
        userName = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            password = password2
        else:
            return HttpResponse("<h1>403 not Allowed</h1>")
        user = User.objects.create_user(userName, email, password)
        user.last_name = lastName
        user.first_name = firstName
        user.save()
    return render(request, "front/sign-up/index.html", {"urls": urls})

def login(request):
    urls = Urllinks.objects.get(extra="main")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")
        else:
            return HttpResponse("<h1>User not authenticated or wrong password. Please go to reset password</h1>")
    return render(request, 'front/log-in/index.html', {"urls": urls})

def reset_password(request):
    urls = Urllinks.objects.get(extra="main")

    if request.method == "POST":
        email = request.POST.get('email')
    return render(request, "front/reset-password/index.html", {"urls": urls})

#TODO?
# ADD RESET PASSWORD EMAIL(NEED TANIMS HELP)