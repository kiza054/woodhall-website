"""
woodhall_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import main_website
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from cubs.sitemaps import CubsStaticViewSitemap, CubsBlogPostsSitemap
from main_website.sitemaps import StaticViewSitemap, NewsUpdatesSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'cubs_static': CubsStaticViewSitemap,
    'news_updates': NewsUpdatesSitemap,
    'cubs_blog_posts': CubsBlogPostsSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/beavers/', include('beavers.urls')),
    path('blog/cubs/', include('cubs.urls')),
    path('blog/scouts/', include('scouts.urls')),
    path('executive/', include('executive.urls')),
    path('', include('accounts.urls')),
    path('', include('main_website.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]

handler403 = main_website.views.error_403_view
handler404 = main_website.views.error_404_view
handler500 = main_website.views.error_500_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)