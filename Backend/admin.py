from django.contrib import admin
import Backend.models as models

admin.site.register(models.UrlLink)
admin.site.register(models.SiteTitle)
admin.site.register(models.SiteDescription)
