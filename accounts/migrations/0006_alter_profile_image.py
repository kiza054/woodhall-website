# Generated by Django 3.2.5 on 2021-09-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]