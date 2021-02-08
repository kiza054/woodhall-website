from django.shortcuts import reverse
from main_website.models import Article
from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    
    def items(self):
        return [
                'main_website_home', 
                'main_website_about', 
                'main_website_search', 
                'main_website_article_create', 
                'main_website_waiting_list_register',
                'main_website_gallery',
                'main_website_gallery_upload',
                'main_website_help_us',
                'main_website_ways_to_donate',
                'main_website_contact_us'
                # These links are hidden from people who do not have access
                #'main_website_article_detail', 
                #'main_website_article_update',
                #'main_website_article_delete',
                #'main_website_article_tags',
                #'main_website_calendar',
                #'main_website_calendar_new_event',
                #'main_website_calendar_edit_event',
        ]
    
    def location(self, item):
        return reverse(item)
"""
class NewsUpdatesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.date_posted

    def location(self, item):
        return reverse(item)
"""