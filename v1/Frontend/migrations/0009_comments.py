# Generated by Django 3.1.4 on 2021-01-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Frontend", "0008_auto_20210104_1752"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=50)),
                ("comments", models.TextField()),
            ],
        ),
    ]