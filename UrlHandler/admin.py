from django.contrib import admin
from UrlHandler.models import UrlLink

admin.site.register(UrlLink)
admin.site.disable_action('delete_selected')
