from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from Backend.models import SiteDescription
from Backend.models import SiteTitle

# Create your views here.


def register(request):
    if request.method == "POST":
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            password = password2
        else:
            return HttpResponse("<h1>403 not Allowed</h1>")
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
    elif request.method == "GET":
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        return render(
            request,
            "front/sign-up/index.html",
            {"title": title, "slogan": slogan, "site_header": "Sign up"},
        )


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_Url = request.GET.get("next")
            if next_Url is not None:
                return redirect(next_Url)
            else:
                return redirect("/")
        elif user is None:
            return HttpResponse("<h1>Please Create an Account</h1>")
        else:
            return HttpResponse(
                "<h1>User not authenticated or wrong password. Please go to reset password</h1>"
            )
    elif request.method == "GET":
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        return render(
            request,
            "front/log-in/index.html",
            {"title": title, "slogan": slogan, "site_header": "Log In"},
        )


def reset_password(request):
    # UrlObject = Url.objects.get(extra="main")

    if request.method == "POST":
        email = request.POST.get("email")

    elif request.method == "GET":
        title = SiteTitle.objects.get(extra="title")
        slogan = SiteDescription.objects.get(extra="description")
        return render(
            request,
            "front/reset-password/index.html",
            {"title": title, "slogan": slogan, "site_header": "Reset Password"},
        )


def logout(request):
    if request.method == "GET":
        auth_logout(request)
        return redirect("/home/")
    else:
        return HttpResponse("<h1>403 Not Allowed</h1>")


# TODO?
# ADD RESET PASSWORD EMAIL(NEED TANIMS HELP)
