# Generated by Django 3.2.8 on 2021-10-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0041_auto_20211018_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='subcategory_id',
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory_id',
            field=models.ManyToManyField(to='settings.CategoryModel'),
        ),
    ]
