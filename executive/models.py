from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class QuartermastersItemInventory(models.Model):

    class Categories(models.TextChoices):
        Unspecified = 'Unspecified', _('Unspecified')
        Camp_Equipment = 'Camp Equipment', _('Camp Equipment')
        Sports_Equipement = 'Sports Equipment', _('Sports Equipment')
        Cooking_Equipment = 'Cooking Equipment', _('Cooking Equipment')
        General_Equipment = 'General Equipment', _('General Equipment')

    item_name = models.CharField(max_length=200, unique=True)
    item_quantity = models.IntegerField(default=1)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(choices=Categories.choices, default=Categories.Unspecified, help_text=_('Category of item'), max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
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