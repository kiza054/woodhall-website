# Generated by Django 3.2.5 on 2021-09-03 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0005_post_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='PostImage',
        ),
    ]
