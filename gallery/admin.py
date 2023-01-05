from django.contrib import admin

from gallery.models import ImageGallery, ImageGalleryCategory


class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'image')

class ImageGalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

admin.site.register(ImageGallery, ImageGalleryAdmin)
admin.site.register(ImageGalleryCategory, ImageGalleryCategoryAdmin)