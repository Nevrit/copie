# Generated by Django 4.1.5 on 2023-01-30 15:27

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('stock_quantity', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=['name'])),
            ],
        ),
    ]
