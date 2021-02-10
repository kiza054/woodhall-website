from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils import timezone
from django.utils.text import slugify

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beavers_blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("beavers_blog_post_detail", kwargs={"slug": str(self.slug)})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='beavers_blog_post_images')
    image = models.ImageField(upload_to='media/post_images/beavers/', blank=True, null=True)

    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='beavers_blog_comments')
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
    file = models.FileField(upload_to='media/beavers/documents/%Y/%B/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name