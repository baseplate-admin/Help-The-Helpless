from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from Backend.models import Backend
from Frontend.models import Blog

import os

# Create your views here.


class imgbb:
    def __init__(self):

        self.key = "a10313abcb97c127a0e4f42e6e14ec73"
        self.filelocation = self._file_read
        self.url = ""

    def _read(self):
        import base64
        import requests
        import json

        with open(self.filelocation, "rb") as f:
            url = "https://api.imgbb.com/1/upload"
            payload = {"key": self.key, "image": base64.b64encode(f.read())}
            res = requests.post(url, payload)
            # pprint(vars(res))
            res = res.json()
            self.url = res["data"]["url"]
            return self.url

    def _file_read(self, filelocation):
        self.filelocation = filelocation
        self._read()
        return self.url


def value_time():
    from datetime import datetime

    time = datetime.now()

    return time


# imgbb()._file_read(f"{os.getcwd()}\\a.png")


@gzip_page
def home_view(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():

            Backend.objects.create(extra="backend").save()

        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/home/index.html",
            {"backend": backend, "site_header": "Home"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


def redirect_to_home(request):
    return redirect("/home/")


def index(request):
    return render(request, "front/index/index.html")


@gzip_page
def donation(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            Backend.objects.create(extra="backend").save()

        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/donate/index.html",
            {"site_header": "Donate", "backend": backend},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog(request):
    if request.method == "GET":
        if not Backend.objects.filter(extra="backend").exists():
            backend = "backend"
        elif Backend.objects.filter(extra="backend").exists():
            backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/blog/index.html",
            {"backend": backend, "site_header": "Blog"},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog_create(request):
    if request.method == "GET":
        backend = Backend.objects.get(extra="backend")

        return render(request, "front/blog-create/index.html", {"backend": backend,})
    else:
        return redirect("/home/")


@gzip_page
def blog_create_handler(request):
    if request.method == "POST":
        header = request.POST.get("header")
        image_1 = request.FILES["myFile1"]  #   1
        image_2 = request.FILES["myFile2"]  #   2
        image_3 = request.FILES["myFile3"]  #   3
        image_4 = request.FILES["myFile4"]  #   4
        text = request.POST.get("text")  #   1
        text_1 = request.POST.get("image_text1")  #   2
        text_2 = request.POST.get("image_text2")  #   3
        text_3 = request.POST.get("image_text3")  #   4
        text_4 = request.POST.get("image_text4")
        image_title_1 = request.POST.get("title1")  #   1
        image_title_2 = request.POST.get("title2")  #   2
        image_title_3 = request.POST.get("title3")  #   3
        image_title_4 = request.POST.get("title4")  #   4

        # Extra logic

        username = request.user.username
        time = value_time()

        # Database Logic
        database = Blog.objects.create()
        database.username = username
        database.date_time = time
        database.header = header

        database.image_1 = image_1
        database.image_2 = image_2
        database.image_3 = image_3
        database.image_4 = image_4

        database.content_1 = text
        database.content_2 = text_1
        database.content_3 = text_2
        database.content_4 = text_3
        database.content_5 = text_4

        database.image_1_title = image_title_1
        database.image_2_title = image_title_2
        database.image_3_title = image_title_3
        database.image_4_title = image_title_4

        database.save()

        database_pk = database.pk
        imgbb_database = Blog.objects.get(pk=database_pk)

        image_1_imgbb = f"{os.getcwd()}\\media\\{database.image_1}"
        image_2_imgbb = f"{os.getcwd()}\\media\\{database.image_2}"
        image_3_imgbb = f"{os.getcwd()}\\media\\{database.image_3}"
        image_4_imgbb = f"{os.getcwd()}\\media\\{database.image_4}"

        image_url_1 = imgbb()._file_read(image_1_imgbb)
        image_url_2 = imgbb()._file_read(image_2_imgbb)
        image_url_3 = imgbb()._file_read(image_3_imgbb)
        image_url_4 = imgbb()._file_read(image_4_imgbb)

        imgbb_database.image_1_url = image_url_1
        imgbb_database.image_2_url = image_url_2
        imgbb_database.image_3_url = image_url_3
        imgbb_database.image_4_url = image_url_4

        imgbb_database.save()
        os.remove(image_1_imgbb)
        os.remove(image_2_imgbb)
        os.remove(image_3_imgbb)
        os.remove(image_4_imgbb)
        # image_path = f"{os.getcwd()}\\media\\"
        return redirect("/blog-create/")

    elif request.method == "GET":
        return redirect("/blog-create/")
