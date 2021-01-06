from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

# Create your views here

from Frontend.models import Blog
from Backend.models import Backend
import os
import concurrent.futures


def value_time():
    from datetime import datetime

    time = datetime.now()
    return time


def imgbb(file_location):
    import base64
    import requests

    key = "c2951e107a0b79b13331db8b483c0ead"
    with open(file_location, "rb") as f:
        url = "https://api.imgbb.com/1/upload"
        payload = {"key": key, "image": base64.b64encode(f.read())}
        res = requests.post(url, payload)
        res = res.json()
        url = res["data"]["url"]
        return url


def remove_file_os(filename):
    os.remove(filename)


def request_post_get_async(request_data, request_name):
    fetched_data = request_data.POST.get(request_name)
    return fetched_data


def request_files_async(request_data, request_name):
    fetched_data = request_data.FILES[request_name]
    return fetched_data


def return_full_path(name):
    return_path = f"{os.getcwd}\\media\\{name}"
    return return_path


def blog_save_to_database(
    username,
    time,
    header,
    image_1,
    image_2,
    image_3,
    image_4,
    text,
    text_1,
    text_2,
    text_3,
    text_4,
    image_title_1,
    image_title_2,
    image_title_3,
    image_title_4,
):
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

    return database


@gzip_page
@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "GET":
        try:
            backend = Backend.objects.get(extra="backend")
        except Exception as e:
            print(e)
            Backend.objects.create().save()
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
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            header_future = executor.submit(request_post_get_async, request, "header")
            header = header_future.result()

            image_1_future = executor.submit(request_files_async, request, "myFile1")
            image_1 = image_1_future.result()

            image_2_future = executor.submit(request_files_async, request, "myFile2")
            image_2 = image_2_future.result()

            image_3_future = executor.submit(request_files_async, request, "myFile3")
            image_3 = image_3_future.result()

            image_4_future = executor.submit(request_files_async, request, "myFile4")
            image_4 = image_4_future.result()

            text_future = executor.submit(request_post_get_async, request, "text")
            text = text_future.result()

            text_1_future = executor.submit(
                request_post_get_async, request, "image_text1"
            )
            text_1 = text_1_future.result()

            text_2_future = executor.submit(
                request_post_get_async, request, "image_text2"
            )
            text_2 = text_2_future.result()

            text_3_future = executor.submit(
                request_post_get_async, request, "image_text3"
            )
            text_3 = text_3_future.result()

            text_4_future = executor.submit(
                request_post_get_async, request, "image_text4"
            )
            text_4 = text_4_future.result()

            image_title_1_future = executor.submit(
                request_post_get_async, request, "title1"
            )
            image_title_1 = image_title_1_future.result()

            image_title_2_future = executor.submit(
                request_post_get_async, request, "title2"
            )
            image_title_2 = image_title_2_future.result()

            image_title_3_future = executor.submit(
                request_post_get_async, request, "title3"
            )
            image_title_3 = image_title_3_future.result()

            image_title_4_future = executor.submit(
                request_post_get_async, request, "title4"
            )
            image_title_4 = image_title_4_future.result()

            time_future = executor.submit(value_time,)
            time = time_future.result()

        # Extra logic

        username = request.user.username

        # Database Logic
        with concurrent.futures.ThreadPoolExecutor() as executor:
            database_futures = executor.submit(
                blog_save_to_database,
                username,
                time,
                header,
                image_1,
                image_2,
                image_3,
                image_4,
                text,
                text_1,
                text_2,
                text_3,
                text_4,
                image_title_1,
                image_title_2,
                image_title_3,
                image_title_4,
            )
            database = database_futures.result()

        database_pk = database.pk
        imgbb_database = Blog.objects.get(pk=database_pk)

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            image_1_imgbb_future = executor.submit(return_full_path, database.image_1)
            image_1_imgbb = image_1_imgbb_future.result()

            image_2_imgbb_future = executor.submit(return_full_path, database.image_2)
            image_2_imgbb = image_2_imgbb_future.result()

            image_3_imgbb_future = executor.submit(return_full_path, database.image_3)
            image_3_imgbb = image_3_imgbb_future.result()

            image_4_imgbb_future = executor.submit(return_full_path, database.image_4)
            image_4_imgbb = image_4_imgbb_future.result()

        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                image_1_future = executor.submit(imgbb, image_1_imgbb)
                image_1_init = image_1_future.result()

                image_2_future = executor.submit(imgbb, image_2_imgbb)
                image_2_init = image_2_future.result()

                image_3_future = executor.submit(imgbb, image_2_imgbb)
                image_3_init = image_3_future.result()

                image_4_future = executor.submit(imgbb, image_2_imgbb)
                image_4_init = image_4_future.result()
            image_url_4 = image_4_init
            image_url_3 = image_3_init
            image_url_2 = image_2_init
            image_url_1 = image_1_init

            imgbb_database.image_1_url = image_url_1
            imgbb_database.image_2_url = image_url_2
            imgbb_database.image_3_url = image_url_3
            imgbb_database.image_4_url = image_url_4
        except Exception as e:
            print(e)
            print("Something is wrong with images Upload")
        finally:
            try:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(remove_file_os, image_1_imgbb)
                    executor.submit(remove_file_os, image_2_imgbb)
                    executor.submit(remove_file_os, image_3_imgbb)
                    executor.submit(remove_file_os, image_4_imgbb)
            except Exception as e:
                print(e)
                pass
        imgbb_database.save()

        return redirect("/blog-create/")

    elif request.method == "GET":
        return redirect("/blog-create/")
