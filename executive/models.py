from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

CATEGORIES = (
    ("Unspecified", "Unspecified"),
    ("Camp Equipment", "Camp Equipment"),
    ("Sports Equipment", "Sports Equipment"), 
    ("Cooking Equipment", "Cooking Equipment"),
    ("General Equipment", "General Equipment")
)

class QuartermastersItemInventory(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(choices=CATEGORIES, default=0, help_text=_('Category of item'), max_length=200)
    added_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    class Meta:
	    verbose_name = ('Inventory Item')
	    verbose_name_plural = ('Inventory Items')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.item_name)
        super(QuartermastersItemInventory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('executive_quartermaster_database', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.item_name}"