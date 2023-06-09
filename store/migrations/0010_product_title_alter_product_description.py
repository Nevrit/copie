# Generated by Django 4.1.5 on 2023-02-12 11:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
