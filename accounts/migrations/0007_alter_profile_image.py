# Generated by Django 3.2.5 on 2021-09-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]