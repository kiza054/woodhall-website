from cubs.models import Post
from django.shortcuts import reverse
from django.contrib.sitemaps import Sitemap

class CubsStaticViewSitemap(Sitemap):
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
    changefreq = "weekly"
    priority = 1

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted