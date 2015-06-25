from django.db import models
from django.utils.html import format_html

class Link(models.Model):
    title = models.CharField("Title", max_length=500)
    slug = models.SlugField("Slug", max_length=50)
    url = models.URLField("URL", max_length=500)
    visible = models.BooleanField("Visible", default=True)

    def clickable_title(self):
        return format_html('<a href="{0}">{1}</a>', '/' + self.slug, self.title)

    clickable_title.short_description = 'Title'
    clickable_title = property(clickable_title)

    def clickable_slug(self):
        return format_html('<a href="{0}">{1}</a>', '/' + self.slug, self.slug)

    clickable_slug.short_description = 'Slug'
    clickable_slug = property(clickable_slug)

    def clickable_url(self):
        return format_html('<a href="{0}">{0}</a>', self.url)


    clickable_url.short_description = 'URL'
    clickable_url = property(clickable_url)


    def __str__(self):
        return self.title
