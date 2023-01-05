from django.urls import path

from gallery.views import (ImageAddView, ImageCategoryAddView, ImageDetailView,
                           ImageGalleryView)

urlpatterns = [
    path('', ImageGalleryView.as_view(), name='gallery'),
    path('upload', ImageAddView.as_view(), name='gallery_upload'),
    path('category/add/', ImageCategoryAddView.as_view(), name='gallery_add_category'),
    path('image/<str:pk>/', ImageDetailView.as_view(), name='gallery_image_detail'),
]