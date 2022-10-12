from django.contrib import admin
from .models import *


class URLsAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'views', 'created_at')


admin.site.register(URLs, URLsAdmin)
