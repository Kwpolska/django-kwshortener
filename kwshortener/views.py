from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Link
import operator


def index(request):
    if 'l' in request.GET:
        context = {
            'pid': 'listing',
            'title': 'Listing',
            'htmltitle': 'Listing | go.chriswarrick.com',
            'urls': filter(operator.attrgetter('visible'), Link.objects.order_by('slug')),
        }
        return render(request, 'kwshortener/listing.html', context)
    else:
        context = {
            'pid': 'index',
            'title': 'go.chriswarrick.com',
            'htmltitle': 'go.chriswarrick.com',
        }
        return render(request, 'kwshortener/index.html', context)


def go(request, slug):
    try:
        link = Link.objects.get(slug=slug)
        link.clicks += 1
        link.save()
        return HttpResponseRedirect(link.url, '<h1>302 Found</h1>\n<a href="{0}">{0}</a>\n'.format(link.url))
    except Link.DoesNotExist:
        context = {
            'pid': '404',
            'title': '404 Not Found',
            'htmltitle': '404 Not Found | go.chriswarrick.com',
        }
        return HttpResponseNotFound(render(request, 'kwshortener/404.html', context))
