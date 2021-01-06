from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

# Create your views here

from Frontend.models import Blog
from Backend.models import Backend
import os


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


@login_required(login_url="log-in")
@gzip_page
def blog_create(request):
    if request.method == "GET":
        backend = Backend.objects.get(extra="backend")

        return render(
            request,
            "front/blog-create/index.html",
            {"backend": backend, "site_header": "Blog Create"},
        )
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

        try:
            image_1_init = imgbb(image_1_imgbb)
            image_2_init = imgbb(image_2_imgbb)
            image_3_init = imgbb(image_3_imgbb)
            image_4_init = imgbb(image_3_imgbb)

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
