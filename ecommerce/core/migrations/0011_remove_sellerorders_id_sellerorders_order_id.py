# Generated by Django 4.1.3 on 2022-12-15 20:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_sellerorders_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerorders',
            name='id',
        ),
        migrations.AddField(
            model_name='sellerorders',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
