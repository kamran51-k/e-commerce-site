# Generated by Django 3.2.8 on 2021-11-02 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0066_auto_20211102_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image_id',
        ),
    ]
