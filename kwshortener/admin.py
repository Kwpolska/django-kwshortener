from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'clickable_slug', 'clickable_url', 'visible')


admin.site.register(Link, LinkAdmin)
