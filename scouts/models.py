from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Post(models.Model):

    class Status(models.TextChoices):
        Draft = 'Draft', _('Draft')
        Published = 'Published', _('Published')

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scouts_blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.Draft)
    likes = models.ManyToManyField(User, blank=True, related_name="scouts_blog_posts_likes")

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("scouts_blog_post_detail", kwargs={"slug": str(self.slug)})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scouts_blog_post_images')
    image = models.ImageField(upload_to='media/post_images/scouts/%Y/%B/', blank=True, null=True) # When in development remove 'media/' in upload_to

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scouts_blog_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class File(models.Model):
    name = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='media/scouts/documents/%Y/%B/') # When in development remove 'media/' in upload_to
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name