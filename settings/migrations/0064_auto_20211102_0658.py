# Generated by Django 3.2.8 on 2021-11-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0063_auto_20211024_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=14)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='navbarmodel',
            name='slice',
        ),
        migrations.AddField(
            model_name='navbarmodel',
            name='url',
            field=models.URLField(default=False),
            preserve_default=False,
        ),
    ]
