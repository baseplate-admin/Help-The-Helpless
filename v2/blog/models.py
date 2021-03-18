from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog import blocks
from blog.orderables import BlogAuthorsOrderable


# Create your models here.


class BlogPage(Page):
    template = "blog/blog_page.html"
    max_count = 1

    class Meta:
        verbose_name = "Blog"
        # verbose_name_plural = "Blogs"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_posts = (
            BlogDetailsPage.objects.live().public().order_by("-first_published_at")
        )

        paginator = Paginator(all_posts, 1)
        page = request.GET.get("page")

        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        return context


class BlogDetailsPage(Page):
    template = "blog/blog_details_page.html"
    blog_title = models.CharField(max_length=50)
    blog_image = models.ForeignKey(
        "wagtailimages.Image", blank=False, null=True, on_delete=models.SET_NULL,
    )

    content = StreamField(
        [("full_richtext", blocks.RichtextBlock()),], null=True, blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("blog_title"),
        ImageChooserPanel("blog_image"),
        MultiFieldPanel(
            [InlinePanel("blog_authors", label="Author", min_num=1, max_num=1)],
            heading="Author",
        ),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Blog Detail"
        verbose_name_plural = "Blog(s) Detail"

