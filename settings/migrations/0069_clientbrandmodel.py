# Generated by Django 3.2.8 on 2021-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0068_alter_creatormodel_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientBrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images_folder')),
                ('alt_name', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
