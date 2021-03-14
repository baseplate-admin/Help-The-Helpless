from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from blog.snippets import BlogAuthor


@register_snippet(BlogAuthor)
class BlogAuthorsOrderable(Orderable):
    page = ParentalKey("blog.BlogDetailsPage", related_name="blog_authors")
    author = models.ForeignKey("blog.BlogAuthor", on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel("author"),
    ]
