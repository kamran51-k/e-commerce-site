# Generated by Django 3.2.8 on 2021-10-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0039_categorymodel_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='url',
        ),
    ]
