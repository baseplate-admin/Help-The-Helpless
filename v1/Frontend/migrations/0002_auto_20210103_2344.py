# Generated by Django 3.1.4 on 2021-01-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Frontend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image_1",
            field=models.ImageField(default=None, upload_to="images"),
        ),
        migrations.AddField(
            model_name="blog",
            name="image_2",
            field=models.ImageField(default=None, upload_to="images"),
        ),
        migrations.AddField(
            model_name="blog",
            name="image_3",
            field=models.ImageField(default=None, upload_to="images"),
        ),
        migrations.AddField(
            model_name="blog",
            name="image_4",
            field=models.ImageField(default=None, upload_to="images"),
        ),
    ]
