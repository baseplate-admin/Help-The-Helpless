# Generated by Django 3.1.4 on 2020-12-25 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_auto_20201225_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_description', models.CharField(default='-', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SiteTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='-', max_length=20)),
            ],
        ),
    ]
