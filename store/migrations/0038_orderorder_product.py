# Generated by Django 5.0.6 on 2024-06-20 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_remove_orderorder_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]