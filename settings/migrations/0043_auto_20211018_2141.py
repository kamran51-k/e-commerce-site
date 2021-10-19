# Generated by Django 3.2.8 on 2021-10-18 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0042_auto_20211018_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='subcategory_id',
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='settings.categorymodel'),
            preserve_default=False,
        ),
    ]
