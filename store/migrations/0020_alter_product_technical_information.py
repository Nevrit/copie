# Generated by Django 4.2 on 2023-05-02 15:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_product_technical_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='technical_information',
            field=ckeditor.fields.RichTextField(blank=True, default='', verbose_name='Fiche technique'),
        ),
    ]
