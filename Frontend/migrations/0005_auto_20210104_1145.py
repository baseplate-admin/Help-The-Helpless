# Generated by Django 3.1.4 on 2021-01-04 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_auto_20210104_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_1_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_2_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_3_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_4_url',
            field=models.URLField(),
        ),
    ]
