# Generated by Django 3.2.9 on 2021-11-16 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_alter_inventory_item_item_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inventory_item',
            new_name='inventory_items',
        ),
    ]
