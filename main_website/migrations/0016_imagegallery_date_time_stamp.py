# Generated by Django 4.0.1 on 2022-02-05 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0015_auto_20210904_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='date_time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
