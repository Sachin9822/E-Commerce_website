# Generated by Django 4.1.3 on 2022-12-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_sellerorders_id_sellerorders_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerorders',
            name='item',
        ),
        migrations.AddField(
            model_name='sellerorders',
            name='item',
            field=models.ManyToManyField(default=None, to='core.items'),
        ),
    ]
