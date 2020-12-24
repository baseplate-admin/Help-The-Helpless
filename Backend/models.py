from django.db import models

# Create your models here.


class UrlLink(models.Model):
    facebook_url = models.URLField()
    youtube_url = models.URLField()
    email_url = models.EmailField(max_length=20)
    extra = models.CharField(max_length=4, default="main")

    def __str__(self):
        return str(self.id)
