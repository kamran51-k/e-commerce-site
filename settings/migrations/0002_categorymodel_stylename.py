# Generated by Django 3.2.7 on 2021-10-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='stylename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
