from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from beavers.models import Post


class BeaversStaticViewSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'beavers_blog_home',
            'beavers_blog_about',
            'beavers_blog_search',
            'beavers_blog_file_upload',
            'beavers_blog_downloads',
            
        ]
    
    def location(self, item):
        return reverse(item)

class BeaversBlogPostsSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted