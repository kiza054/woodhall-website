from django.urls import path

from main_website import views
from main_website.views import (
    IndexView, 
    AboutView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView,
    TaggedView, 
    CalendarView,
    EventView,
    EditEventView, 
    HelpUsView, 
    SearchView, 
    ContactUsView,
    DonateView,
    ImageGalleryView,
    ImageDetailView,
    ImageAddView,
    ImageCategoryAddView
)

urlpatterns = [
    path('', IndexView.as_view(), name='main_website_home'),
    path('about', AboutView.as_view(), name='main_website_about'),
    path('search/', SearchView.as_view(), name='main_website_search'),
    path('article_create', ArticleCreateView.as_view(), name='main_website_article_create'),
    path('article/<slug:slug>', views.article_detail, name='main_website_article_detail'),
    path('article/update/<slug:slug>/', ArticleUpdateView.as_view(), name='main_website_article_update'),
    path('article/delete/<slug:slug>/', ArticleDeleteView.as_view(), name='main_website_article_delete'),
    path('tags/<slug:slug>/articles/', TaggedView.as_view(), name="main_website_article_tags"),
    path('calendar/', CalendarView.as_view(), name='main_website_calendar'),
    path('calendar/event/new/', EventView.as_view(), name='main_website_calendar_new_event'),
	path('calendar/event/edit/<event_id>/', EditEventView.as_view(), name='main_website_calendar_edit_event'),
    path('waiting_list/register', views.waiting_list_register, name='main_website_waiting_list_register'),
    path('gallery', ImageGalleryView.as_view(), name='main_website_gallery'),
    path('gallery/upload', ImageAddView.as_view(), name='main_website_gallery_upload'),
    path('gallery/category/add/', ImageCategoryAddView.as_view(), name='main_website_gallery_add_category'),
    path('gallery/image/<str:pk>/', ImageDetailView.as_view(), name='main_website_gallery_image_detail'),
    path('help_us', HelpUsView.as_view(), name='main_website_help_us'),
    path('ways_to_donate', DonateView.as_view(), name='main_website_ways_to_donate'),
    path('contact_us', ContactUsView.as_view(), name='main_website_contact_us')
]