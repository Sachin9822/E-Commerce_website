# Generated by Django 4.1.3 on 2022-12-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_items_seller_alter_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
