# Generated by Django 3.2.8 on 2021-10-13 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0031_auto_20211013_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='post_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='settings.navbarmodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]