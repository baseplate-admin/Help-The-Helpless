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

    key = "2a08e37bb3b1552dc96462768e7bcee1"
    with open(file_location, "rb") as f:
        url = "https://api.imgbb.com/1/upload"
        payload = {"key": key, "image": base64.b64encode(f.read())}
        res = requests.post(url, payload)
        res = res.json()
        url = res["data"]["url"]
        print(url)
        return url


def remove_file_os(filename):
    os.remove(filename)


def request_files_async(request_data, request_name):
    fetched_data = request_data.FILES[request_name]
    return fetched_data


def request_post_get_async(request_data, request_name):
    fetched_data = request_data.POST.get(request_name)
    return fetched_data


def return_full_path(name):
    return_path = f"{os.getcwd()}\\media\\{name}"
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


def image_url_save_to_database(
    primary_key, image_1_url, image_2_url, image_3_url, image_4_url
):
    imgbb_database = Blog.objects.get(pk=primary_key)
    imgbb_database.image_1_url = image_1_url
    imgbb_database.image_2_url = image_2_url
    imgbb_database.image_3_url = image_3_url
    imgbb_database.image_4_url = image_4_url
    imgbb_database.save()


@gzip_page
@login_required(login_url="log-in")
def url_edit(request):
    if request.method == "GET":
        backend = None
        try:
            backend = Backend.objects.get(extra="backend")
        except Exception as e:
            print(e)
            Backend.objects.create(extra="backend").save()
        return render(
            request,
            "back/url-edit/index.html",
            {"site_header": "Url Edit", "backend": backend},
        )

    else:
        return redirect("/home/")


@gzip_page
@login_required(login_url="log-in")
def url_edit_create(request):
    if request.method == "POST":
        database = Backend.objects.get(extra="backend")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            facebook_url_future = executor.submit(
                request_post_get_async, request, "facebook_url"
            )
            facebook_url = facebook_url_future.result()

            youtube_url_future = executor.submit(
                request_post_get_async, request, "youtube_url"
            )
            youtube_url = youtube_url_future.result()

            email_url_future = executor.submit(
                request_post_get_async, request, "email_url"
            )
            email_url = email_url_future.result()

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
            {"site_header": "Title and Slogan Edit", "backend": backend},
        )
    else:
        return HttpResponse("<h1>403 post not Allowed</h1>")


@gzip_page
@login_required(login_url="log-in")
def slogan_and_title_edit_create(request):
    backend = Backend.objects.get(extra="backend")

    if request.method == "POST":
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            title_future = executor.submit(request_post_get_async, request, "title")
            title = title_future.result()

            slogan_future = executor.submit(request_post_get_async, request, "slogan")
            slogan = slogan_future.result()
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
            {"site_header": "Github User ID", "backend": backend},
        )
    else:
        return HttpResponse("<h1>Post not allowed</h1>")


@login_required(login_url="log-in")
def github_user_id_handle(request):
    if request.method == "POST":
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            username_future = executor.submit(
                request_post_get_async, request, "github_username"
            )
            username = username_future.result()

            tag_future = executor.submit(request_post_get_async, request, "github_tag")
            tag = tag_future.result()

            repo_future = executor.submit(
                request_post_get_async, request, "github_repo"
            )
            repo = repo_future.result()

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
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
                header_future = executor.submit(request_post_get_async, request, "head")
                header = header_future.result()

                counter_future = executor.submit(
                    request_post_get_async, request, "counter"
                )
                counter = counter_future.result()

                time_future = executor.submit(value_time,)
                time = time_future.result()

                username = request.user.username

                text_future = executor.submit(request_post_get_async, request, "post")
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

        except Exception as e:
            print(e)
            raise e
            # Extra logic
            # Database Logic
        image_title_dict = {}
        image_dict = {}
        for i in range(1, (int(counter) + 1)):
            image_dict[f"image_{i}"] = request.FILES[f"myFile{i}"]
            image_title_dict[f"image_title_{i}"] = request.POST.get(f"title{i}")
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                database_futures = executor.submit(
                    blog_save_to_database,
                    username,
                    time,
                    header,
                    image_dict.get("image_1", None),
                    image_dict.get("image_2", None),
                    image_dict.get("image_3", None),
                    image_dict.get("image_4", None),
                    text,
                    text_1,
                    text_2,
                    text_3,
                    text_4,
                    image_title_dict.get("image_title_1", None),
                    image_title_dict.get("image_title_2", None),
                    image_title_dict.get("image_title_3", None),
                    image_title_dict.get("image_title_4", None),
                )
                database = database_futures.result()
                database_pk = database.pk
        except Exception as e:
            print(e)
            raise e
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                image_1_imgbb_future = executor.submit(
                    return_full_path, database.image_1
                )
                image_1_imgbb = image_1_imgbb_future.result()

                image_2_imgbb_future = executor.submit(
                    return_full_path, database.image_2
                )
                image_2_imgbb = image_2_imgbb_future.result()

                image_3_imgbb_future = executor.submit(
                    return_full_path, database.image_3
                )
                image_3_imgbb = image_3_imgbb_future.result()

                image_4_imgbb_future = executor.submit(
                    return_full_path, database.image_4
                )
                image_4_imgbb = image_4_imgbb_future.result()
        except Exception as e:
            print(e)
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
            try:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(
                        image_url_save_to_database,
                        database_pk,
                        image_url_1,
                        image_url_2,
                        image_url_3,
                        image_url_4,
                    )
            except Exception as e:
                print(e)

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
            return redirect("/blog-create/")

    elif request.method == "GET":
        return redirect("/blog-create/")
