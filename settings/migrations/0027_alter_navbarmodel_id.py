# Generated by Django 3.2.8 on 2021-10-10 18:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0026_alter_navbarmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbarmodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
