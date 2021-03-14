from django.db import models

# Create your models here.
from wagtail.core.models import Page


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
