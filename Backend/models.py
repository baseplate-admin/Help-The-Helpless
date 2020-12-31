from django.db import models


# Create your models here.


class Backend(models.Model):
    facebook_url = models.URLField()
    youtube_url = models.URLField()
    email_url = models.EmailField()
    site_title = models.CharField(max_length=20, default="Title")
    site_description = models.CharField(max_length=50, default="Description")
    github_username = models.CharField(max_length=20, default="Github Username")
    github_tag = models.CharField(max_length=3, default="1.0")
    github_repo = models.CharField(max_length=50, default="Github Repo Name")
    favicon = models.TextField(default="Favicon")
    logo = models.TextField(default="Main logo")
    reload = models.IntegerField(default=0)
    extra = models.CharField(max_length=7, default="backend")

    def __str__(self):
        return str(self.id)
