# Generated by Django 5.0.3 on 2024-04-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_material_is_published_material_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='material',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Превью'),
        ),
    ]
