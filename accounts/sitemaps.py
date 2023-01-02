from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class AccountsStaticViewSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'profile',
            'register',
            'login',
            'logout'            
        ]
    
    def location(self, item):
        return reverse(item)