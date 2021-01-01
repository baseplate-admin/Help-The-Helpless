from django.db import models


class Blog(models.Model):
    username = models.CharField(max_length=50)
    date_time = models.CharField(max_length=23)
    header = models.CharField(max_length=50)
    content = models.TextField()
    extra = "blog"

    def __str__(self):
        return self.extra
