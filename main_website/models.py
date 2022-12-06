from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from accounts.models import User


class Article(models.Model):
    article_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_updates')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    tags = TaggableManager()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, help_text=_('Decide whether you want to Publish the news article or save it as a Draft'))

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.article_name
    
    def get_absolute_url(self):
        return reverse("main_website_article_detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_name)
        super(Article, self).save(*args, **kwargs)

class WaitingList(models.Model):
    first_name = models.CharField(_('first name'), max_length=200)
    last_name = models.CharField(_('last name'), max_length=200)
    date_of_birth = models.DateField(_('date of birth'), max_length=200, help_text=_('DD/MM/YYYY or DD-MM-YYYY'))
    section_of_interest = models.CharField(max_length=30, help_text=_('Section that your child wants to join'))
    name_of_parent_carer = models.CharField(_('name of parent/carer'), max_length=200)
    parent_carer_email = models.EmailField(_('email of parent/carer'), max_length=254)
    parent_carer_phone_number = models.CharField(_('phone number of parent/carer'), max_length=20)
    parent_carer_address = models.CharField(_('address of parent/carer'), max_length=200)
    date_of_submission = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Waiting List Submission'
        verbose_name_plural = 'Waiting List Submissions'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('main_website_calendar_edit_event', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    class Meta:
        verbose_name = 'Group Event'
        verbose_name_plural = 'Group Events'

    def __str__(self):
        return f"{self.title}"

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

class UrgentAnnouncements(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urgent_announcements')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Urgent Announcements'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(UrgentAnnouncements, self).save(*args, **kwargs)
