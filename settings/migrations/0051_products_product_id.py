# Generated by Django 3.2.8 on 2021-10-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0050_auto_20211020_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_id',
            field=models.ManyToManyField(to='settings.CategoryModel'),
        ),
    ]
