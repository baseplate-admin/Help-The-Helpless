from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

from Backend.models import SiteDescription
from Backend.models import SiteTitle


# Create your views here.


@gzip_page
def register(request):
    if request.method == "GET":
        if (
                not SiteTitle.objects.filter(extra="title").exists()
                and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
                SiteTitle.objects.filter(extra="title").exists()
                and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")
        return render(
            request,
            "front/sign-up/index.html",
            {"title": title, "slogan": slogan, "site_header": "Sign up"},
        )
    else:
        return redirect("/home/")


@gzip_page
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/home/")
        if (
                not SiteTitle.objects.filter(extra="title").exists()
                and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
                SiteTitle.objects.filter(extra="title").exists()
                and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")
        else:
            return HttpResponse("<h1>403 not Allowed</h1>")
        return render(
            request,
            "front/log-in/index.html",
            {"title": title, "slogan": slogan, "site_header": "Log In"},
        )
    else:
        return redirect("/home/")


@gzip_page
def login_handle(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            next_url = request.POST["next"]
            if bool(next_url):
                return redirect(next_url)
            elif not bool(next_url):
                return redirect("/home/")
            else:
                return HttpResponse(
                    "<h1>Something wrong with userhandler/views.py(login_handle). Please contact Zarif Ahnaf(zarifahnaf@outlook.com)."
                )
        elif user is None:
            return HttpResponse("<h1>Please Create an Account</h1>")
        else:
            return HttpResponse(
                "<h1>User not authenticated or wrong password. Please go to reset password</h1>"
            )
    else:
        return redirect("/log-in/")


@gzip_page
def reset_password(request):
    # UrlObject = Url.objects.get(extra="main")

    if request.method == "POST":
        email = request.POST.get("email")

    elif request.method == "GET":
        if (
                not SiteTitle.objects.filter(extra="title").exists()
                and not SiteDescription.objects.filter(extra="description").exists()
        ):
            title = "title"
            slogan = "slogan"
        elif (
                SiteTitle.objects.filter(extra="title").exists()
                and SiteDescription.objects.filter(extra="description").exists()
        ):
            title = SiteTitle.objects.get(extra="title")
            slogan = SiteDescription.objects.get(extra="description")

        return render(
            request,
            "front/reset-password/index.html",
            {"title": title, "slogan": slogan, "site_header": "Reset Password"},
        )


@gzip_page
def logout(request):
    if request.method == "GET":
        auth_logout(request)
        return redirect("/home/")
    else:
        return HttpResponse("<h1>403 Not Allowed</h1>")


@gzip_page
def register_handler(request):
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
        return redirect("/log-in/")
    else:
        return redirect("/sign-up/")

# TODO?
# ADD RESET PASSWORD EMAIL(NEED TANIMS HELP)
