# Generated by Django 3.2.7 on 2021-10-06 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0017_categorymodel_category1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='category1',
        ),
    ]
