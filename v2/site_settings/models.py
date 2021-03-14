from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text="Facebook Url")
    email = models.URLField(blank=True, null=True, help_text="Email Url")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube Url")
    main_logo = models.URLField(blank=True, null=True, help_text="Main Logo Url")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("email"),
                FieldPanel("youtube"),
                FieldPanel("main_logo"),
            ],
            heading="Social Media Settings",
        )
    ]


@register_setting
class SiteNameSettings(BaseSetting):
    site_name = models.CharField(max_length=30)
    site_description = models.CharField(max_length=100)

    site_url_title = models.CharField(max_length=30)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_url_title"),
                FieldPanel("site_name"),
                FieldPanel("site_description"),
            ]
        )
    ]
