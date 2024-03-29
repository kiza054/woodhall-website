# Generated by Django 4.1.3 on 2022-12-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0018_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='imagegallery',
            name='image',
            field=models.ImageField(upload_to='image_gallery/%Y/%B/'),
        ),
    ]
