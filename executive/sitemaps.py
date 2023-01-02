from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from executive.models import QuartermastersItemInventory


class ExecutiveStaticViewSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return [
                'executive_home',
        ]
    
    def location(self, item):
        return reverse(item)