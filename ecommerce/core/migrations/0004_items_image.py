# Generated by Django 4.1.3 on 2022-12-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_items_category_alter_items_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
