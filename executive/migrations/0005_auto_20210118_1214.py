# Generated by Django 3.1.4 on 2021-01-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0004_auto_20210118_1207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuartermastersItemInventory',
            new_name='Item',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Quartermasters Item Inventory', 'verbose_name_plural': 'Quartermasters Item Inventories'},
        ),
    ]
