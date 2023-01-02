from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from cubs.models import Post


class CubsStaticViewSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return [
            'cubs_blog_home',
            'cubs_blog_about',
            'cubs_blog_search',
            'cubs_blog_file_upload',
            'cubs_blog_downloads',
            
        ]
    
    def location(self, item):
        return reverse(item)

class CubsBlogPostsSitemap(Sitemap):
    changefreq = 'hourly'
    priority = 1
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted