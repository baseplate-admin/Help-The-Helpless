from django.db import models
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

# Create your models here.
from wagtail.core.models import Page
from about import blocks


class AboutUs(Page):
    template = "about/about_us_page.html"
    max_count = 1

    page_title = models.CharField(max_length=50)

    content = StreamField(
        [("full_richtext", blocks.RichtextBlock()),], null=True, blank=True
    )
    content_panels = Page.content_panels + [StreamFieldPanel("content")]

    class Meta:
        verbose_name = "About Us"

