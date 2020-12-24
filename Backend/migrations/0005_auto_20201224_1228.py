# Generated by Django 3.1.4 on 2020-12-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20201223_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urllink',
            name='email_url',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='urllink',
            name='extra',
            field=models.CharField(default='main', max_length=4),
        ),
        migrations.AlterField(
            model_name='urllink',
            name='facebook_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='urllink',
            name='youtube_url',
            field=models.URLField(),
        ),
    ]
