from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from scouts.models import Post


class ScoutsStaticViewSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'scouts_blog_home',
            'scouts_blog_about',
            'scouts_blog_search',
            'scouts_blog_file_upload',
            'scouts_blog_downloads',
            
        ]
    
    def location(self, item):
        return reverse(item)

class ScoutsBlogPostsSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted