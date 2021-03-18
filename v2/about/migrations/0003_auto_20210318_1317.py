# Generated by Django 3.1.7 on 2021-03-18 07:17

import about.blocks
from django.db import migrations, models
import django.utils.timezone
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_auto_20210318_1007"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="aboutus", options={"verbose_name": "About Us"},
        ),
        migrations.AddField(
            model_name="aboutus",
            name="content",
            field=wagtail.core.fields.StreamField(
                [("full_richtext", about.blocks.RichtextBlock())], blank=True, null=True
            ),
        ),
        migrations.AddField(
            model_name="aboutus",
            name="page_title",
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]