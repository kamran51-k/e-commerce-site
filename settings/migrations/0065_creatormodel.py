# Generated by Django 3.2.8 on 2021-11-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0064_auto_20211102_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('profession', models.CharField(blank=True, max_length=30, null=True)),
                ('company', models.CharField(blank=True, max_length=30, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images_folder')),
                ('about', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
