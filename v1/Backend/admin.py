from django.contrib import admin
import Backend.models as backend
import Frontend.models as frontend

admin.site.register(backend.Backend)
admin.site.register(frontend.Blog)
admin.site.register(frontend.Comments)
