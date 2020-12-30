from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here
from django.views.decorators.gzip import gzip_page

from Backend.models import Backend


class ImageToBase64:
    def __init__(self):
        self.image = None
        self.base64 = None

    def _read_image(self, image):
        file = open(f"{image}", "rb")
        self.image = file.read()
        return self.image

    def _image_to_base64(self):
        import base64

        self.base64 = base64.b64encode(self.image)
        return self.base64

    def image_input(self, input_image):
        self._read_image(input_image)
        self._image_to_base64()


class GenerateKey:
    def __init__(self):
        self.key = self.gen_key()

    def gen_key(self):
        self.key = Fernet.generate_key()
        return self.key

    def does_key_exist(self):
        database = Backend.objects.filter(extra="backend")
        if database.key_hash is not None:
            return database.key_hash
        else:
            database.key_hash = self.key


@gzip_page
@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            Backend.objects.create().save()
        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        else:
            return HttpResponse(
                "<h1>Something is wrong with backend/views.py. Please contact Zarif_Ahnaf(zarifahnaf@outlook.com).</h1>"
            )
        return render(
            request,
            "back/url-edit/index.html",
            {"site_header": "Url Edit", "backend": backend,},
        )

    else:
        return redirect("/home/")


@gzip_page
@login_required(login_url="log-in")
def url_edit_create(request):
    if request.method == "POST":

        database = Backend.objects.get(extra="backend")
        facebook_url = request.POST.get("facebook_url")
        youtube_url = request.POST.get("youtube_url")
        email_url = request.POST.get("email_url")

        database.facebook_url = facebook_url
        database.youtube_url = youtube_url
        database.email_url = email_url
        database.save()

        return redirect("/home/")
    elif request.method == "GET":
        return redirect("/home/")


@gzip_page
@login_required(login_url="log-in")
def slogan_and_title_edit(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            Backend.objects.create(extra="backend").save()
        backend = Backend.objects.get(extra="backend")
        return render(
            request,
            "back/title-and-slogan-edit/index.html",
            {"site_header": "Title and Slogan Edit", "backend": backend,},
        )
    else:
        return HttpResponse("<h1>403 post not Allowed</h1>")


@gzip_page
@login_required(login_url="log-in")
def slogan_and_title_edit_create(request):
    backend = Backend.objects.get(extra="backend")

    if request.method == "POST":
        title = request.POST.get("title")
        slogan = request.POST.get("slogan")
        # SiteDescription == slogan
        # SiteTitle == title

        backend.site_title = title
        backend.site_description = slogan

        backend.save()
        return redirect("/back/title-and-slogan-edit/")
    elif request.method == "GET":
        return redirect("/back/title-and-slogan-edit/")


@gzip_page
@login_required(login_url="log-in")
def github_user_id(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            Backend.objects.create(extra="backend").save()
        backend = Backend.objects.get(extra="backend")
        return render(
            request,
            "back/github-user-id/index.html",
            {"site_header": "Github User ID", "backend": backend,},
        )
    else:
        return HttpResponse("<h1>Post not allowed</h1>")


@login_required(login_url="log-in")
def github_user_id_handle(request):
    if request.method == "POST":
        username = request.POST.get("github_username")
        tag = request.POST.get("github_tag")
        repo = request.POST.get("github_repo")
        backend = Backend.objects.get(extra="backend")
        backend.github_username = username
        backend.github_tag = tag
        backend.github_repo = repo
        backend.save()
        return redirect("/back/github-user-id")
    else:
        return redirect("/back/github-user-id")
