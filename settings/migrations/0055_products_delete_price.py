# Generated by Django 3.2.8 on 2021-10-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0054_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='delete_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
