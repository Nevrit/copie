# Generated by Django 5.0.6 on 2024-06-20 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_orderorder_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderorder',
            name='product',
        ),
    ]