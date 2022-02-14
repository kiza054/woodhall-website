# Generated by Django 4.0.1 on 2022-02-14 20:29

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='section',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], max_length=3),
        ),
    ]
