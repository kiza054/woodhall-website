from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):

    class Status(models.IntegerChoices):
        Draft = 0
        Published = 1

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scouts_blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=Status.choices, default=Status.Draft)
    likes = models.ManyToManyField(User, related_name="scouts_blog_posts_likes")

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
    image = models.ImageField(upload_to='media/post_images/scouts/%Y/%B/', blank=True, null=True)

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='scouts_blog_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class File(models.Model):
    name = models.CharField(max_length=25, blank=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='media/scouts/documents/%Y/%B/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name