# Generated by Django 4.1.3 on 2022-11-24 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beavers', '0007_auto_20210906_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='beavers_blog_posts_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
