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
    def __init__(self, filelocation):
        self.filelocation = filelocation
        self.key = ""
        self.url = ""
        # self.delete_url = ""
        self._read()

    def _read(self):
        import base64
        import requests

        if self.key == "":
            raise KeyError("Enter IMGBB api key")
        else:
            with open(self.filelocation, "rb") as f:
                url = "https://api.imgbb.com/1/upload"
                payload = {"key": self.key, "image": base64.b64encode(f.read())}
                res = requests.post(url, payload)
                # pprint(vars(res))
                res = res.json()
                self.url = res["data"]["url"]
                # self.delete_url = res["data"]["delete_url"]
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
def blog_details(request, pk):
    blog_database = Blog.objects.get(pk=pk)
    backend = Backend.objects.get(extra="backend")
    return render(
        request,
        "front/blog-details/index.html",
        {
            "blog": blog_database,
            "backend": backend,
            "site_header": f"{blog_database.header}",
        },
    )


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

        image_1_init = imgbb(image_1_imgbb)

        # image_1_delete = image_1_init.delete_url

        image_2_init = imgbb(image_2_imgbb)

        # image_2_delete = image_2_init.delete_url

        image_3_init = imgbb(image_3_imgbb)

        # image_3_delete = image_3_init.delete_url

        image_4_init = imgbb(image_3_imgbb)

        # image_4_delete = image_4_init.delete_url
        try:
            image_url_4 = image_4_init.url
            image_url_3 = image_3_init.url
            image_url_2 = image_2_init.url
            image_url_1 = image_1_init.url
            imgbb_database.image_1_url = image_url_1
            imgbb_database.image_2_url = image_url_2
            imgbb_database.image_3_url = image_url_3
            imgbb_database.image_4_url = image_url_4
        except Exception as e:
            print("Something is wrong with images Upload")
        finally:
            os.remove(image_1_imgbb)
            os.remove(image_2_imgbb)
            os.remove(image_3_imgbb)
            os.remove(image_4_imgbb)

        # imgbb_database.image_1_delete = image_1_delete
        # imgbb_database.image_2_delete = image_2_delete
        # imgbb_database.image_3_delete = image_3_delete
        # imgbb_database.image_4_delete = image_4_delete

        imgbb_database.save()

        # image_path = f"{os.getcwd()}\\media\\"
        return redirect("/blog-create/")

    elif request.method == "GET":
        return redirect("/blog-create/")
