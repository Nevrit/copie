# Generated by Django 4.2 on 2023-05-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mark',
        ),
        migrations.AddField(
            model_name='category',
            name='mark',
            field=models.CharField(default='', max_length=50),
        ),
    ]