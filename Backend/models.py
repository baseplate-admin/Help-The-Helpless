from django.db import models

# Create your models here.


class UrlLink(models.Model):
    facebook_url = models.URLField()
    youtube_url = models.URLField()
    email_url = models.EmailField(max_length=20)
    extra = models.CharField(max_length=4, default="main")

    def __str__(self):
        return str(self.id)


class SiteTitle(models.Model):
    site_title = models.CharField(max_length=20, default="-")
    extra = models.CharField(max_length=5, default="title")

    def __str__(self):
        return str(self.extra)


class SiteDescription(models.Model):
    site_description = models.CharField(max_length=50, default="-")
    extra = models.CharField(max_length=11, default="description")

    def __str__(self):
        return str(self.extra)
