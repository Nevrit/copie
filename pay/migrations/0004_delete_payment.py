# Generated by Django 4.2.3 on 2023-07-15 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_rename_status_payment_autre_telephone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
