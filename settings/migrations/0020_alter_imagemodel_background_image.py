# Generated by Django 3.2.7 on 2021-10-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0019_imagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]