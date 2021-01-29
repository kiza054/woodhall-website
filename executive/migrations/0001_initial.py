# Generated by Django 3.1.4 on 2021-01-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuartermastersItemInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.IntegerField(choices=[(0, 'Unspecified'), (1, 'Camp Equipment'), (2, 'Sports Equipment'), (3, 'Cooking Equipment'), (4, 'General Equipment')], default=0, help_text='Category of item')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
