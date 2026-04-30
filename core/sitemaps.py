from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return ['home', 'menu', 'gallery', 'reserve', 'faq']

    def location(self, item):
        return reverse(item)