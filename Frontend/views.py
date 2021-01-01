from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse

from Backend.models import Backend

# Create your views here.


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
            {"backend": backend, "site_header": "Home",},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


def redirect_to_home(request):
    return redirect("/home/")

def index(request):
    return render(request, 'front/index/index.html')

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
            {"site_header": "Donate", "backend": backend,},
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
            {"backend": backend, "site_header": "Blog",},
        )
    else:
        return HttpResponse("<h1>No POST allowed</h1>")


@gzip_page
def blog_create(request):
    if request.method == "GET":
        backend = Backend.objects.get(extra="backend")
        return render(request, "front/blog-create/index.html", {"backend": backend})
    else:
        return redirect("/home/")


@gzip_page
def blog_create_handler(request):
    if request.method == "POST":
        header = request.POST.get("header")
        div_ = request.POST.get("div_")             #   1
        divv = request.POST.get("divv")             #   2
        divvv_ = request.POST.get("divvv_")         #   3
        divvvv_ = request.POST.get("divvvv_")       #   4
        text = request.POST.get("text")             #   1
        text_1 = request.POST.get("image_text1")    #   2
        text_2 = request.POST.get("image_text2")    #   3
        text_3 = request.POST.get("image_text3")    #   4
        image_title_1 = request.POST.get("title1")  #   1
        image_title_2 = request.POST.get("title2")  #   2
        image_title_3 = request.POST.get("title3")  #   3
        image_title_4 = request.POST.get("title4")  #   4
    elif request.method == "GET":
        return redirect("/blog-create/")
