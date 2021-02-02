from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

SECTIONS = (
    (0, "Beavers"),
    (1, "Cubs"), 
    (2, "Scouts"),
    (3, "Unsure of Section")
)

class Article(models.Model):
    article_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_updates')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    tags = TaggableManager()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0, help_text=_('Decide whether you want to Publish the news article or save it as a Draft'))

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.article_name
    
    def get_absolute_url(self):
        return reverse("main_website_article_detail", kwargs={"slug": str(self.slug)})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_name)
        super(Article, self).save(*args, **kwargs)

class WaitingList(models.Model):
    first_name = models.CharField(_('first name'), max_length=200)
    last_name = models.CharField(_('last name'), max_length=200)
    date_of_birth = models.DateField(_('date of birth'), max_length=200, help_text=_('DD/MM/YYYY or DD-MM-YYYY'))
    section_of_interest = models.IntegerField(choices=SECTIONS, default=3, help_text=_('Section that your child wants to join'))
    name_of_parent_carer = models.CharField(_('name of parent/carer'), max_length=200)
    parent_carer_email = models.EmailField(_('email of parent/carer'), max_length=254)
    parent_carer_phone_number = models.CharField(_('phone number of parent/carer'), max_length=20)
    parent_carer_address = models.CharField(_('address of parent/carer'), max_length=200)
    date_of_submission = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Waiting List Entry'
        verbose_name_plural = 'Waiting List Entries'

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

    def __str__(self):
        return f"{self.title}"

class ImageGallery(models.Model):
    file_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/image_gallery/%Y/%B/', blank=False, null=False)

    def __str__(self):
        return self.file_name