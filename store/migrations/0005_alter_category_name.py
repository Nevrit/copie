# Generated by Django 4.1.5 on 2023-01-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=228),
        ),
    ]
