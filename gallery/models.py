from django.db import models
from django.utils import timezone

from accounts.models import User

class ImageGalleryCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Image Categories'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class ImageGallery(models.Model):
    category = models.ForeignKey(ImageGalleryCategory, on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.CharField(max_length=50)
    date_time_stamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media/image_gallery/%Y/%B/', blank=False, null=False) # When in development remove 'media/' in upload_to
    description = models.TextField(null=False, blank=False, default=None)
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Image Gallery'

    def __str__(self):
        return self.file_name