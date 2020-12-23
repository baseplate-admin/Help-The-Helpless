from django.db import models

# Create your models here.

class UrlLink(models.Model):
    facebook_url = models.URLField(default="null")
    youtube_url = models.URLField(default="null")
    email_url = models.CharField(max_length=20, default="null")
    extra = models.CharField(max_length=4, default="null")

    def __str__(self):
        return str(self.id)
