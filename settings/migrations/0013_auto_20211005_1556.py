# Generated by Django 3.2.7 on 2021-10-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RenameField(
            model_name='categorymodel',
            old_name='title',
            new_name='style',
        ),
        migrations.DeleteModel(
            name='StyleModel',
        ),
    ]
