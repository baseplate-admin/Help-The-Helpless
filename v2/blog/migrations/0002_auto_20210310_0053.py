# Generated by Django 3.1.7 on 2021-03-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AddField(
            model_name='blog',
            name='page_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]