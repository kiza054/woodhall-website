# Generated by Django 3.1.4 on 2020-12-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0002_auto_20201227_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last name')),
                ('date_of_birth', models.DateField(help_text='DD/MM/YYYY or DD-MM-YYYY', max_length=200, verbose_name='date of birth')),
                ('section_of_interest', models.IntegerField(choices=[(0, 'Beavers'), (1, 'Cubs'), (2, 'Scouts'), (3, 'Unsure of Section')], default=3, help_text='Section that your child wants to join')),
                ('name_of_parent_carer', models.CharField(max_length=200, verbose_name='name of parent/carer')),
                ('parent_carer_email', models.EmailField(max_length=254, verbose_name='email address of parent/carer')),
                ('parent_carer_phone_number', models.CharField(max_length=20, verbose_name='phone number of parent/carer')),
                ('parent_carer_address', models.CharField(max_length=200, verbose_name='address of parent/carer')),
                ('date_of_submission', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Decide whether you want to Publish the news article or save it as a Draft'),
        ),
    ]
