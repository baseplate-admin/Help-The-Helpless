from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=False
    )

    panels = [
        MultiFieldPanel(
            [FieldPanel("name"), ImageChooserPanel("image")], heading="Author info",
        ),
        MultiFieldPanel([FieldPanel("website")], heading="Links"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"
