# Generated by Django 4.1.3 on 2022-12-07 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0020_alter_imagegallery_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagegallery',
            name='slug',
        ),
    ]