from django.db import models


class Blog(models.Model):
    username = models.CharField(max_length=50)
    date_time = models.CharField(max_length=26)
    header = models.CharField(max_length=50)

    content_1 = models.TextField(default="")
    content_2 = models.TextField(default="")
    content_3 = models.TextField(default="")
    content_4 = models.TextField(default="")
    content_5 = models.TextField(default="")

    image_1_title = models.CharField(max_length=20, default="")
    image_2_title = models.CharField(max_length=20, default="")
    image_3_title = models.CharField(max_length=20, default="")
    image_4_title = models.CharField(max_length=20, default="")

    image_1 = models.ImageField(upload_to="images", default=None)
    image_2 = models.ImageField(upload_to="images", blank=True, default=None)
    image_3 = models.ImageField(upload_to="images", blank=True, default=None)
    image_4 = models.ImageField(upload_to="images", blank=True, default=None)

    image_1_url = models.URLField(default="")
    image_2_url = models.URLField(default="")
    image_3_url = models.URLField(default="")
    image_4_url = models.URLField(default="")

    extra = "blog"

    def __str__(self):
        return str(self.id)


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    comments = models.TextField()
    blog_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.blog_id)
