# Generated by Django 4.1.3 on 2022-12-15 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_sellerorders_item_sellerorders_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerorders',
            name='item',
        ),
        migrations.AddField(
            model_name='sellerorders',
            name='item_id',
            field=models.IntegerField(default=-1),
        ),
    ]
