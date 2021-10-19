# Generated by Django 3.2.8 on 2021-10-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0044_auto_20211018_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_id',
            field=models.ManyToManyField(to='settings.NavbarModel'),
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='products',
            name='id',
            field=models.BigAutoField(auto_created=True, default=False, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]