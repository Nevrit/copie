# Generated by Django 5.0.6 on 2024-06-20 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_alter_orderorder_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderorder',
            name='product',
        ),
    ]